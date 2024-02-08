from __future__ import annotations

from typing import Optional, List, Union, Literal
from pydantic.dataclasses import dataclass

from aas2openapi.models.base import AAS, Submodel, SubmodelElementCollection

   

class KPI(Submodel):
    range: float
    target: float
    actualValue: float

class BOM(SubmodelElementCollection):
    component: str
    subcomponents: Optional[BOM]
    material: str

class Product(Submodel):
    product_group: str
    BOM: BOM

class Order(Submodel):
    orderType: str
    quantity: int
    timeOfOrder: str
    RequiredProcesses: Optional[List[str]]

class Process(Submodel):
    processType: str
    required_capabilities: Optional[List[str]]

class Resource(Submodel):
    resourceType: str
    position: str

class Parameters(SubmodelElementCollection):
    name: str
    value: float

class Capability(Submodel):
    capabilityType: str
    parameters: Optional[parameters]

class Layer1(AAS):
    KPI: KPI
    Product: Product
    Order: Order
    Process: Process
    Resource: Resource
    Capability: Capability
