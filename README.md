# AWS Lambda Layer Demo

This project demonstrates how to build and invoke AWS Lambda Layers using Python and Node.js, with requirements.txt and package.json files, using the AWS Serverless Application Model (SAM).

## Prerequisites

- AWS CLI
- AWS SAM CLI
- Python 3.8 or later
- Node.js 14.x or later

## Project Structure

```
lambda-layer-demo/
├── .gitignore
├── README.md
├── template.yaml
└── src/
    ├── nodejs/
    │   ├── layer/
    │   │   └── package.json
    │   └── lambda.js
    └── python/
        ├── layer/
        │   └── requirements.txt
        └── lambda.py
```

## Deployment

1. Install the AWS SAM CLI: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html

2. Clone this repository:
   ```
   git clone https://github.com/yourusername/lambda-layer-demo.git
   cd lambda-layer-demo
   ```

3. Build the SAM application:
   ```
   sam build
   ```

4. Deploy the SAM application:
   ```
   sam deploy --guided
   ```

   Follow the prompts to configure your deployment.

## Testing

1. Invoke the Python Lambda function:
   ```
   sam local invoke PythonFunction
   ```

2. Invoke the Node.js Lambda function:
   ```
   sam local invoke NodejsFunction
   ```

3. You should see output similar to:
   ```
   {\"statusCode\": 200, \"body\": \"\\\"Hello from Lambda! Current time: YYYY-MM-DD HH:MM:SS\\\"\"}
   ```

## Cleanup

To delete the SAM application and all associated resources:

```
sam delete
```

## License

This project is licensed under the MIT License.