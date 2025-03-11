from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid

app = FastAPI()

# In-memory store for simplicity
db = {}

class FilterState(BaseModel):
    filters: dict
    sort: dict

@app.post("/shorten")
def shorten(state: FilterState):
    state_id = str(uuid.uuid4())[:8]  # Short unique ID
    db[state_id] = state
    return {"short_url": f"https://app.coolcompany.com/users?state={state_id}"}

@app.get("/expand/{state_id}")
def expand(state_id: str):
    state = db.get(state_id)
    if not state:
        raise HTTPException(status_code=404, detail="State not found")
    return state
