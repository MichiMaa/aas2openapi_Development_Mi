from __future__ import annotations

from typing import Optional, List, Union, Literal
from pydantic.dataclasses import dataclass

from aas2openapi.models.base import AAS, Submodel, SubmodelElementCollection


class Layer1(AAS):
    Product: [Product]
    KPI: [KPI]


#Product SM
class Product(Submodel):
    product_group:str
    BOM: [BOM]

class BOM(SubmodelElementCollection):
    components: str
    subcomponents: str
    material: str

#KPI SM
class KPI(Submodel):
    target: str



