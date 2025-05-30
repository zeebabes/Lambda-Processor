import json

def lambda_handler(event, context):
    print("=== FULL EVENT ===")
    print(json.dumps(event))
    print("==================")

    try:
        if "Records" in event:
            return {
                "statusCode": 200,
                "body": "S3 event processed successfully."
            }
        else:
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
