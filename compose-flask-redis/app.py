import os
import redis
from flask import Flask

app = Flask(__name__)

# "redis" = nom du service Docker Compose (DNS interne)
cache = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=6379,
    password=os.getenv("REDIS_PASSWORD"),
)

@app.route("/")
def index():
    visites = cache.incr("visites")
    return f"<h1>Hello depuis Docker Compose !</h1><p>Cette page a été vue {visites} fois.</p>"

@app.route("/health")
def health():
    cache.ping()
    return "OK"