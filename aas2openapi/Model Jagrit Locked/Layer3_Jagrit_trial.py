from Layer_2_Jagrit_final_locked import *
from datetime import datetime
from typing import Optional
from enum import Enum
from decimal import Decimal

class ProvidedGood(SubmodelElementCollection):
    component: str
    material: str
    name: str
    cost_per_unit: float
    lead_time: float 
class storedUnit(SubmodelElementCollection):
    Product: str
    Component: str
    subComponent: str
    Material: str

class StoreOrder(SubmodelElementCollection):
    storedUnit: storedUnit
    #correspondingOrder (ref)

class TransportOrder(SubmodelElementCollection):
    destination_position: Decimal
    distance_in_km: float
    #correspondingOrder (ref)

class ProductionOrder(SubmodelElementCollection):
    #correspondingOrder (ref)
    #task (ref)
    pass
class SupplierOrder(SubmodelElementCollection):
    supplier_name: str
    location_of_supplier: Decimal
    ProvidedGood: ProvidedGood   
    contact_info_supplier: str
class CustomerOrder(SubmodelElementCollection):
    customer_name: str
    location_of_customer: Decimal
    #product(ref)
    #task(ref)
    dueDate: datetime
    penaltyCostperdayOverdue: float
    StoreOrder: StoreOrder
    TransportOrder: TransportOrder
    ProductionOrder: ProductionOrder
class ProductionProcess(SubmodelElementCollection):
    #input(ref)
    #task(ref)
    #outpot(ref)
    pass
class TransportProcess(SubmodelElementCollection):
    #transport_from_resource
    #transport_to_resource
    #used_transportMode
    transportUnit_quantity:int

class Network(Network):
    #KPI ?
    #Product : no changes
    class Order(Order):
        SupplierOrder: SupplierOrder
        CustomerOrder: CustomerOrder
    class Process(Process):
        ProductionProcess: ProductionProcess
        TransportProcess: TransportProcess
    class Resources(Resources):
        #...
        pass
        
    
class Location(Location):
    #KPI ?
    #Product : no changes
    pass
class System(System):
    #KPI ?
    #Product : no changes
    pass
class Machine(Machine):
    #KPI ?
    #Product : no changes
    pass
