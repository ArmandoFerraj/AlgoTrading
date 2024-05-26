import requests
from  StateMachine import FSM

url = 'http://localhost:8000/getmessage/'
signals = []

SIGNALBOT = FSM()
    
def process_messages(message): #classifies each element as a trading signal or not, returns a list of all trading signals
    return message
      
def get_messages(url): #gets response from the server and processes all messages
    response = requests.get(url)
    if response.status_code == 200:
        incoming_message = response.json()
        return process_messages(incoming_message)
    
    elif response.status_code == 204:
        # print("No new messages")
        return None
    else:
        print(f"Failed to fetch messages, status code: {response.status_code}")
        return None

def append_signal(signal_list, new_list):
    if new_list:
            signal_list.extend(new_list)


while True:
    incoming_signals = get_messages(url)
    append_signal(signals, incoming_signals)
    SIGNALBOT.run(signals)




