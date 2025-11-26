Project 3 — Terraform + VirtualBox + Cloud-Init (Ubuntu 22.04 Automation)



By: DevOps Engineer Openshift Engineer – Amith



🚀 Overview



This project demonstrates full VM lifecycle automation using Terraform and VirtualBox:



Automatic VM creation



Automatic ISO attachment



Cloud-init autoinstall



NGINX setup



Static IP assignment



Headless startup



Fully repeatable IaC workflow



It shows strong DevOps skills:



Terraform



Virtualization



Provisioning



Cloud-Init



Infrastructure as Code



Automation



🧱 Technology Stack

Tool	Purpose

Terraform	Infrastructure automation

VirtualBox	Local virtualization

Cloud-Init	Automated OS installation

NGINX	Web server installation

Shell Provisioners	Custom configuration

📂 Folder Structure

project-3-virtualbox-ubuntu/

&nbsp;├── cloud\_init/

&nbsp;│    └── user-data

&nbsp;├── iso/

&nbsp;│    └── ubuntu.iso

&nbsp;├── main.tf

&nbsp;├── variables.tf

&nbsp;├── outputs.tf

&nbsp;└── README.md



▶️ How It Works

1\. Terraform executes local-exec → calls VBoxManage

2\. VirtualBox creates a VM

3\. Disk is created

4\. Ubuntu Server ISO is mounted

5\. VM boots headless

6\. Cloud-init autoinstalls Ubuntu

7\. NGINX is installed automatically

8\. VM gets static IP 192.168.56.30

🌐 Test the VM

curl http://192.168.56.30





Expected:



Terraform VirtualBox Automation Successful



🔥 Destroy VM

terraform destroy -auto-approve



📌 Skills Demonstrated



✔ Terraform IaC

✔ VirtualBox automation

✔ Cloud-Init provisioning

✔ SSH automation

✔ NGINX installation

✔ Virtualization networking

✔ Reproducible DevOps workflows



👨‍💻 Author



DevOps Engineer Openshift Engineer – Amith

GitHub: https://github.com/openshift09



Portfolio: devops-portfolio-amith



💡 This project strengthens local IaC skills and demonstrates expertise in provisioning fully automated VMs.

