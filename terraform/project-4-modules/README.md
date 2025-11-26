Terraform Project 4 — Modular VirtualBox VM Automation



By: DevOps Engineer Openshift Engineer – Amith



🚀 Overview



This project demonstrates Terraform Modules, the most important concept for real DevOps and SRE infrastructure.



You will see:



Root module



Reusable child module



Dev, Stage, Prod environments



VirtualBox VM provisioning



Modular folder structure



Clean separation of concerns



🧱 Architecture

project-4-modules/

│

├── modules/

│   └── vm/

│       ├── main.tf

│       ├── variables.tf

│       └── outputs.tf

│

└── environments/

&nbsp;   ├── dev/main.tf

&nbsp;   ├── stage/main.tf

&nbsp;   └── prod/main.tf





Each environment uses the same reusable module to create a VirtualBox VM.



✨ Features

Feature	Description

Modules	Clean, reusable Terraform code

VirtualBox Automation	VM created using VBoxManage

Environment Isolation	Dev, Stage, Prod folders

Scalability	Create multiple VMs using same module

IaC Best Practices	Real industry-style structure

▶️ Usage

1️⃣ Go to an environment

cd environments/dev

terraform init

terraform apply



2️⃣ Destroy VM

terraform destroy



✔ Skills Demonstrated



Terraform modules



Local-exec provisioning



VirtualBox VM automation



IaC structuring



Environment-based infra



Output variables



Reusable infrastructure design



👨‍💻 Author



DevOps Engineer Openshift Engineer – Amith

GitHub: https://github.com/openshift09

