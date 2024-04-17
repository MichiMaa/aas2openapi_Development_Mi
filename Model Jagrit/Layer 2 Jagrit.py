from Layer_1_Jagrit import *
from datetime import datetime
from typing import Optional
from enum import Enum

class SubKPI(SubmodelElementCollection):
    """
    Submodel element collection for Sub-KPIs.
    """
    pass

class Material(SubmodelElementCollection):
    """
    Submodel element collection for Materials.
    """
    name: str
    cost: str

class SubComponent(SubmodelElementCollection):
    """
    Submodel element collection for Sub-Components.
    """
    pass

class Component(SubmodelElementCollection):
    """
    Submodel element collection for Components.
    """
    name: str
    subComponents: SubComponent
    cost: float
    transfer_price: float
    measurements_in_cm: List[float]
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
    Submodel element collection for Sub-Processes.
    """
    name: str
    description: str
    process_time: float
    process_cost: float
    ProcessStatus: ProcessStatus
    ProcessType: ProcessType

class OrganizationType(Submodel):
    """
    Submodel for Organization Type.
    """
    type: list["InternalOrga", "ExternalOrga"]

class Organization(SubmodelElementCollection):
    """
    Submodel element collection for Organization.
    """
    name: str
    description: str
    OrganizationType: OrganizationType

class SubResources(SubmodelElementCollection):
    """
    Submodel element collection for Sub-Resources.
    """
    name: str
    description: str

class ResourceType(str, Enum):
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

class Cost(Submodel):
    """
    Submodel for Cost.
    """
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
    """
    Submodel element collection for Sub-Capabilities.
    """
    name: str
    description: str

class CapabilityType(SubmodelElementCollection):
    """
    Submodel element collection for Capability Type.
    """
    subCapabilities: SubCapabilities
    inherentCapability: InherentCapability

class Network(AAS):
    """
    Asset Administration Shell for Network.
    """


    class KPI(KPI):
        """
        Submodel for Key Performance Indicators in Network.
        """
        KPI_Type: str
        Sub_KPI: SubKPI

    class Product(Product):
        """
        Submodel for Product information in Network.
        """
        name: str
        measurements_in_cm: List[float]
        Material: Material
        Component: Component
        cost: float
        product_generation: str

    class Order(Order):
        """
        Submodel for Order information in Network.
        """
        position: str
        orderStatus: OrderStatus
        priority: str
        OrderType: OrderType

    class Process(Process):
        """
        Submodel for Process information in Network.
        """
        subProcesses: SubProcesses
        process_time: float
        process_cost: float
        ProcessStatus: ProcessStatus
        ProcessType: ProcessType

    class Resources(Resources):
        """
        Submodel for Resources in Network.
        """
        subResources: SubResources
        Organization: Organization
        ResourceType: ResourceType

    class Capability(Capability):
        """
        Submodel for Capability in Network.
        """
        CapabilityType: CapabilityType
    
    kpi: KPI
    product: Product
    order: Order
    process: Process
    resources: Resources
    capability: Capability

class Location(AAS):
    """
    Asset Administration Shell for Location.
    """


    class KPI(KPI):
        """
        Submodel for Key Performance Indicators in Location.
        """
        KPI_Type: str
        Sub_KPI: SubKPI

    class Product(Network.Product):
        """
        Submodel for Product information in Location.
        """
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
        """
        Submodel for Order information in Location.
        """
        orderStatus: OrderStatus
        priority: str
        OrderType: OrderType

    class Process(Process):
        """
        Submodel for Process information in Location.
        """
        subProcesses: SubProcesses
        process_time: float
        process_cost: float
        ProcessStatus: ProcessStatus
        ProcessType: ProcessType

    class Resources(Resources):
        """
        Submodel for Resources in Location.
        """
        Organization: Organization
        subResources: SubResources
        ResourceType: LocationResourceType
        Cost: Cost
        ResStatus: ResStatus
        network_resource_type: ResourceType

    class Capability(Capability):
        """
        Submodel for Capability in Location.
        """
        CapabilityType: CapabilityType
    kpi: KPI
    product: Product
    order: Order
    process: Process
    resources: Resources
    capability: Capability

class System(AAS):
    """
    Asset Administration Shell for System.
    """


    class KPI(KPI):
        """
        Submodel for Key Performance Indicators in System.
        """
        KPI_Type: str
        Sub_KPI: SubKPI

    class Product(Location.Product):
        """
        Submodel for Product information in System.
        """
        pass

    class Order(Order):
        """
        Submodel for Order information in System.
        """
        orderStatus: OrderStatus
        priority: str
        OrderType: OrderType

    class Process(Process):
        """
        Submodel for Process information in System.
        """
        subProcesses: SubProcesses
        process_time: float
        process_cost: float
        ProcessStatus: ProcessStatus
        ProcessType: ProcessType

    class Resources(Resources):
        """
        Submodel for Resources in System.
        """
        subResources: SubResources
        ResourceType: SystemResourceType
        Cost: Cost
        ResStatus: SystemResStatus
        location_resource_type: LocationResourceType

    class Capability(Capability):
        """
        Submodel for Capability in System.
        """
        CapabilityType: CapabilityType
    kpi: KPI
    product: Product
    order: Order
    process: Process
    resources: Resources
    capability: Capability

class Machine(AAS):
    """
    Asset Administration Shell for Machine.
    """


    class KPI(KPI):
        """
        Submodel for Key Performance Indicators in Machine.
        """
        KPI_Type: str
        Sub_KPI: SubKPI

    class Product(Location.Product):
        """
        Submodel for Product information in Machine.
        """
        pass

    class Order(Order):
        """
        Submodel for Order information in Machine.
        """
        orderStatus: OrderStatus
        OrderType: OrderType

    class Process(Process):
        """
        Submodel for Process information in Machine.
        """
        subProcesses: SubProcesses
        process_time: float
        process_cost: float
        ProcessStatus: ProcessStatus
        ProcessType: ProcessType

    class Resources(Resources):
        """
        Submodel for Resources in Machine.
        """
        subResources: SubResources
        ResourceType: MachineResourceType
        Cost: Cost
        ResStatus: SystemResStatus
        system_resource_type: SystemResourceType

    class Capability(Capability):
        """
        Submodel for Capability in Machine.
        """
        CapabilityType: CapabilityType
    kpi: KPI
    product: Product
    order: Order
    process: Process
    resources: Resources
    capability: Capability