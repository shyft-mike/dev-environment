import os

import openai
from fastapi import FastAPI

import db.queries.reminders as reminders

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI(title="Real Estate GPT")


@app.get("/reminders")
async def get_reminders():
    return reminders.get_reminders().to_response()


@app.get("/city")
async def get_city_info(city: str):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Tell me information about moving to {city}.",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return response
