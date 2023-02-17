from fastapi import FastAPI

import db.queries.reminders as reminders

app = FastAPI(title="Reminderator")


@app.get("/reminders")
async def get_reminders():
    return reminders.get_reminders().to_response()
