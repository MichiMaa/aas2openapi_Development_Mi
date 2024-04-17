from __future__ import annotations
from typing import List, Optional, Tuple
from pydantic import BaseModel, validator, root_validator

from aas2openapi.models.base import AAS, Submodel, SubmodelElementCollection

class KPI(Submodel):
    """
    Submodel for Key Performance Indicators.
    """
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

class Component(BaseModel):
    """
    Class representing a component.
    """
    name: str
    description: str

class Components(SubmodelElementCollection):
    """
    Submodel element collection for Components.
    """
    components: List[Component]

class SubComponent(BaseModel):
    """
    Class representing a sub-component.
    """
    name: str
    description: str

class SubComponents(SubmodelElementCollection):
    """
    Submodel element collection for Sub-Components.
    """
    sub_components: List[SubComponent]

class MaterialProperty(BaseModel):
    """
    Class representing a material property.
    """
    name: str
    value: str
    unit: str

class Material(SubmodelElementCollection):
    """
    Submodel element collection for Materials.
    """
    material_name: str
    properties: List[MaterialProperty]
    sub_materials: Optional[List['Material']] = None

    @validator('sub_materials', each_item=True)
    def validate_sub_materials(cls, value):
        if not isinstance(value, Material):
            raise ValueError("sub_materials must be instances of Material")
        return value

class BOM(SubmodelElementCollection):
    """
    Submodel for Bill of Materials.
    """
    components: Components
    sub_components: SubComponents
    materials: Material

class Product(Submodel):
    """
    Submodel for Product information.
    """
    product_group: str
    bom: BOM

class RequiredProcess(BaseModel):
    """
    Class representing a required process.
    """
    name: str
    description: str

class RequiredProcesses(SubmodelElementCollection):
    """
    Submodel element collection for Required Processes.
    """
    required_processes: List[RequiredProcess]

class Order(Submodel):
    """
    Submodel for Order information.
    """
    order_type: str
    quantity: str
    time_of_order: str
    required_processes: RequiredProcesses

class RequiredCapability(BaseModel):
    """
    Class representing a required capability.
    """
    name: str
    description: str

class RequiredCapabilities(SubmodelElementCollection):
    """
    Submodel element collection for Required Capabilities.
    """
    required_capabilities: List[RequiredCapability]

class Process(Submodel):
    """
    Submodel for Process information.
    """
    processType: str
    required_capabilities: RequiredCapabilities

class Parameter(BaseModel):
    """
    Class representing a parameter.
    """
    name: str
    value: str
    unit: str

class Parameters(SubmodelElementCollection):
    """
    Submodel element collection for Parameters.
    """
    parameters: List[Parameter]

class Resources(Submodel):
    """
    Submodel for Resources information.
    """
    resourceType: str
    position: float

class Capability(Submodel):
    """
    Submodel for Capability information.
    """
    capabilityType: str
    parameters: Parameters

class Layer1(AAS):
    """
    Asset Administration Shell for Layer 1.
    """
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
                id_short="Components",
                description="Components",
                components=[
                    Component(name="CPU", description="Central Processing Unit"),
                    Component(name="RAM", description="Random Access Memory")
                ]
            ),
            sub_components=SubComponents(
                id_short="SubComponents",
                description="Sub-Components",
                sub_components=[
                    SubComponent(name="Resistor", description="Electronic resistor"),
                    SubComponent(name="Capacitor", description="Electronic capacitor")
                ]
            ),
            materials=Material(
                id_short="Materials",
                description="Materials",
                material_name="Plastic",
                properties=[
                    MaterialProperty(name="Density", value="1.2", unit="g/cm³"),
                    MaterialProperty(name="Melting Point", value="200", unit="°C")
                ],
                sub_materials=[
                    Material(
                        id_short="SubMaterial",
                        description="Sub-Material",
                        material_name="ABS",
                        properties=[
                            MaterialProperty(name="Tensile Strength", value="40", unit="MPa")
                        ]
                    )
                ]
            )
        )
    ),
    order=Order(
        id="id8",
        id_short="Order",
        description="Order information",
        order_type="Production",
        quantity="1000",
        time_of_order="2023-04-05T12:00:00",
        required_processes=RequiredProcesses(
            id_short="RequiredProcesses",
            description="Required Processes",
            required_processes=[
                RequiredProcess(name="Assembly", description="Product assembly process"),
                RequiredProcess(name="Testing", description="Quality testing process")
            ]
        )
    ),
    process=Process(
        id="id10",
        id_short="Process",
        description="Process information",
        processType="Manufacturing",
        required_capabilities=RequiredCapabilities(
            id_short="RequiredCapabilities",
            description="Required Capabilities",
            required_capabilities=[
                RequiredCapability(name="Molding", description="Plastic molding capability"),
                RequiredCapability(name="Soldering", description="Electronic soldering capability")
            ]
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
            id_short="Parameters",
            description="Parameters",
            parameters=[
                Parameter(name="Speed", value="100", unit="rpm"),
                Parameter(name="Temperature", value="250", unit="°C")
            ]
        )
    )
)