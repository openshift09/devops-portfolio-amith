terraform {
  required_providers {
    docker = {
      source = "kreuzwerker/docker"
    }
  }
}
resource "docker_container" "redis" {
  name  = "${var.name}-redis"
  image = "redis:alpine"
  ports {
    internal = 6379
    external = var.port
  }
}
