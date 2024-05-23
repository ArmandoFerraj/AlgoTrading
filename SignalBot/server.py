import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

message_list = []

app = FastAPI()

class DiscordData(BaseModel):
    message: str #Tuple[str, str]

@app.post("/postmessage/")
async def from_discord(data: DiscordData):
    message_list.append(data.message)
    return message_list

@app.get("/getmessage/")
async def to_signalbot():
    global message_list
    if len(message_list) == 0:
        print('EMPTY NO MESSAGES FROM DISCORD')
        raise HTTPException(status_code=204, detail="No content")
    
    else:
        current_message = message_list  #create this temp list that sends the message 
        message_list = [] #empty message list after each GET request so we dont ever duplicate messages
        return current_message

def start_server():
    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    start_server()
