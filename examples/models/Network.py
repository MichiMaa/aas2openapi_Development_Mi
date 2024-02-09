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

class Sub_KPI(SubmodelElementCollection):
    Sub_KPI :list
   # Sub_KPI:Optional[KPI]
    #Sub_KPI:Optional[Sub_KPI]


class Network_KPI(KPI):
    KPI_Type: str
    #Sub_KPI:Optional[KPI]
    Sub_KPI:Sub_KPI
    

KPIexample = Network_KPI(
    id_short="finance",
    id = "fin",
    range = 200,
    target = 250,
    actualValue= 150,
    KPI_Type="Monetary",
    Sub_KPI=Sub_KPI(
        id_short="f",
        Sub_KPI = ["rer","gdf"],
    )
    #Sub_KPI.append
    # Sub_KPI=Sub_KPI(
    #     id_short="revenue",
    #     KPI_Type="Monetary",
    #     Sub_KPI=Sub_KPI(
    #         id_short="Income",
    #         KPI_Type="Monetary",
    #     ),
    # Sub_KPI=KPI(
    #     id_short="Loans",
    #     KPI_Type="Monetary",  
    # )

    # )
)
print(KPIexample)
#------------------------------------------------------#

class measurements_in_cm(SubmodelElementCollection):
   measurements_in_cm_list = list()
   #should this have multiple lists for height, width etc ?
   #or list contains the dimensions for one instance, with defined order ?


class Material(SubmodelElementCollection):
    
    name: str
    cost: str

class subComponents(SubmodelElementCollection):
    #check pass and use of this empty class
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
#--------------------------------------------------------#
    
class orderStatus(str,Enum):
    preparing = "preparing"
    in_progress= "in progress"
    finsihed = "finished"
    failed = "failed"
    status:str
    #not used any defined models or list, AASX specified SML


class OrderType(str,Enum):
    
    SupplierOrder = "SupplierOrder"
    CustomerOrder = "CustomerOrder" 
    ProductionOrder = "ProductionOrder"
    TransportOrder = "TransportOrder"
    StoreOrder = "StoreOrder"
    #not used any defined models or list, AASX specified SML

class Network_Order(Order):
    position:str
    orderStatus:orderStatus
    priority:str
    OrderType:OrderType
#----------------------------------------------------------#
class subProcesses(SubmodelElementCollection):
   #check pass and use of this empty class
   pass 


class ProcessStatus(str,Enum):
    preparing = "preparing"
    in_progress= "in progress"
    finsihed = "finished"
    failed = "failed"
    #not used any defined models or list, AASX specified SML


class ProcessType(str,Enum):

    Transport = "Transport"
    Production = "Production"

class Network_Process(Process):
    subProcesses:subProcesses
    process_time:str
    process_cost:str
    ProcessStatus:ProcessStatus
    processType:ProcessType
#------------------------------------------------------#
class subResources(SubmodelElementCollection):
    #check pass and use of this empty class
   pass 

class OrganisationType(str,Enum):
    InternalOrga = "InternalOrga"
    ExternalOrga = "ExternalOrga"

class Organisation(SubmodelElementCollection):
    OrganisationType:OrganisationType
#why use this class with OrganisationType inside and not just one class ?
class ResourceType(str,Enum):
    Network = "Network"
    TransportUnit = "TransportUnit"
    LocationNode = "LocationNode"

class Network_Resource(Resource):
    subResources:subResources
    Organisation:Organisation
    ResourceType:ResourceType
#---------------------------------------------------------#
class subCapabilities(SubmodelElementCollection):
     #check pass and use of this empty class
   pass 

class inherentCapability(str,Enum):
    TransportCapability = "TransportCapability"
    ProductionCapability = "ProductionCapability"

class CapabilityType(SubmodelElementCollection):
    subCapabilities:subCapabilities
    inherentCapability:inherentCapability

class Network_Capability(Capability):
    CapabilityType:CapabilityType
    #why use a seperate class for only one class inside it ?

    
#-------------------------------------------------------#
class Network(AAS):
    KPI: Network_KPI
    Product: Network_Product
    Order: Network_Order
    #Process: Network_Process
    #Resource: Network_Resource
    #Capability: Network_Capability

