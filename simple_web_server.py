import sys
from pathlib import Path
import html

from flask import Flask, request, send_file

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent


@app.get("/")
def home():
    index_path = BASE_DIR / "index.html"
    if not index_path.exists():
        return "index.html not found", 500
    return send_file(index_path, mimetype="text/html")


@app.get("/greet")
def greet_page():
    name = request.args.get("name", "Guest").strip() or "Guest"
    safe_name = html.escape(name, quote=True)
    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Greeting</title>
</head>
<body>
    <h1>Hello, {safe_name}!</h1>
    <a href="/"><button type="button">Go back</button></a>
</body>
</html>
"""
    return page, 200, {"Content-Type": "text/html; charset=utf-8"}


def main():
    app.run(host="0.0.0.0", port=80)


if __name__ == "__main__":
    main()
