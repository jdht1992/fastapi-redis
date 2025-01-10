from abc import ABC, abstractmethod
import json
import redis
from src.config.config import settings


class PubSubInterface(ABC):
    @abstractmethod
    def publish(self, channel: str, data: dict):
        pass

    @abstractmethod
    def consume(self, channel: str):
        pass

class RedisBroker(PubSubInterface):
    """
    Message Broker: A message broker acts as a middleman between systems, 
    handling message delivery between producers and consumers. The broker 
    accepts messages from the sender and then forwards them to the receiver, 
    or it might store them temporarily.
    """

    def __init__(self):
        self.redis_client = redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_DB,
            decode_responses=True 
        )

    def publish(self, channel: str, data: dict):
        """ Publish the message to the channel """
        message = json.dumps(data)
        self.redis_client.publish(channel, message)

    def consume(self, channel: str):
        """ Receives and processes messages from the broker. """
        pubsub = self.redis_client.pubsub()
        pubsub.subscribe(channel)
        
        for message in pubsub.listen():
            print(f"Consume message: {message}")
            if message and message["type"] == "message":
                print(f"Received Redis Message From Consumer: {message['data']}")

