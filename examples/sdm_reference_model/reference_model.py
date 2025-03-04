from __future__ import annotations
from typing import Literal, Union, Optional, List

from pydantic import BaseModel

from sdm.models.sdm_reference_model.processes import Process
from sdm.models.sdm_reference_model.procedure import Procedure, TimeModel
from sdm.models.sdm_reference_model.product import Product
from sdm.models.sdm_reference_model.resources import Resource
from sdm.models.sdm_reference_model.order import Order
from sdm.models.sdm_reference_model.change_scenario import ChangeScenario
from sdm.model_core.data_model import DataModel


class ReferenceModel(DataModel):
    def __init__(self, *models: Union[List[BaseModel], BaseModel]):
        super().__init__(*models)

        self.models = {}

    """
    Reference model to describe a production system with products, resources, procedures, processes and orders.
    """

    @classmethod
    def from_dict(cls, dict: dict) -> ReferenceModel:
        """
        Method to load the reference model from a dictionary.

        Args:
            dict (dict): The dictionary to load from.

        Returns:
            ReferenceModel: The loaded reference model.
        """
        models = []
        for key, values in dict.items():
            if key == "product":
                products = [Product(**product_dict) for product_dict in values]
                models += products
            elif key == "resource":
                resources = [Resource(**resource_dict) for resource_dict in values]
                models += resources
            elif key == "procedure":
                procedures = [Procedure(**procedure_dict) for procedure_dict in values]
                models += procedures
            elif key == "process":
                processes = [Process(**process_dict) for process_dict in values]
                models += processes
            elif key == "order":
                orders = [Order(**order_dict) for order_dict in values]
                models += orders
            elif key == "change_scenario":
                change_scenarios = [
                    ChangeScenario(**scenario_dict) for scenario_dict in values
                ]
                models += change_scenarios
        instance = cls(*models)
        instance.models = {
            "product": products,
            "resource": resources,
            "procedure": procedures,
            "process": processes,
            "order": orders,
            "change_scenario": change_scenarios,
        }
        return instance

    @property
    def products(self) -> List[Product]:
        """
        Property to get the products of the reference model.

        Returns:
            List[Product]: The products.
        """
        return self.get_models_of_type(Product)

    @property
    def resources(self) -> List[Resource]:
        """
        Property to get the resources of the reference model.

        Returns:
            List[Resource]: The resources.
        """
        return self.get_models_of_type(Resource)

    @property
    def procedures(self) -> List[Procedure]:
        """
        Property to get the procedures of the reference model.

        Returns:
            List[Procedure]: The procedures.
        """
        return self.get_models_of_type(Procedure)

    @property
    def processes(self) -> List[Process]:
        """
        Property to get the processes of the reference model.

        Returns:
            List[Process]: The processes.
        """
        return self.get_models_of_type(Process)

    @property
    def orders(self) -> List[Order]:
        """
        Property to get the orders of the reference model.

        Returns:
            List[Order]: The orders.
        """
        return self.get_models_of_type(Order)

    @property
    def change_scenario(self) -> List[ChangeScenario]:
        """
        Property to get the change scenarios of the reference model.

        Returns:
            List[ChangeScenario]: The change scenarios.
        """
        return self.get_models_of_type(ChangeScenario)
