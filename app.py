#!/usr/bin/env python3

from aws_cdk import core

from cdk_py_lambda_sqs_dynamo.cdk_py_lambda_sqs_dynamo_stack import CdkPyLambdaSqsDynamoStack


app = core.App()
CdkPyLambdaSqsDynamoStack(app, "cdk-py-lambda-sqs-dynamo")

app.synth()
