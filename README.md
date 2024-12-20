# AWS Lambda Layer Demo for Python and Node.js

This project demonstrates how to create and use Lambda Layers in both Python and Node.js using the AWS Serverless Application Model (SAM).

## Project Structure

The project has the following structure:

```
.
├── README.md
├── nodejs
│   ├── lambda.js
│   └── layer
│       └── package.json
├── python
│   ├── lambda.py
│   └── layer
│       └── requirements.txt
├── samconfig.toml
└── template.yaml
```

- `nodejs/`: Contains the Node.js Lambda function code and layer configuration.
  - `lambda.js`: The Node.js Lambda function code.
  - `layer/`: Configuration for the Node.js Lambda layer.
    - `package.json`: Specifies the Node.js dependencies for the layer.

- `python/`: Contains the Python Lambda function code and layer configuration.
  - `lambda.py`: The Python Lambda function code.
  - `layer/`: Configuration for the Python Lambda layer.
    - `requirements.txt`: Specifies the Python dependencies for the layer.

- `template.yaml`: The SAM template that defines the AWS resources for the application.

## Prerequisites

Before you begin, ensure you have the following installed:

- AWS CLI - [Install the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)
- SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
- Node.js - [Install Node.js 18](https://nodejs.org/en/), including the npm package management tool.
- Python - [Install Python 3.12](https://www.python.org/downloads/), including the pip package management tool.

## Deployment

To build and deploy your application for the first time, run the following in your shell:

```bash
sam build
sam deploy --guided
```

The `sam build` command will build the source of your application. The `sam deploy --guided` command will package and deploy your application to AWS, with a series of prompts:

- **Stack Name**: The name of the stack to deploy to CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
- **AWS Region**: The AWS region you want to deploy your app to.
- **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
- **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modifies IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
- **Save arguments to samconfig.toml**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.

## Testing

You have 2 options:

First, you can log into the AWS console, navigate to Lambda and run a Test with the following input:
```json
{
  "key1": "value1",
  "key2": "value2",
  "key3": "value3"
}
```

Or, if you have Docker installed locally, you can test locally with the following steps:

1. Invoke the Python Lambda function:
   ```bash
   sam local invoke PythonFunction
   ```

2. Invoke the Node.js Lambda function:
   ```bash
   sam local invoke NodejsFunction
   ```

3. You should see output similar to:
   ```
   {\"statusCode\": 200, \"body\": \"\\\"Hello from Lambda! Current time: YYYY-MM-DD HH:MM:SS\\\"\"}
   ```

## Use the SAM CLI to build and test locally

Build your application with the `sam build` command.

```bash
sam build
```

The SAM CLI installs dependencies defined in `nodejs/layer/package.json` and `python/layer/requirements.txt`, creates a deployment package, and saves it in the `.aws-sam/build` folder.

Test a single function by invoking it directly with a test event. An event is a JSON document that represents the input that the function receives from the event source. Test events are included in the `events` folder in this project.

Run functions locally and invoke them with the `sam local invoke` command.

```bash
sam local invoke PythonFunction
sam local invoke NodejsFunction
```

The SAM CLI can also emulate your application's API. Use the `sam local start-api` to run the API locally on port 3000.

```bash
sam local start-api
curl http://localhost:3000/
```

## Fetch, tail, and filter Lambda function logs

To simplify troubleshooting, SAM CLI has a command called `sam logs`. `sam logs` lets you fetch logs generated by your deployed Lambda function from the command line. In addition to printing the logs on the terminal, this command has several nifty features to help you quickly find the bug.

`NOTE`: This command works for all AWS Lambda functions; not just the ones you deploy using SAM.

```bash
sam logs -n PythonFunction --stack-name {{ stack_name }} --tail
sam logs -n NodejsFunction --stack-name {{ stack_name }} --tail
```

You can find more information and examples about filtering Lambda function logs in the [SAM CLI Documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-logging.html).

## Cleanup

To delete the sample application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```bash
aws cloudformation delete-stack --stack-name {{ project_name }}
```

## Resources

See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.

Next, you can use AWS Serverless Application Repository to deploy ready to use Apps that go beyond hello world samples and learn how authors developed their applications: [AWS Serverless Application Repository main page](https://aws.amazon.com/serverless/serverlessrepo/)