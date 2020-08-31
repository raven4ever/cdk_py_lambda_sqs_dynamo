from aws_cdk import (
    core,
    aws_lambda as lmdb,
    aws_apigateway as apigw,
    aws_dynamodb as dynamodb
)
from aws_cdk.core import RemovalPolicy


class CdkPyLambdaSqsDynamoStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # API GW definition
        api = apigw.RestApi(self, 'API-GW')

        # Dynamo DB
        table = dynamodb.Table(self, 'movies',
                               partition_key=dynamodb.Attribute(name='title', type=dynamodb.AttributeType.STRING),
                               table_name='movies_table',
                               removal_policy=RemovalPolicy.DESTROY)

        # Create function
        createFunction = lmdb.Function(self, 'LSD-Create-Function',
                                       runtime=lmdb.Runtime.PYTHON_3_8,
                                       code=lmdb.Code.from_asset('lambda'),
                                       handler='create.handler')

        createIntegration = apigw.LambdaIntegration(createFunction)
        api.root.add_resource('create').add_method('POST', createIntegration)

        # Read function
        readFunction = lmdb.Function(self, 'LSD-Process-Function',
                                           runtime=lmdb.Runtime.PYTHON_3_8,
                                           code=lmdb.Code.from_asset('lambda'),
                                           handler='main.handler')

        readIntegration = apigw.LambdaIntegration(readFunction)
        api.root.add_resource('read').add_method('GET', readIntegration)

        # Table permissions
        table.grant_read_write_data(createFunction)
