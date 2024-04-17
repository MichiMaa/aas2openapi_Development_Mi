from __future__ import annotations
from enum import Enum
from typing import Optional, List, Union, Literal
from pydantic.dataclasses import dataclass

from aas2openapi.models.base import AAS, Submodel, SubmodelElementCollection

from Layer1 import KPI
from Layer1 import Product
from Layer1 import Order
from Layer1 import Process
from Layer1 import Resource
from Layer1 import Capability


#SM KPI
#Should KPI alaso habve a list ?
#Sub KPI should be changed from SMC to SMCL

class Sub_KPI(SubmodelElementCollection):
    test1: str
    test2: str
class Network_KPI(KPI):
    KPI_Type: str
    Sub_KPIs:list[Sub_KPI]

#SM Process
    
class measurements (SubmodelElementCollection):
   measurement1 = list()
   measurement2 = list()
   measurement3 = list()
class measurements_in_cm(SubmodelElementCollection):
    measurements_in_cm:list[measurements]
   
class Material(SubmodelElementCollection):
    
    name: str
    cost: str

class subComponents(SubmodelElementCollection):
    pass

class Component(SubmodelElementCollection):
    name:str
    subComponent:subComponents
    cost:str
    transfer_price:str
    measurements_in_cm:measurements_in_cm
    weight:str
    time_stamp_lastprocess:str

class Network_Product(Product):
    name: str
    measurements_in_cm: measurements_in_cm
    Material: Material
    Component: Component
    cost: str
    product_generation: str

#SM Order
    
 #SML changed to SMC ?    
class orderStatus(str,Enum):
    preparing = "preparing"
    in_progress= "in progress"
    finsihed = "finished"
    failed = "failed"
    status:str
   

 #SML changed to SMC ? 
class OrderType(str,Enum):
    
    SupplierOrder = "SupplierOrder"
    CustomerOrder = "CustomerOrder" 
    ProductionOrder = "ProductionOrder"
    TransportOrder = "TransportOrder"
    StoreOrder = "StoreOrder"
class Network_Order(Order):
    position:str
    orderStatus:orderStatus
    priority:str
    OrderType:OrderType

#SM Process
    
        
class subProcesses(SubmodelElementCollection):
   pass 
#SML changed to SMC ? 
class ProcessStatus(str,Enum):
    preparing = "preparing"
    in_progress= "in progress"
    finsihed = "finished"
    failed = "failed"
#SML changed to SMC ? 
class ProcessType(str,Enum):

    Transport = "Transport"
    Production = "Production"

class Network_Process(Process):
    subProcesses:subProcesses
    process_time:str
    process_cost:str
    ProcessStatus:ProcessStatus
    processType:ProcessType

#SM Resources
    
class subResources(SubmodelElementCollection):
   pass 

class OrganisationType(str,Enum):
    InternalOrga = "InternalOrga"
    ExternalOrga = "ExternalOrga"

class Organisation(SubmodelElementCollection):
    OrganisationType:OrganisationType
class ResourceType(str,Enum):
    Network = "Network"
    TransportUnit = "TransportUnit"
    LocationNode = "LocationNode"

class Network_Resource(Resource):
    subResources:subResources
    Organisation:Organisation
    ResourceType:ResourceType

#SM Capability

class subCapabilities(SubmodelElementCollection):
   pass 

class inherentCapability(str,Enum):
    TransportCapability = "TransportCapability"
    ProductionCapability = "ProductionCapability"

class CapabilityType(SubmodelElementCollection):
    subCapabilities:subCapabilities
    inherentCapability:list[inherentCapability]

class Network_Capability(Capability):
    CapabilityType:CapabilityType

    
#-------------------------------------------------------#
class Network(AAS):
    KPI: Network_KPI
    Product: Network_Product
    Order: Network_Order
    Process: Network_Process
    Resource: Network_Resource
    Capability: Network_Capability

