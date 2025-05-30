import json

def lambda_handler(event, context):
    print("Event received:", json.dumps(event))

    try:
        if "Records" in event:
            # Handle S3 trigger
            return {
                "statusCode": 200,
                "body": "S3 event processed successfully."
            }
        else:
            # Handle API Gateway trigger
            return {
                "statusCode": 200,
                "body": json.dumps("API Gateway request received.")
            }
    except Exception as e:
        print("Error:", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps("Internal Server Error")
        }
