import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="cdk_py_lambda_sqs_dynamo",
    version="0.0.1",

    description="An empty CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="raven4ever",

    package_dir={"": "cdk_py_lambda_sqs_dynamo"},
    packages=setuptools.find_packages(where="cdk_py_lambda_sqs_dynamo"),

    install_requires=[
        "aws-cdk.core",
        "aws-cdk.aws_lambda",
        "aws-cdk.aws_apigateway",
        "aws-cdk.aws_dynamodb"
    ],

    python_requires=">=3.7",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",
    ],
)
