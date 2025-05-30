variable "aws_region" {
  description = "The AWS region to deploy resources in"
  type        = string
  default     = "us-east-1"
}

variable "bucket_name" {
  description = "The name of the S3 bucket used for file uploads"
  type        = string
  default     = "zeebabes-lambda-upload-bucket"  # Change this to something globally unique
}

variable "lambda_function_name" {
  description = "Name of the Lambda function"
  type        = string
  default     = "fileProcessor"
}
