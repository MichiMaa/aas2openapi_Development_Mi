
from typing import Literal, Union, Optional, List

from enum import Enum
from pydantic import conlist

from aas2openapi.models.base import AAS, Submodel, SubmodelElementCollection

from sdm.models.sdm_reference_model.distribution import ABSTRACT_INTEGER_DISTRIBUTION, ABSTRACT_REAL_DISTRIBUTION
from sdm.models.sdm_reference_model.performance import KPIEnum

class ChangeDriverInfluence(SubmodelElementCollection):
    is_influenced: bool
    influenecing_change_driver: str # ID of the change driver
    influence_type: str # original bool doesn't make sense here...
    influence_time: float # original bool doesn't make sense here...

    
class ChangeDriver(Submodel):
    distribution_function_over_time_horizon: ABSTRACT_REAL_DISTRIBUTION
    occurrence_distribution_per_unit_of_time: ABSTRACT_INTEGER_DISTRIBUTION # ergibt sich das eine nicht aus dem anderen?
    frequency: float
    change_driver_influences: List[ChangeDriverInfluence]
    influenced_receptor_key_figure_ids: List[str] # List of IDs of the receptor key figures

class ReceptorEnum(str, Enum):
    QUANTITY= "quantity"
    COST= "cost"
    TIME= "time"
    PRODUCT= "product"
    TECHNOLOGY= "technology"
    QUALITY= "quality"

class ModellingEnum(str, Enum):
    DISCRETE = "discrete"
    CONTINUOUS = "continuous"

class DiscreteRKF(SubmodelElementCollection):
    value_for_occurence: str
    value_for_non_occurence: str
    previous_value: str

class ContinuousRKF(SubmodelElementCollection):
    absolute_influences_change_drivers: str # wird hier auf change driver verlinkt? Wenn ja -> _id als suffix anhängen
    relative_influences_change_drivers: str
    slope_influences_change_drivers: str
    previous_slope: float
    previous_value: float

class ReceptorKeyFigure(Submodel):
    receptor_type: ReceptorEnum
    modelling_type: ModellingEnum
    unit: str
    value: Union[DiscreteRKF, ContinuousRKF]


class ReconfigurationConstraints(Submodel):
    """
    The ReconfigurationConstraints represents the constraints for the reconfiguration of the production system.

    Args:
        max_reconfiguration_cost (float): The maximum cost of reconfiguration of the production system.
        max_reconfiguration_time (float): The maximum time of reconfiguration of the production system.
        max_number_of_machines (int): The maximum number of machines of the production system.
        max_number_of_transport_resources (int): The maximum number of transport resources of the production system.
        max_number_of_process_model_per_resource (int): The maximum number of process models per resource of the production system.
    """
    max_reconfiguration_cost: float
    max_reconfiguration_time: float
    max_number_of_machines: int
    max_number_of_transport_resources: int
    max_number_of_process_modules_per_resource: int


class ReconfigurationEnum(str, Enum):
    """
    # from prodsys
    Enum that represents the different levels of reconfigurations that are possible.

    - ProductionCapacity: Reconfiguration of production capacity (number of machines and their configuration)
    - TransportCapacity: Reconfiguration of transport capacity (number of transport resources and their configuration)
    - Layout: Reconfiguration of layout (only position of resources)
    - SequencingLogic: Reconfiguration of sequencing logic (only the control policy of resources)
    - RoutingLogic: Reconfiguration of routing logic (only the routing heuristic of routers)
    """

    FULL = "full"
    PRODUCTION_CAPACITY = "production_capacity"
    TRANSPORT_CAPACITY = "transport_capacity"
    LAYOUT = "layout"
    SEQUENCING_LOGIC = "sequencing_logic"
    ROUTING_LOGIC = "routing_logic"

class ReconfigurationOptions(Submodel):
    """
    The ReconfigurationOptions represents the options for the reconfiguration of the production system.

    Args:
        id (str): The id of the reconfiguration option.
        description (Optional[str]): The description of the reconfiguration option.
        id_short (Optional[str]): The short id of the reconfiguration option.
        sematic_id (Optional[str]): The semantic id of the reconfiguration option.
        reconfiguration_type (ReconfigurationEnum): The type of reconfiguration that is possible.
        machine_controllers (List[Literal["FIFO", "LIFO", "SPT"]]): The machine controllers that are possible.
        transport_controllers (List[Literal["FIFO", "SPT_transport"]]): The transport controllers that are possible.
        routing_heuristics (List[Literal["shortest_queue", "random"]]): The routing heuristics that are possible.
    """
    reconfiguration_type: ReconfigurationEnum
    machine_controllers: List[Literal["FIFO", "LIFO", "SPT"]]
    transport_controllers: List[Literal["FIFO", "SPT_transport"]]
    routing_heuristics: List[Literal["shortest_queue", "random"]]


class Objective(SubmodelElementCollection):
    """
    The Objective represents an objective of the change scenario.

    Args:
        description (Optional[str]): The description of the objective.
        id_short (Optional[str]): The short id of the objective.
        sematic_id (Optional[str]): The semantic id of the objective.
        type (KPIEnum): The type of the objective.
        weight (float): The weight of the objective.
    """
    type: KPIEnum
    weight: float


class ReconfigurationObjectives(Submodel):
    """
    The ReconfigurationObjectives represents the objectives of the change scenario.

    Args:
        id (str): The id of the reconfiguration objectives.
        description (Optional[str]): The description of the reconfiguration objectives.
        id_short (Optional[str]): The short id of the reconfiguration objectives.
        sematic_id (Optional[str]): The semantic id of the reconfiguration objectives.
        objectives (List[Objective]): The objectives of the change scenario.
    """
    objectives: List[Objective]

class ChangeScenario(AAS):
    """
    The ChangeScenario represents a change scenario for the configuration of a production system. It contains the change drivers and the 
    receptor key figures of the change scenario, thus describing how requirements on the production system change over time.

    Moreover, the change scenario holds constraints and options for reconfiguration of the production system, objectives of the change 
    scenario and a list to found solutions. 

    Args:
        id (str): The id of the change scenario.
        description (Optional[str]): The description of the change scenario.
        id_short (Optional[str]): The short id of the change scenario.
    """
    change_drivers: Optional[List[ChangeDriver]]
    receptor_key_figures: Optional[List[ReceptorKeyFigure]]
    base_production_system_id: Optional[str] # link to the base production system
    reconfiguration_constraints: Optional[ReconfigurationConstraints]
    reconfiguration_options: Optional[ReconfigurationOptions]
    reconfiguration_objectives: Optional[ReconfigurationObjectives]
    solution_ids: Optional[List[str]] # List of IDs of the solutions