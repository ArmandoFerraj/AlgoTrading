import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

message_list = []

app = FastAPI()

class DiscordData(BaseModel):
    message: list[str] #Tuple[str, str]

@app.post("/postmessage/")
async def from_discord(data: DiscordData):
    message_list.append(data.message)
    print('Discord',message_list)
    return message_list

@app.get("/getmessage/")
async def to_signalbot():
    global message_list
    current_message = message_list 
    message_list = [] #empty message list after each GET request
    return current_message#{"message":current_message}


def start_server():
    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    start_server()
 