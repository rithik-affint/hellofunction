# main.py
from flask import Request

def hello_http(request: Request):
    data = request.get_json(silent=True) or {}
    name = request.args.get("name") or data.get("name") or "World"
    return f"Hello, {name}!"
