terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.2"
    }
    local = {
      source  = "hashicorp/local"
      version = "~> 2.5.1"
    }
  }
}

provider "docker" {
  host = "tcp://localhost:2375"
}

provider "local" {}

# ----------------------------
# WEB MODULE
# ----------------------------
module "web" {
  source      = "./modules/web"
  name        = "web-server"
  port        = 8080
  environment = "development"
}

# ----------------------------
# APP MODULE
# ----------------------------
module "app" {
  source      = "./modules/app"
  name        = "app-server"
  environment = "development"
  app_port    = 8081
}

# ----------------------------
# REDIS MODULE
# ----------------------------
module "redis" {
  source = "./modules/redis"
  name   = "redis-db"
  port   = 6379
}
