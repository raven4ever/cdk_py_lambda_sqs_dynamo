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
                               removal_policy=RemovalPolicy.DESTROY,
                               billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST)

        # Create function
        createFunction = lmdb.Function(self, 'LSD-Create-Function',
                                       function_name='LSD-Create-Function',
                                       runtime=lmdb.Runtime.PYTHON_3_8,
                                       code=lmdb.Code.from_asset(path='lambda/create_function'),
                                       handler='create.handler')

        createIntegration = apigw.LambdaIntegration(createFunction)
        api.root.add_resource('create').add_method('POST', createIntegration)

        # Report function
        reportFunction = lmdb.Function(self, 'LSD-Report-Function',
                                       function_name='LSD-Report-Function',
                                       runtime=lmdb.Runtime.PYTHON_3_8,
                                       code=lmdb.Code.from_asset(path='lambda/report_function'),
                                       handler='report.handler')

        reportIntegration = apigw.LambdaIntegration(reportFunction)
        api.root.add_resource('report').add_method('GET', reportIntegration)

        # Table permissions
        table.grant_read_write_data(createFunction)
