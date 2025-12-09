\# Local CI/CD Pipeline Simulation



This project demonstrates a full CI/CD workflow using:

\- Python application

\- Automated testing (pytest)

\- Docker build stage

\- Pre-commit hooks (black formatter)

\- GitHub Actions pipeline



\## Run Tests

pytest



\## Build Docker Image

docker build -t ci-demo .



\## Run App

docker run ci-demo
