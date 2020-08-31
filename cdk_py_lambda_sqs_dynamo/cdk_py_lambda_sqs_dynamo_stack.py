from aws_cdk import (
    core,
    aws_lambda as lmdb,
    aws_apigateway as apigw)


class CdkPyLambdaSqsDynamoStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Lambda function
        lambdaFunction = lmdb.Function(
            self, 'LSD-Function',
            runtime=lmdb.Runtime.PYTHON_3_8,
            code=lmdb.Code.from_asset('lambda'),
            handler='main.handler',
        )

        # API GW
        api = apigw.RestApi(self, 'API-GW')
        apiLambdaIntegration = apigw.LambdaIntegration(lambdaFunction)
        apiLambdaResource = api.root.add_resource('gigel')
        apiLambdaResource.add_method('GET', apiLambdaIntegration)
