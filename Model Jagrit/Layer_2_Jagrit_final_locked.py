from Layer_1_Jagrit_Locked import *
from datetime import datetime
from typing import Optional
from enum import Enum

class SubKPI(SubmodelElementCollection):
    #Please add elements via editing of sub-ordinate entities
    pass
class measurements_in_cm (SubmodelElementCollection):
    pass
class Material(SubmodelElementCollection):
    name: str
    cost: str

class SubComponent(SubmodelElementCollection):
    #Please add elements via editing of sub-ordinate entities
    pass

class Component(SubmodelElementCollection):
    name: str
    subComponents: SubComponent
    cost: float
    transfer_price: float
    measurements_in_cm: list[measurements_in_cm]
    weight: float
    time_stamp_lastprocess: datetime

class OrderStatus(str, Enum):
    preparing = "preparing"
    in_progress = "in_progress"
    finished = "finished"
    failed = "failed"

class OrderType(str, Enum):
    SupplierOrder = "SupplierOrder"
    CustomerOrder = "CustomerOrder"
    ProductionOrder = "ProductionOrder"
    TransportOrder = "TransportOrder"
    StoreOrder = "StoreOrder"

class ProcessStatus(str, Enum):
    preparing = "preparing"
    in_progress = "in_progress"
    finished = "finished"
    failed = "failed"
    ready = "ready"

class ProcessType(str, Enum):
    Transport = "Transport"
    Production = "Production"
    Store = "Store"
    Reconfiguration = "Reconfiguration"

class SubProcesses(SubmodelElementCollection):
  """
  If properties needs to be added in Layer 2 itself
  Nest class 'Process' or Add properties explicitly like such : 
    name: str
    description: str
    process_time: float
    process_cost: float
    ProcessStatus: ProcessStatus
    ProcessType: ProcessType 
 """
  pass 

class OrganizationType(str, Enum):
    InternalOrga = "InternalOrga"
    ExternalOrga = "ExternalOrga"

class Organization(SubmodelElementCollection):
    OrganizationType: OrganizationType

class SubResources(SubmodelElementCollection):
#Please add elements via editing of sub-ordinate entities
    pass

class NetworkResourceType(str, Enum):
    Network = "Network"
    TransportUnit = "TransportUnit"
    LocationNode = "LocationNode"

class LocationResourceType(str, Enum):
    Customer = "Customer"
    Supplier = "Supplier"
    Warehouse = "Warehouse"
    Distributor = "Distributor"
    Retailer = "Retailer"
    ProductionSite = "ProductionSite"
    StorageUnit = "StorageUnit"
    TransportUnit = "TransportUnit"
    TransportUnitInternal = "TransportUnit (INTERNAL)"
    ProductionSystem = "ProductionSystem"

class Cost(SubmodelElementCollection):
    agg_fixedCost: float
    agg_variableCost: float

class ResStatus(str, Enum):
    available = "available"
    not_available = "not_available"

class SystemResourceType(str, Enum):
    StorageUnit = "StorageUnit"
    TransportUnitInternal = "TransportUnit (INTERNAL)"
    ProductionSystem = "ProductionSystem"
    Machine = "Machine"
    Worker = "Worker"

class SystemResStatus(str, Enum):
    available = "available"
    occupied = "occupied"
    overload = "overload"
    in_maintenance = "in_maintenance"
    error = "error"

class MachineResourceType(str, Enum):
    Machine = "Machine"
    Worker = "Worker"

class InherentCapability(str, Enum):
    TransportCapability = "TransportCapability"
    ProductionCapability = "ProductionCapability"
    StoreCapability = "StoreCapability"

class SubCapabilities(SubmodelElementCollection):
    #Please add elements via editing of sub-ordinate entities
    pass

class CapabilityType(SubmodelElementCollection):
    subCapabilities: SubCapabilities
    inherentCapability: InherentCapability


class Network(AAS):
    class KPI(KPI):
        KPI_Type: str
        Sub_KPI: SubKPI

    class Product(Product):
        name: str
        measurements_in_cm: list[measurements_in_cm]
        Material: Material
        Component: Component
        cost: float
        product_generation: str

    class Order(Order):
        position: str
        orderStatus: OrderStatus
        priority: str
        OrderType: OrderType

    class Process(Process):
        subProcesses: SubProcesses
        process_time: float
        process_cost: float
        ProcessStatus: ProcessStatus
        ProcessType: ProcessType

    class Resources(Resources):
        subResources: SubResources
        Organization: Organization
        ResourceType: NetworkResourceType

    class Capability(Capability):
        CapabilityType: CapabilityType
    
    kpi: KPI
    product: Product
    order: Order
    process: Process
    resources: Resources
    capability: Capability

class Location(AAS):
    class KPI(KPI):
        #or KPI(Network.KPI)
        KPI_Type: str
        Sub_KPI: SubKPI

    class Product(Network.Product):
        default_material: Material = None
        default_component: Component = None

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.default_material = self.Material or Network.Product(*args, **kwargs).Material
            self.default_component = self.Component or Network.Product(*args, **kwargs).Component

        @validator('Material', always=True)
        def validate_material(cls, v, values):
            if v is None:
                return values['default_material']
            return v

        @validator('Component', always=True)
        def validate_component(cls, v, values):
            if v is None:
                return values['default_component']
            return v

    class Order(Order):
        orderStatus: OrderStatus
        priority: str
        OrderType: OrderType

    class Process(Process):
        subProcesses: SubProcesses
        process_time: float
        process_cost: float
        ProcessStatus: ProcessStatus
        ProcessType: ProcessType

    class Resources(Resources):
        Organization: Organization
        subResources: SubResources
        ResourceType: LocationResourceType
        Cost: Cost
        ResStatus: ResStatus
        network_resource_type: NetworkResourceType

    class Capability(Capability):
        CapabilityType: CapabilityType
    kpi: KPI
    product: Product
    order: Order
    process: Process
    resources: Resources
    capability: Capability

class System(AAS):
    class KPI(KPI):
        KPI_Type: str
        Sub_KPI: SubKPI

    class Product(Location.Product):
        pass

    class Order(Order):
        orderStatus: OrderStatus
        priority: str
        OrderType: OrderType

    class Process(Process):
        subProcesses: SubProcesses
        process_time: float
        process_cost: float
        ProcessStatus: ProcessStatus
        ProcessType: ProcessType

    class Resources(Resources):
        subResources: SubResources
        ResourceType: SystemResourceType
        Cost: Cost
        ResStatus: SystemResStatus
        location_resource_type: LocationResourceType

    class Capability(Capability):
        CapabilityType: CapabilityType
    kpi: KPI
    product: Product
    order: Order
    process: Process
    resources: Resources
    capability: Capability

class Machine(AAS):
    class KPI(KPI):
        KPI_Type: str
        Sub_KPI: SubKPI

    class Product(Location.Product):
        pass

    class Order(Order):
        orderStatus: OrderStatus
        OrderType: OrderType

    class Process(Process):
        subProcesses: SubProcesses
        process_time: float
        process_cost: float
        ProcessStatus: ProcessStatus
        ProcessType: ProcessType

    class Resources(Resources):
        subResources: SubResources
        ResourceType: MachineResourceType
        Cost: Cost
        ResStatus: SystemResStatus
        system_resource_type: SystemResourceType

    class Capability(Capability):
        CapabilityType: CapabilityType
    kpi: KPI
    product: Product
    order: Order
    process: Process
    resources: Resources
    capability: Capability