import pika
import  models
from database import *

from fastapi import FastAPI,Depends,status ,responses,Response ,routing, APIRouter

import asyncio
from fastapi import APIRouter, Request
from  schema import MessageSchema
import pika_client
from sqlalchemy.orm import Session


router =APIRouter()

models.Base.metadata.create_all(engine)

router = APIRouter(
    tags=['items'],
    responses={404: {"description": "Page not found"}}
)


@router.post('/send-message')
async def send_message(payload: MessageSchema, request: Request, db: Session=Depends(get_db)):
    request.app.pika_client.send_message({"message": payload.message})
    new_topic = models.message(topic=payload.message )
    db.add(new_topic)
    db.commit()
    db.refresh(new_topic)

    return {"status": "ok"}






'''

foo_app = FooApp()
foo_app.include_router(router)


@foo_app.on_event('startup')
async def startup():
    loop = asyncio.get_running_loop()
    task = loop.create_task(foo_app.pika_client.consume(loop))
    await task  



'''




# Ztask/pika_client.py



# @router.get("/he")
# def fuc():
#     message = {'message':"New video Uploaded"}
#     obj = PikaClient()
#     obj.publish(payload=message)
#     return {'message':"hello Sajal"}

