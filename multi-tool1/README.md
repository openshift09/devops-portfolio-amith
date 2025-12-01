Int_Prep/
└── Multi-App-DevOps/
    ├── Jenkins-CICD-App/           # Your existing Jenkins project
    ├── k8s/
    │   ├── node-deploy.yaml
    │   ├── python-deploy.yaml
    │   ├── go-deploy.yaml
    │   ├── ingress.yaml
    │   ├── prometheus-deploy.yaml
    │   ├── prometheus-config.yaml
    │   ├── grafana-deploy.yaml
    │   └── grafana-service.yaml
    ├── argocd/
    │   └── application.yaml
    └── ansible/
        ├── playbook.yml
        ├── inventory.ini
        └── roles/
            ├── docker/
            │    └── tasks/main.yml
            └── jenkins/
                 └── tasks/main.yml
