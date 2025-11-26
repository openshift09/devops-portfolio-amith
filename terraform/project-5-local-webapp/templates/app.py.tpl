from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Flask App Running via Terraform!</h1><p>Environment: ${environment}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=${app_port})
