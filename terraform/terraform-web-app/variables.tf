variable "region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-east-1"
}

variable "ami" {
  description = "AMI ID for EC2 instance"
  type        = string
  # Amazon Linux 2 (update AMI ID if region changes)
  default     = "ami-0c02fb55956c7d316"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
}

variable "project_name" {
  description = "Name tag for AWS resources"
  type        = string
  default     = "Terraform-Web-App"
}
