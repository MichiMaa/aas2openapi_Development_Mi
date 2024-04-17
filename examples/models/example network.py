import typing
import aas2openapi
from aas2openapi.middleware import Middleware
from aas2openapi import models
from enum import Enum

from Layer1 import Layer1, KPI,Product, BOM, Order, Process, Resource, Capability
from Network import Network_KPI,Sub_KPI,measurements,  Network_Product, Network_Order, Network_Process,Network_Resource,Network_Capability

example_Network_KPI =Network_KPI(
        id="test2",
        id_short="test2",
        range=1,
        target=2,
        actualValue=3,   
        KPI_Type="ds",
        Sub_KPIs=[Sub_KPI(id_short="1",test1="test",test2="test2"),Sub_KPI(id_short="2", test1="test2",test2="test3",)],
        
    ),
    

print(example_Network_KPI)

example_Network_Product = Network_Product (
    id_short="test3",
    id="test3",
    product_group="test3",
    BOM=BOM(
        id_="test4",
        id_short="test4",
        components="test",
        subcomponents="test",
        material="test",
    name="test3",
    measurements_in_cm = Network_Product.measurements_in_cm(
        measurements_in_cm=[measurements(id_short="test5",measurement1 = [2],measurement2 = [2],measurement3 = [2])],

    )
    Material: Material,
    Component: Component,
    cost: str,
    product_generation: str

)