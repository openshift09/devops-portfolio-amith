terraform {
    required_providers {
        local = {
            source = "hashicorp/local"
            version = "2.5.1"
        }
    }
}

provider "local" {}

resource "local_file" "welcome_file" {
    content= "Hello, this file was created by Terraform! Project: ${var.project_name}"
    filename= "${path.module}/output/welcome.txt"
}