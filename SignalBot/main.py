import helper
from  StateMachine import FSM

url = 'http://localhost:8000/getmessage/'
signals = []
SIGNALBOT = FSM()

while True:
    incoming_signals = helper.get_messages(url)
    helper.append_signal(signals, incoming_signals)
    print(f"These are all of our trading signals{signals}")
    SIGNALBOT.run(signals)



