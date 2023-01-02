from pika_client import *
from fastapi import FastAPI,Depends,status ,responses,Response
import asyncio
from router import msg


class FooApp(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pika_client = PikaClient(self.log_incoming_message)
        

    @classmethod
    def log_incoming_message(cls, message: dict):
        """Method to do something meaningful with the incoming message"""
        print(f'Here we got incoming message--- ', message)





foo_app = FooApp()



foo_app.include_router(msg.router)

# @foo_app.on_event('startup')
# def startup():
#     print("This is StartAPp EVEnt")









@foo_app.on_event('startup')
async def startup():
    loop = asyncio.get_running_loop()
    task = loop.create_task(foo_app.pika_client.consume(loop))
    await task