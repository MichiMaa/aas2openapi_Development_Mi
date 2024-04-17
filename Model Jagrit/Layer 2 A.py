from Layer_1_Jagrit import *
from datetime import datetime
from typing import Optional

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

class Network(AAS):
    """
    Asset Administration Shell for Network.
    """
    kpi: KPI
    product: Product
    order: Order
    process: Process
    resources: Resources
    capability: Capability

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

class Location(AAS):
    """
    Asset Administration Shell for Location.
    """
    kpi: KPI
    product: Product
    order: Order
    process: Process
    resources: Resources
    capability: Capability

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
        Material: Material = Network.Product.Material
        Component: Component = Network.Product.Component

        @validator('Material', always=True)
        def validate_material(cls, v, values):
            if v is None:
                return Network.Product.Material
            return v

        @validator('Component', always=True)
        def validate_component(cls, v, values):
            if v is None:
                return Network.Product.Component
            return v

class System(AAS):
    """
    Asset Administration Shell for System.
    """
    kpi: KPI
    product: Product
    order: Order
    process: Process
    resources: Resources
    capability: Capability

    class KPI(KPI):
        """
        Submodel for Key Performance Indicators in System.
        """
        KPI_Type: str
        Sub_KPI: SubKPI

    class Product(Network.Product):
        """
        Submodel for Product information in System.
        """
        Material: Material = Network.Product.Material
        Component: Component = Network.Product.Component

        @validator('Material', always=True)
        def validate_material(cls, v, values):
            if v is None:
                return Network.Product.Material
            return v

        @validator('Component', always=True)
        def validate_component(cls, v, values):
            if v is None:
                return Network.Product.Component
            return v

class Machine(AAS):
    """
    Asset Administration Shell for Machine.
    """
    kpi: KPI
    product: Product
    order: Order
    process: Process
    resources: Resources
    capability: Capability

    class KPI(KPI):
        """
        Submodel for Key Performance Indicators in Machine.
        """
        KPI_Type: str
        Sub_KPI: SubKPI

    class Product(Network.Product):
        """
        Submodel for Product information in Machine.
        """
        Material: Material = Network.Product.Material
        Component: Component = Network.Product.Component

        @validator('Material', always=True)
        def validate_material(cls, v, values):
            if v is None:
                return Network.Product.Material
            return v

        @validator('Component', always=True)
        def validate_component(cls, v, values):
            if v is None:
                return Network.Product.Component
            return v
