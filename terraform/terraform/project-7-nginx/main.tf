terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.2"
    }
  }
}

provider "docker" {}

# Build a custom NGINX image
resource "docker_image" "nginx_custom" {
  name = "custom-nginx:latest"

  build {
    context    = "${path.module}"
    dockerfile = "Dockerfile"
  }
}

# Start container with port 8080
resource "docker_container" "nginx_server" {
  name  = "terraform-nginx7"
  image = docker_image.nginx_custom.name

  ports {
    internal = 80
    external = 8080
  }
}

output "nginx_url" {
  value = "http://localhost:8080"
}
