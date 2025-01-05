import os, requests
import chainlit as cl
from chainlit import Message

API_URL = os.environ.get("API_URL")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")

@cl.set_starters
async def starters():
    return [
        cl.Starter(
            label="Find the most popular post",
            message="Which post is the most popular?",
            icon="public/fire.png",
        ),
        cl.Starter(
            label="Post with the highest engagement",
            message="Which post has the highest engagement?",
            icon="public/rocket.png",
        ),
        cl.Starter(
            label="Post with the lowest engagement",
            message="Which post has the lowest engagement?",
            icon="public/chart.png",
        ),
    ]


@cl.on_message
async def main(message: Message):
    payload = {"input_value": message.content}
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {AUTH_TOKEN}",
    }
    response = requests.post(API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        message = (
            data.get("outputs", [{}])[0]
            .get("outputs", [{}])[0]
            .get("messages", [{}])[0]
            .get("message", "No response")
        )
        await cl.Message(content=message).send()
    else:
        await cl.Message(content="Error communicating with the API").send()
