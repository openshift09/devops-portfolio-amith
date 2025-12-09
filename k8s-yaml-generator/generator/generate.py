import yaml


# Load template
def load_template(path):
    with open(path, "r") as f:
        return f.read()


# Replace placeholders
def render(template, values):
    for key, val in values.items():
        template = template.replace("{{" + key + "}}", str(val))
    return template


values = {
    "app_name": "demo-app",
    "replicas": 2,
    "image": "nginx:latest",
    "port": 80,
}

# Generate Deployment
template = load_template("generator/deployment_template.yaml")
rendered = render(template, values)
with open("examples/output/deployment.yaml", "w") as f:
    f.write(rendered)

# Generate Service
template = load_template("generator/service_template.yaml")
rendered = render(template, values)
with open("examples/output/service.yaml", "w") as f:
    f.write(rendered)

print("YAML files generated successfully!")
