
from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Cloud Computing on Azure</title>
        <style>
            body {
                font-family: Arial;
                background: linear-gradient(120deg, #0078D4, #50E6FF);
                text-align: center;
                padding: 30px;
                color: white;
            }

            h1 {
                font-size: 40px;
            }

            .container {
                display: flex;
                justify-content: center;
                flex-wrap: wrap;
                gap: 20px;
            }

            .card {
                background: white;
                color: #333;
                padding: 25px;
                width: 230px;
                border-radius: 15px;
                box-shadow: 0 4px 10px #555;
            }

            h2 {
                color: #0078D4;
            }
        </style>
    </head>

    <body>

        <h1>☁ Cloud Computing</h1>
        <h3>Deployed Using Microsoft Azure App Service</h3>

        <div class="container">

            <div class="card">
                <h2>IaaS</h2>
                <p>Infrastructure as a Service provides virtual
                machines, storage and networking.</p>
            </div>

            <div class="card">
                <h2>PaaS</h2>
                <p>Platform as a Service provides a platform
                to develop and deploy applications.</p>
            </div>

            <div class="card">
                <h2>SaaS</h2>
                <p>Software as a Service provides software
                through the internet.</p>
            </div>

            <div class="card">
                <h2>Azure Cloud</h2>
                <p>Microsoft Azure provides cloud computing
                services and hosting.</p>
            </div>

            <div class="card">
                <h2>Scalability</h2>
                <p>Increase or decrease computing resources
                based on requirements.</p>
            </div>

            <div class="card">
                <h2>Cloud Storage</h2>
                <p>Store and access data over the internet.</p>
            </div>

        </div>

        <h3>Successfully Running with Python Flask!</h3>
        <p>Hosted on Microsoft Azure App Service</p>

    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
