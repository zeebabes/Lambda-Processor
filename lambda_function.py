import json

def lambda_handler(event, context):
    print("Event received:", json.dumps(event))

    # Check if it's an S3 event
    if "Records" in event and event["Records"][0].get("eventSource") == "aws:s3":
        return {
            "statusCode": 200,
            "body": "S3 upload processed."
        }

    # Otherwise, assume API Gateway
    return {
        "statusCode": 200,
        "body": json.dumps("API Gateway call successful!")
    }
