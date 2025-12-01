Amith’s DevOps Portfolio – Terraform Projects (Beginner → Advanced → CI/CD)

Welcome to my DevOps Portfolio, showcasing some advanced Terraform projects built during hands-on practice.
These projects demonstrate:

1.  Infrastructure as Code (IaC), 
2.  CI/CD, 
3.  Docker automation, 
4.  Virtualization, 
5.  Module development,
6.  multi-environment workflows.

Each project builds on the previous one, forming a complete learning + professional showcase path.

📚 Table of Contents

Project 1 — Terraform Docker Nginx

Project 2 — Terraform Multi-Container (Nginx + Redis)

Project 3 — Terraform VirtualBox VM Automation

Project 4 — Terraform Modules & Reusable Architecture

Project 5 — Terraform Local Web Application Environment

Project 6 — Terraform CI/CD Pipeline using Jenkins + Docker

Skills Demonstrated

Future Enhancements

🟢 Project 1 — Terraform Docker Nginx
⭐ Goal:

Deploy a simple Nginx container using Terraform to learn the basics of providers, resources, and state.

🔧 Tech Stack

Terraform

Docker

nginx:latest

📁 Key Files
main.tf

🚀 What This Project Demonstrates

✔ Installing providers
✔ Creating Docker images & containers via Terraform
✔ Basic provisioning
✔ Terraform init / plan / apply workflow

🟡 Project 2 — Terraform Multi-Container (Nginx + Redis)
⭐ Goal:

Deploy two containers (Nginx + Redis) connected through Docker network using Terraform.

🔧 Tech Stack

Terraform

Docker

Redis DB

Nginx

📁 Key Files
main.tf
outputs.tf
variables.tf

🚀 What This Project Demonstrates

✔ Using multiple resources
✔ Defining variables
✔ Docker networking
✔ Exposing ports
✔ Output values (IP addresses + ports)

🔵 Project 3 — Terraform VirtualBox VM Automation
⭐ Goal:

Automate VirtualBox VM creation using Terraform and local-exec.

🔧 Tech Stack

Terraform

VirtualBox

Bash scripts

VM provisioning automation

📁 Key Files
main.tf
scripts/provision.sh
variables.tf
outputs.tf

🚀 What This Project Demonstrates

✔ Using Terraform with VirtualBox
✔ local-exec provisioner
✔ Automated VM creation
✔ Cloud-init style provisioning
✔ Understanding Infrastructure Automation on local systems

This project upgrades your experience from containers → virtual machines.

🟣 Project 4 — Terraform Modules (Reusable Infrastructure)
⭐ Goal:

Build reusable Terraform modules for VM deployment.

🔧 Tech Stack

Terraform

VirtualBox

Modules

Multi-environment folder structure

📁 Structure
modules/
   vm/
      main.tf
      variables.tf
      outputs.tf

environments/dev/
environments/prod/

🚀 What This Project Demonstrates

✔ Terraform Modules (real professional skill)
✔ DRY (Don’t Repeat Yourself) infrastructure
✔ Reusability for dev / staging / prod
✔ Variable inheritance
✔ Scalable Terraform architecture

This project marks the transition to professional-grade Terraform usage.

🔴 Project 5 — Terraform Local Web Application Environment
⭐ Goal:

Deploy a 3-tier local web environment using Terraform + Docker:

Web server (Nginx)

App server (Python)

Redis DB

🔧 Tech Stack

Terraform

Docker

templatefile() functions

Multi-module design

📁 Structure
main.tf
outputs.tf
modules/web
modules/app
modules/redis
app/index.html
app/app.py

🚀 What This Project Demonstrates

✔ Multi-module Terraform architecture
✔ Templatefile usage
✔ Absolute path volume mounting
✔ Web + App + DB complete topology
✔ Local development environment automation

This project is ideal for interviews to show full-stack infrastructure automation.

🟠 Project 6 — Terraform CI/CD Pipeline (Jenkins + Terraform + Docker)
⭐ Goal:

Create a fully automated CI/CD pipeline that deploys infrastructure using Terraform triggered by Jenkins.

🧩 Pipeline Architecture
GitHub → Jenkins → Terraform → Docker → Running App

🔧 Tech Stack

Jenkins (CI/CD)

Terraform (IaC)

Docker Engine

Docker Compose

GitHub (Version control)

📁 Key Files
docker-compose.yml
terraform/main.tf
app/index.html
Jenkins Pipeline Script

🚀  Project Demonstrates

✔ End-to-end CI/CD automation
✔ Docker + Jenkins + Terraform integration
✔ Jenkins pipeline (Groovy)
✔ GitHub → Jenkins Webhook integration
✔ Real DevOps workflow used in companies

🧠 Skills Demonstrated Across All Projects
🎯 Terraform (Core + Advanced)

Providers

Resources

Variables, Outputs

Modules

Local-exec

Multi-environment IaC

Docker + Terraform integration

VM automation

CI/CD powered Terraform

🎯 DevOps Tools

Docker

Jenkins

VirtualBox

GitHub

Bash scripting

YAML

CI/CD pipelines

🎯 Concepts

Infrastructure as Code

Declarative configuration

Reusable modules

Web application hosting

CI/CD workflow

Local + Remote provisioning






