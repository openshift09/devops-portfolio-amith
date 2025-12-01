Prometheus + Node Exporter Monitoring (DevOps Portfolio Project)

This project sets up a Prometheus monitoring system using Docker Compose.
It collects host-level metrics using Node Exporter and visualizes them in the Prometheus dashboard.

This is a perfect hands-on DevOps project to showcase monitoring, exporters, and containerization skills.

Features

✔ Prometheus running in Docker
✔ Node Exporter for system metrics
✔ Custom Prometheus configuration
✔ Port exposure for UI access
✔ Clean, beginner–friendly setup
✔ Perfect for DevOps & SRE interviews

Project Structure
Devops-Prometheus/
│── docker-compose.yaml
│── prometheus.yaml
│── README.md
│── images/
      └── prometheus-dashboard.png  (optional)
      └── architecture.png          (optional)

Architecture Diagram
                +------------------------+
                |     Prometheus UI      |
                |   (localhost:9090)     |
                +-----------+------------+
                            |
                            |  Scrapes Metrics
                            |
              +-------------+--------------+
              |        Node Exporter       |
              | (CPU, RAM, Disk Metrics)   |
              +-------------+--------------+
                            |
                            |
                   +--------+-------+
                   |   Local Host   |
                   +----------------+

Technologies Used

Prometheus
Node Exporter
Docker Desktop
Docker Compose
YAML

