from __future__ import annotations

from typing import Optional, List, Union, Literal
from pydantic.dataclasses import dataclass

from aas2openapi.models.base import AAS, Submodel, SubmodelElementCollection

from models.Layer1 import Product

class Product_Network(Product):
    testa: str
    testb: str
    


class Network(AAS):
    Product: Product_Network
