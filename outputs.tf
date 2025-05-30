output "s3_bucket_name" {
  value = aws_s3_bucket.upload_bucket.id
}

output "lambda_function_name" {
  value = aws_lambda_function.file_processor.function_name
}

output "api_gateway_url" {
  value = "https://${aws_api_gateway_rest_api.api.id}.execute-api.${var.aws_region}.amazonaws.com/prod/process"
}
