# Import necessary classes and enums from FinalLayer1.py
from FinalLayer1 import Submodel, SubmodelElementCollection, AAS

# Create instances of basic classes
material_1 = Material(
    id="http://example.com/submodel/material/1",
    id_short="Material1",
    description="Raw material for production",
    name="Steel",
    cost="100 USD/ton"
)

component_1 = Component(
    id="http://example.com/submodel/component/1",
    id_short="Component1",
    description="Main component for product",
    name="Chassis",
    subComponents=SubComponent(
        id="http://example.com/submodel/component/1/subcomponents",
        id_short="SubComponents",
        description="Sub-components for Chassis"
    ),
    cost=500.0,
    transfer_price=800.0,
    measurements_in_cm=[100.0, 50.0, 30.0],
    weight=20.0,
    time_stamp_lastprocess=datetime(2023, 4, 1, 10, 30)
)

# Create instances of enums
order_status = OrderStatus.in_progress
order_type = OrderType.ProductionOrder
process_status = ProcessStatus.preparing
process_type = ProcessType.Production

# Create instances of submodel classes
sub_processes = SubProcesses(
    id="http://example.com/submodel/subprocess",
    id_short="SubProcess",
    description="Sub-processes for production",
    name="Welding and Painting",
    process_time=2.5,
    process_cost=1000.0,
    ProcessStatus=process_status,
    ProcessType=process_type
)

organization_type = OrganizationType(
    id="http://example.com/submodel/organizationtype",
    id_short="OrgType",
    description="Organization Type",
    type="InternalOrga"
)

organization = Organization(
    id="http://example.com/submodel/organization",
    id_short="Organization",
    description="Organization information",
    name="Acme Manufacturing",
    OrganizationType=organization_type
)

sub_resources = SubResources(
    id="http://example.com/submodel/subresources",
    id_short="SubResources",
    description="Sub-Resources information",
    name="Production Sub-Resources"
)

cost = Cost(
    id="http://example.com/submodel/cost",
    id_short="Cost",
    description="Cost information",
    agg_fixedCost=5000.0,
    agg_variableCost=2000.0
)

sub_capabilities = SubCapabilities(
    id="http://example.com/submodel/subcapabilities",
    id_short="SubCapabilities",
    description="Sub-Capabilities information",
    name="Welding and Painting Capabilities"
)

capability_type = CapabilityType(
    id="http://example.com/submodel/capabilitytype",
    id_short="CapabilityType",
    description="Capability Type information",
    subCapabilities=sub_capabilities,
    inherentCapability=InherentCapability.ProductionCapability
)

# Create instances of AAS classes
network_product = Network.Product(
    id="http://example.com/submodel/network/product",
    id_short="NetworkProduct",
    description="Product information for Network",
    name="Automotive Chassis",
    measurements_in_cm=[120.0, 60.0, 40.0],
    Material=material_1,
    Component=component_1,
    cost=1500.0,
    product_generation="Gen 2"
)

network_order = Network.Order(
    id="http://example.com/submodel/network/order",
    id_short="NetworkOrder",
    description="Order information for Network",
    position="A12",
    orderStatus=order_status,
    priority="high",
    OrderType=order_type
)

network_process = Network.Process(
    id="http://example.com/submodel/network/process",
    id_short="NetworkProcess",
    description="Process information for Network",
    subProcesses=sub_processes,
    process_time=5.0,
    process_cost=2500.0,
    ProcessStatus=process_status,
    ProcessType=process_type
)

network_resources = Network.Resources(
    id="http://example.com/submodel/network/resources",
    id_short="NetworkResources",
    description="Resources information for Network",
    subResources=sub_resources,
    Organization=organization,
    ResourceType=ResourceType.Network
)

network_capability = Network.Capability(
    id="http://example.com/submodel/network/capability",
    id_short="NetworkCapability",
    description="Capability information for Network",
    CapabilityType=capability_type
)

location_product = Location.Product(
    id="http://example.com/submodel/location/product",
    id_short="LocationProduct",
    description="Product information for Location",
    name="Automotive Chassis",
    measurements_in_cm=[120.0, 60.0, 40.0],
    Material=material_1,
    Component=component_1,
    cost=1500.0,
    product_generation="Gen 2"
)

location_order = Location.Order(
    id="http://example.com/submodel/location/order",
    id_short="LocationOrder",
    description="Order information for Location",
    orderStatus=order_status,
    priority="high",
    OrderType=order_type
)

location_process = Location.Process(
    id="http://example.com/submodel/location/process",
    id_short="LocationProcess",
    description="Process information for Location",
    subProcesses=sub_processes,
    process_time=5.0,
    process_cost=2500.0,
    ProcessStatus=process_status,
    ProcessType=process_type
)

location_resources = Location.Resources(
    id="http://example.com/submodel/location/resources",
    id_short="LocationResources",
    description="Resources information for Location",
    Organization=organization,
    subResources=sub_resources,
    ResourceType=LocationResourceType.ProductionSite,
    Cost=cost,
    ResStatus=ResStatus.available,
    network_resource_type=ResourceType.LocationNode
)

location_capability = Location.Capability(
    id="http://example.com/submodel/location/capability",
    id_short="LocationCapability",
    description="Capability information for Location",
    CapabilityType=capability_type
)

system_product = System.Product(
    id="http://example.com/submodel/system/product",
    id_short="SystemProduct",
    description="Product information for System",
    name="Automotive Chassis",
    measurements_in_cm=[120.0, 60.0, 40.0],
    Material=material_1,
    Component=component_1,
    cost=1500.0,
    product_generation="Gen 2"
)

system_order = System.Order(
    id="http://example.com/submodel/system/order",
    id_short="SystemOrder",
    description="Order information for System",
    orderStatus=order_status,
    priority="high",
    OrderType=order_type
)

system_process = System.Process(
    id="http://example.com/submodel/system/process",
    id_short="SystemProcess",
    description="Process information for System",
    subProcesses=sub_processes,
    process_time=5.0,
    process_cost=2500.0,
    ProcessStatus=process_status,
    ProcessType=process_type
)

system_resources = System.Resources(
    id="http://example.com/submodel/system/resources",
    id_short="SystemResources",
    description="Resources information for System",
    subResources=sub_resources,
    ResourceType=SystemResourceType.ProductionSystem,
    Cost=cost,
    ResStatus=SystemResStatus.occupied,
    location_resource_type=LocationResourceType.ProductionSite
)

system_capability = System.Capability(
    id="http://example.com/submodel/system/capability",
    id_short="SystemCapability",
    description="Capability information for System",
    CapabilityType=capability_type
)

machine_product = Machine.Product(
    id="http://example.com/submodel/machine/product",
    id_short="MachineProduct",
    description="Product information for Machine",
    name="Automotive Chassis",
    measurements_in_cm=[120.0, 60.0, 40.0],
    Material=material_1,
    Component=component_1,
    cost=1500.0,
    product_generation="Gen 2"
)

machine_order = Machine.Order(
    id="http://example.com/submodel/machine/order",
    id_short="MachineOrder",
    description="Order information for Machine",
    orderStatus=order_status,
    OrderType=order_type
)

machine_process = Machine.Process(
    id="http://example.com/submodel/machine/process",
    id_short="MachineProcess",
    description="Process information for Machine",
    subProcesses=sub_processes,
    process_time=5.0,
    process_cost=2500.0,
    ProcessStatus=process_status,
    ProcessType=process_type
)

machine_resources = Machine.Resources(
    id="http://example.com/submodel/machine/resources",
    id_short="MachineResources",
    description="Resources information for Machine",
    subResources=sub_resources,
    ResourceType=MachineResourceType.Machine,
    Cost=cost,
    ResStatus=SystemResStatus.in_maintenance,
    system_resource_type=SystemResourceType.Machine
)

machine_capability = Machine.Capability(
    id="http://example.com/submodel/machine/capability",
    id_short="MachineCapability",
    description="Capability information for Machine",
    CapabilityType=capability_type
)
