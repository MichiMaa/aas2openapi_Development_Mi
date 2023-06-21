from __future__ import annotations

import json
from urllib import parse

from basyx.aas import model

from typing import Union
from pydantic import BaseModel, Field

from aas2openapi.models import base

def get_vars(obj: object) -> dict:
    vars_dict = vars(obj)
    vars_dict = {key: value for key, value in vars_dict.items() if key[0] != "_"}
    vars_dict = {key: value for key, value in vars_dict.items() if value is not None}
    vars_dict = {key: value for key, value in vars_dict.items() if key != "id_"}
    vars_dict = {key: value for key, value in vars_dict.items() if key != "description"}
    vars_dict = {key: value for key, value in vars_dict.items() if key != "id_short"}
    return vars_dict


def convert_pydantic_model_to_aas(
    aas: base.AAS,
) -> model.DictObjectStore[model.Identifiable]:
    """
    Convert a pydantic model to an AssetAdministrationShell and return it as a DictObjectStore with all Submodels

    Args:
        pydantic_aas (base.AAS): pydantic model to convert

    Returns:
        model.DictObjectStore[model.Identifiable]: DictObjectStore with all Submodels
    """
    aas_attributes = get_vars(aas)
    aas_submodels = []  # placeholder for submodels created
    for attribute_name, attribute_value in aas_attributes.items():
        if isinstance(attribute_value, base.Submodel):
            tempsubmodel = create_submodel(
                attribute_name=attribute_name, attribute_value=attribute_value
            )
            aas_submodels.append(tempsubmodel)

    asset_information = model.AssetInformation(
    )

    aas = model.AssetAdministrationShell(
        asset_information=asset_information,
        id_short=aas.id_,
        id_=aas.id_,
        submodel={
            model.ModelReference.from_referable(submodel) for submodel in aas_submodels
        },
    )
    obj_store: model.DictObjectStore[model.Identifiable] = model.DictObjectStore()
    obj_store.add(aas)
    for sm in aas_submodels:
        obj_store.add(sm)
    return obj_store


def get_id_short(
    element: Union[
        base.Submodel, base.SubmodelElementCollection, base.SubmodelElementList
    ]
) -> str:
    if element.id_short:
        return element.id_short
    else:
        return element.id_


def create_submodel(
    attribute_name: str, attribute_value: base.Submodel
) -> model.Submodel:
    submodel = model.Submodel(
        id_short=get_id_short(attribute_value),
        id_=attribute_value.id_,
        description=model.LangStringSet({"en": attribute_value.description})
    )

    submodel_attributes = get_vars(attribute_value)

    for sm_attribute_name, sm_attribute_value in submodel_attributes.items():
        submodel_element = create_submodel_element(
            sm_attribute_name, sm_attribute_value
        )
        submodel.submodel_element.add(submodel_element)
    return submodel


def create_submodel_element(
    attribute_name: str,
    attribute_value: Union[
        base.SubmodelElementCollection, str, float, int, bool, tuple, list, set
    ]
) -> model.SubmodelElement:
    if isinstance(attribute_value, base.SubmodelElementCollection):
        smc = create_submodel_element_collection(attribute_value, attribute_name)
        return smc
    elif isinstance(attribute_value, list) or isinstance(attribute_value, tuple):
        sml = create_submodel_element_list(attribute_name, attribute_value)
        return sml
    elif isinstance(attribute_value, set):
        sml = create_submodel_element_list(attribute_name, attribute_value, ordered=False)
        return sml
    elif (isinstance(attribute_value, str)) and (
        (
            parse.urlparse(attribute_value).scheme
            and parse.urlparse(attribute_value).netloc
        )
        or (attribute_value.split("_")[-1] in ["id", "ids"])
    ):
        key = model.Key(
            type_=model.KeyTypes.ASSET_ADMINISTRATION_SHELL,
            value=attribute_value,
        )
        reference = model.ModelReference(key=(key,), type_="")
        reference_element = model.ReferenceElement(
            id_short=attribute_name,
            value=reference,
        )
        return reference_element
    else:
        property = create_property(attribute_name, attribute_value)

        return property


def get_value_type_of_attribute(
    attribute: Union[str, int, float, bool]
) -> model.datatypes:
    if isinstance(attribute, int):
        return model.datatypes.Integer
    elif isinstance(attribute, float):
        return model.datatypes.Double
    elif isinstance(attribute, bool):
        return model.datatypes.Boolean
    else:
        return model.datatypes.String


def create_property(
    attribute_name: str, attribute_value: Union[str, int, float, bool]
) -> model.Property:
    property = model.Property(
        id_short=attribute_name,
        value_type=get_value_type_of_attribute(attribute_value),
        value=attribute_value,
    )
    return property


def create_submodel_element_collection(
    pydantic_submodel_element_collection: base.SubmodelElementCollection, name: str
) -> model.SubmodelElementCollection:
    value = []
    smc_attributes = get_vars(pydantic_submodel_element_collection)

    for attribute_name, attribute_value in smc_attributes.items():
        sme = create_submodel_element(attribute_name, attribute_value)
        value.append(sme)

    smc = model.SubmodelElementCollection(
        id_short=name,
        value=value,
    )
    return smc


def create_submodel_element_list(name: str, value: list, ordered=True) -> model.SubmodelElementList:
    submodel_elements = []
    for el in value:
        submodel_element = create_submodel_element(name, el)
        submodel_elements.append(submodel_element)

    sml = model.SubmodelElementList(
        id_short=name,
        type_value_list_element=type(submodel_elements[0]),
        value=submodel_elements,
        order_relevant=ordered
    )
    return sml


from ba_syx_aas_repository_client.models import (
    AssetInformationAssetKind,
)
import basyx.aas.adapter.json.json_serialization


class ClientModel(BaseModel):
    basyx_object: Union[model.AssetAdministrationShell, model.Submodel]

    class Config:
        arbitrary_types_allowed = True

    def to_dict(self) -> dict:
        basyx_json_string = json.dumps(self.basyx_object, cls=basyx.aas.adapter.json.AASToJsonEncoder)
        data = json.loads(basyx_json_string)
        if isinstance(self.basyx_object, model.AssetAdministrationShell):
            value = data["assetInformation"]["assetKind"]
            if value == "Instance":
                data["assetInformation"]["assetKind"] = AssetInformationAssetKind.INSTANCE
            if value == "Type":
                data["assetInformation"]["assetKind"] = AssetInformationAssetKind.TYPE            
        return data