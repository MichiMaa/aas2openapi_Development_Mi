# layer3.py
from expreiments import *

class SubKPI(SubKPI):
    name: str

class Network(Network):
    pass

# Creating instances
network_instance = Network()
network_instance.kpi = network_instance.KPI()
network_instance.kpi.KPI_Type = "Throughput"
network_instance.kpi.Sub_KPI = SubKPI()
network_instance.kpi.Sub_KPI.name = "Bandwidth Utilization"
network_instance.kpi.Sub_KPI.type = "net"

print(network_instance.kpi.KPI_Type)        
print(network_instance.kpi.Sub_KPI.name)    