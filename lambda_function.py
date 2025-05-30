import json

def lambda_handler(event, context):
    print("Event received:", json.dumps(event))

    try:
        # Handle S3 trigger
        if "Records" in event and event["Records"][0].get("eventSource") == "aws:s3":
            return {
                "statusCode": 200,
                "body": "S3 upload processed."
            }

        # Handle API Gateway event (HTTP)
        return {
            "statusCode": 200,
            "body": json.dumps("API Gateway call successful!")
        }

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps("Internal Server Error: " + str(e))
        }
