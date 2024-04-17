from __future__ import annotations
from datetime import datetime
from typing import Optional, List
from enum import Enum
from decimal import Decimal
from aas2openapi.models.base import AAS, Submodel, SubmodelElementCollection


class BinomialDistribution(SubmodelElementCollection):
    trials: int
    probability: float
class TriangularDistribution(SubmodelElementCollection):
    minimumValue: int
    maximumValue: int
    peakValue: int
    
class DistributionType(str, Enum):
    Normal = "Normal"
    Binomial = "Binomial"
    Triangular = "Triangular"
    
class DistributionFunction(SubmodelElementCollection):
    distributionType: DistributionType
    def __init__(self, distributionType):
        self.distributionType = DistributionType
        if self.distributionType == "Binomial":
            distributionParameters: BinomialDistribution
        elif self.distributionType == "Triangular":
            distributionParameters: TriangularDistribution

class ContinuousReceptorKeyFigure(SubmodelElementCollection):
    absoluteInfluencesChangeDrivers: List[DistributionFunction]
    relativeInfluencesChangeDrivers: List[DistributionFunction]
    slopeInfluencesChangeDrivers: List[DistributionFunction]
    initialSlope: float
    intialValue: float

                                    
class SimulationScenraios(SubmodelElementCollection):
    simulationBaseId: str
    changeDriverScenarios: List[ChangeDriverScenarios]
    receptorKeyFigureScenarios: List[ReceptorKeyFigureScenarios]

class ChangeDriverScenarios(SubmodelElementCollection):
    changeDriverScenariosPerIteration: list

class ReceptorKeyFigureScenarios(SubmodelElementCollection):
    receptorKeyFigureScenariosPerIteration: List[ReceptorKeyFigure.unit]

class DiscreteReceptorKeyFigure(SubmodelElementCollection):
 valueForOccurence: str
 valueForNonOccurence: str
 previousValue: str

class ChangeDriverInfluence(SubmodelElementCollection):
    changeDriverID : str
    typeOfInfluence: bool

class ModellingType(str, Enum):
 discrete = "discrete"
 continuous = "continuous"

class Receptor(str, Enum):
 Quantity = "Quantity"
 Cost = "Cost"
 Time = "Time"
 Product = "Product"
 Technology = "Technology"
 Quality = "Quality"

class ReceptorKeyFigure(SubmodelElementCollection):
    name: str
    receptor: Receptor
    modellingType: ModellingType
    influencingChangeDrivers: List[ChangeDriverInfluence]
    unit: str

class ChangeDriver(Submodel):
    name: str
    distributionFunctionOverTimeHorizon: DistributionFunction
    occurenceDistributionPerUnitOfTime: DistributionFunction
    frequency: int = 1
    influencedChangeDrivers: List[ChangeDriverInfluence] 
    influencedReceptorKeyFigures: List[ReceptorKeyFigure]
    occurenceTime: int

class SimulationBase(AAS):
    timeHorizon: int
    drawingFrequency: int
    timeUnit: str
    confidenceLevel: float
    maxError: float
    consideredChangeDrivers: List[ChangeDriver]
    consideredReceptorKeyFigures: List[ReceptorKeyFigure]
