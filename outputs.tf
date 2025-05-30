output "s3_bucket_name" {
  description = "S3 Bucket name where files will be uploaded"
  value       = aws_s3_bucket.uploads.bucket
}

output "lambda_function_name" {
  description = "The name of the Lambda function"
  value       = aws_lambda_function.file_processor.function_name
}

output "api_gateway_url" {
  description = "The HTTP endpoint for triggering the Lambda function"
  value       = aws_apigatewayv2_api.http_api.api_endpoint
}
