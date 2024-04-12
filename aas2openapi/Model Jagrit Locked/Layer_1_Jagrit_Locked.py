from __future__ import annotations
from typing import List, Optional, Tuple
from pydantic import BaseModel, validator, root_validator
from datetime import datetime
from decimal import Decimal

from aas2openapi.models.base import AAS, Submodel, SubmodelElementCollection

class KPI(Submodel):
    range: Optional[Tuple[float, float]]
    target: Optional[float]
    actual_value: Optional[float]

    @validator("range")
    def validate_range(cls, v):
        if v is not None and v[0] > v[1]:
            raise ValueError("Range minimum must be less than or equal to range maximum")
        return v

    @root_validator
    def validate_target_and_actual(cls, values):
        range_min = values.get("range", (None, None))[0]
        range_max = values.get("range", (None, None))[1]
        target = values.get("target")
        actual_value = values.get("actual_value")

        if target is not None and (target < range_min or target > range_max):
            raise ValueError("Target value must be within the specified range")

        if actual_value is not None and (actual_value < range_min or actual_value > range_max):
            raise ValueError("Actual value must be within the specified range")

        return values

class Components(SubmodelElementCollection):

    pass

class SubComponents(SubmodelElementCollection):

    pass

class Material(SubmodelElementCollection):

    pass

class BOM(SubmodelElementCollection):

    components: Components
    sub_components: SubComponents
    materials: Material

class Product(Submodel):

    product_group: str
    bom: BOM

class RequiredProcesses(SubmodelElementCollection):

    pass

class Order(Submodel):

    order_type: str
    quantity: str
    time_of_order: datetime
    required_processes: RequiredProcesses

class RequiredCapabilities(SubmodelElementCollection):

    pass

class Process(Submodel):

    processType: str
    required_capabilities: RequiredCapabilities

class Parameters(SubmodelElementCollection):

    pass

class Resources(Submodel):

    resourceType: str
    position: Decimal

class Capability(Submodel):

    capabilityType: str
    parameters: Parameters

class Layer1(AAS):

    kpi: KPI
    product: Product
    order: Order
    process: Process
    resources: Resources
    capability: Capability

# Example instance
layer1 = Layer1(
    id="id1",
    id_short="Layer1",
    description="Asset Administration Shell for Layer 1",
    kpi=KPI(
        id="id2",
        id_short="KPI",
        description="Key Performance Indicators",
        range=(0.0, 1.0),
        target=0.8,
        actual_value=0.7
    ),
    product=Product(
        id="id3",
        id_short="Product",
        description="Product information",
        product_group="Electronics",
        bom=BOM(
            id="id4",
            id_short="BOM",
            description="Bill of Materials",
            components=Components(
                id="id5",
                id_short="Components",
                description="Components"
            ),
            sub_components=SubComponents(
                id="id6",
                id_short="SubComponents",
                description="Sub-Components"
            ),
            materials=Material(
                id="id7",
                id_short="Material",
                description="Materials"
            )
        )
    ),
    order=Order(
        id="id8",
        id_short="Order",
        description="Order information",
        order_type="Production",
        quantity="100",
        time_of_order="2023-04-05T12:00:00",
        required_processes=RequiredProcesses(
            id="id9",
            id_short="RequiredProcesses",
            description="Required Processes"
        )
    ),
    process=Process(
        id="id10",
        id_short="Process",
        description="Process information",
        processType="Manufacturing",
        required_capabilities=RequiredCapabilities(
            id="id11",
            id_short="RequiredCapabilities",
            description="Required Capabilities"
        )
    ),
    resources=Resources(
        id="id12",
        id_short="Resources",
        description="Resources information",
        resourceType="Machine",
        position=10.5
    ),
    capability=Capability(
        id="id13",
        id_short="Capability",
        description="Capability information",
        capabilityType="Manufacturing",
        parameters=Parameters(
            id="id14",
            id_short="Parameters",
            description="Parameters"
        )
    )
)

