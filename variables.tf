variable "aws_region" {
  description = "AWS region"
  default     = "us-east-2"
}

variable "s3_bucket_name" {
  description = "Name of the S3 bucket"
  type        = string
}
