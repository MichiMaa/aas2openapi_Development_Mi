from __future__ import annotations

from typing import Optional, List, Union, Literal
from pydantic.dataclasses import dataclass

from aas2openapi.models.base import AAS, Submodel, SubmodelElementCollection

   

class KPI(Submodel):
    range: float
    target: float
    actualValue: float

class BOM(SubmodelElementCollection):
    components: str
    subcomponents: str
    material: str

class Product(Submodel):
    product_group:str
    BOM: BOM

class required_processes(SubmodelElementCollection):
    test: Optional[str]

class Order(Submodel):
    orderType: str
    quantity: int
    time_of_order: str
    required_processes: required_processes

class required_capabilities(SubmodelElementCollection):
    test: Optional[str]

class Process(Submodel):
    processType: str
    required_capabilities: required_capabilities

class Resource(Submodel):
    resourceType: str
    position: str

class parameters(SubmodelElementCollection):
    test: str

class Capability(Submodel):
    capabilityType: str
    parameters: parameters

class Layer1(AAS):
    KPI: KPI
    Product: Product
    Order: Order
    Process: Process
    Resource: Resource
    Capability: Capability
