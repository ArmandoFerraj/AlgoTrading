import requests

def process_messages(message: list[str]) -> list[dict]: #classifies each element as a trading signal or not, returns a list of all trading signals
    """
    - this function will take the list from server.py holding all of the discord messages
    - each element in this list is a string (a message)
    - we want to iterate through all of the elements and classify whether or not they are trading signals
    - if they are a trading signal then we replace that string with a dictionary
    - this dictionary will hold everything we need to know to enter a trade e.g. {ticker:"btc", pos:"long", ...}
    - if they are not a trading signal get rid of the message
    - iterate through all messages and return the list of dictionaries. the length of this should be less than or equal to the original list
    - """
    return message
      
def get_messages(url): #gets response from the server and processes all messages
    response = requests.get(url)
    if response.status_code == 200:
        incoming_message = response.json()
        return process_messages(incoming_message) # incoming_message is a list of strings! will probably be only 1 string in the list unless the chat is getting spammed
    
    elif response.status_code == 204:
        # print("No new messages")
        return None
    else:
        print(f"Failed to fetch messages, status code: {response.status_code}")
        return None

def append_signal(signal_list, new_list):
    if new_list:
            signal_list.extend(new_list)