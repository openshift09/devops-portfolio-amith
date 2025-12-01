variable "app_name" {
  default = "terraform-webapp"
}

variable "environment" {
  default = "dev"
}

variable "web_port" {
  default = 8080
}

variable "app_port" {
  default = 5000
}

variable "redis_port" {
  default = 6379
}
