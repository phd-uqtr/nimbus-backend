import redis
import json

r = redis.Redis(host="localhost", port=6379, decode_responses=True)


def publish_event(channel: str, message: dict):
    r.publish(channel, json.dumps(message))
