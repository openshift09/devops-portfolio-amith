terraform {
  required_providers {
    docker = {
      source = "kreuzwerker/docker"
    }
  }
}
resource "docker_container" "app" {
  name  = "${var.name}-app"
  image = "python:3.10"

  volumes {
    container_path = "/app/app.py"
    host_path      = "C:/Users/Amit/Desktop/Int_prep/Terraform_Local_WebApp_Project/modules/web/index.html"
  }

  working_dir = "/app"

  command = ["python", "app.py"]

  ports {
    internal = var.app_port
    external = var.app_port
  }
}
