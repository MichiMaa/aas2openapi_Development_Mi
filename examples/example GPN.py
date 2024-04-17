import typing
import aas2openapi
from aas2openapi.middleware import Middleware
from aas2openapi import models
from enum import Enum

from models.Network import Network, Product_Network

example_Layer_1 = Layer1(
    id_="test1",
    id_short="test1",
    KPI=KPI(
        id_="test2",
        id_short="test2",
        range=1,
        target=2,
        actualValue=3,
    ),
    Product=Product(
        id_="test3",
        id_short="test3",
        product_group="test",
        BOM=BOM(
            id_="test4",
            id_short="test4",
            components="test",
            subcomponents="test",
            material="test",
        ),
    ),
    Order=Order(
        id_="test5",
        id_short="test5",
        orderType="test",
        quantity=2,
        time_of_order="test",
        required_processes=required_processes(
            id_="test6",
            id_short="test6",
            test="test",
        ),
    ),
    Process=Process(
        id_="test7",
        id_short="test7",
        processType="test",
        required_capabilities=required_capabilities(
            id_="test8",
            id_short="test8",
            test="test",
        ),
    ),
    Resource=Resource(
        id_="test9",
        id_short="test9",
        resourceType="test",
        position="test",
    ),
    Capability=Capability(
        id_="test10",
        id_short="test10",
        capabilityType="test",
        parameters=parameters(
            id_="test11",
            id_short="test11",
            test="test",
        ),
    ),
)

example_network = Network(
    id_="test21",
    id_short="test21",
    Product=Product_Network(
        id_="test20",
        id_short="test20",
        testa="test",
        testb="test",
        product_group="test",
        BOM=BOM(
            id_="test4",
            id_short="test4",
            components="test",
            subcomponents="test",
            material="test",
        )
    )
)

obj_store = aas2openapi.convert_pydantic_model_to_aas(example_network)

import basyx.aas.adapter.json.json_serialization

with open("examples/simple_aas_and_submodels.json", "w", encoding="utf-8") as json_file:
    basyx.aas.adapter.json.write_aas_json_file(json_file, obj_store)


# Reverse transformation

data_model = aas2openapi.convert_object_store_to_pydantic_models(obj_store)

# Create the middleware and load the models
middleware = Middleware()

middleware.load_pydantic_models([Network])
# middleware.load_pydantic_model_instances([example_product, example_process])
# middleware.load_aas_objectstore(obj_store)
# middleware.load_json_models(file_path="examples/example_json_model.json")
middleware.generate_rest_api()
middleware.generate_graphql_api()
middleware.generate_model_registry_api()

app = middleware.app
#run with: uvicorn examples.minimal_example:app --reload
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
