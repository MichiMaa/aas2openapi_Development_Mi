from typing import List, Optional, Tuple, Literal

from enum import Enum

from aas2openapi.models.base import AAS, Submodel, SubmodelElementCollection
from sdm.models.sdm_reference_model.procedure import Event




class KPIEnum(str, Enum):
    OUTPUT = "output"
    THROUGHPUT = "throughput"
    COST = "cost"
    WIP = "WIP"

    TRHOUGHPUT_TIME = "throughput_time"
    PROCESSING_TIME = "processing_time"

    PRODUCTIVE_TIME = "productive_time"
    STANDBY_TIME = "standby_time"
    SETUP_TIME = "setup_time"
    UNSCHEDULED_DOWNTIME = "unscheduled_downtime"

    DYNAMIC_WIP = "dynamic_WIP"
    DYNAMIC_THROUGHPUT_TIME = "dynamic_throughput_time"


class KPILevelEnum(str, Enum):
    SYSTEM = "system"
    RESOURCE = "resource"
    ALL_MATERIALS = "all_materials"
    MATERIAL_TYPE = "material_type"
    MATERIAL = "material"
    PROCESS = "process"


class KPI(SubmodelElementCollection):
    name: KPIEnum
    target: Literal["min", "max"]
    weight: Optional[float] = 1
    value: Optional[float] = None
    context: Tuple[KPILevelEnum, ...] = None
    resource: Optional[str] = None
    product: Optional[str] = None
    process: Optional[str] = None
    start_time: Optional[float] = None
    end_time: Optional[float] = None


class KeyPerformanceIndicators(Submodel):
    kpis: List[KPI]

class EventLog(Submodel):
    event_log: List[Event]

class Performance(AAS):
    key_performance_indicators: KeyPerformanceIndicators
    event_log: Optional[EventLog]
