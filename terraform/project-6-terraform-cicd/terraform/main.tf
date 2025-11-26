terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.2"
    }
  }
}

provider "docker" {}

resource "docker_image" "nginx" {
  name = "nginx:latest"
}

resource "docker_container" "webapp" {
  name  = "jenkins-terraform-app"
  image = docker_image.nginx.latest
  ports {
    internal = 80
    external = 8085
  }

  volumes {
    host_path      = "${path.root}/../app/index.html"
    container_path = "/usr/share/nginx/html/index.html"
  }
}
