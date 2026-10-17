from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps Cloud Status Dashboard</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f1f5f9;
            color: #0f172a;
        }
        header {
            background: #0f172a;
            color: white;
            padding: 28px 20px;
            text-align: center;
        }
        main {
            max-width: 900px;
            margin: 35px auto;
            padding: 0 20px;
        }
        .cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 20px;
        }
        .card {
            background: white;
            padding: 24px;
            border-radius: 12px;
            box-shadow: 0 3px 12px rgba(15, 23, 42, 0.08);
        }
        .status {
            color: #15803d;
            font-weight: bold;
        }
        footer {
            text-align: center;
            color: #64748b;
            padding: 25px;
        }
    </style>
</head>
<body>
    <header>
        <h1>DevOps Cloud Status Dashboard</h1>
        <p>Application and infrastructure overview</p>
    </header>
    <main>
        <h2>System Overview</h2>
        <div class="cards">
            <section class="card">
                <h3>Application</h3>
                <p class="status">● Running</p>
                <p>Python and Flask web application</p>
            </section>
            <section class="card">
                <h3>Containerization</h3>
                <p>Docker</p>
                <p>Container configuration available</p>
            </section>
            <section class="card">
                <h3>Continuous Integration</h3>
                <p>GitHub Actions</p>
                <p>Automated tests and image build</p>
            </section>
            <section class="card">
                <h3>Infrastructure</h3>
                <p>Microsoft Azure</p>
                <p>Infrastructure managed with Terraform</p>
            </section>
        </div>
    </main>
    <footer>DevOps Cloud Project · Learning and development environment</footer>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(DASHBOARD_HTML)


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
