terraform {
  required_providers {
    docker = {
      source = "kreuzwerker/docker"
    }
  }
}
resource "docker_container" "web" {
  name  = "${var.name}-web"
  image = "nginx:latest"

  ports {
    internal = 80
    external = var.port
  }

  volumes {
    container_path = "/usr/share/nginx/html/index.html"
    host_path      = "C:/Users/Amit/Desktop/Int_prep/Terraform_Local_WebApp_Project/modules/web/index.html"
  }
}
