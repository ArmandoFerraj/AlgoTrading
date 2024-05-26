STATE_BUY = "BUY"
STATE_SELL = "SELL"

class FSM:
    def __init__(self):
        self.state = STATE_BUY

    def enter_position(self, trading_signal):
        # trading_signal is an element from signals. I dont know what type of oobject it is yet (maybe tuple)
        #it should have all of the information needed to enter a trade ie: ticker, position type, ...?
        #send request to coinbase to enter a position
        self.state = STATE_SELL #switch state

    def exit_position(self):
        #send request to coinbase to exit position
        self.state = STATE_BUY #switch state

    def run(self, signal_list): #pass in signals as the parameter
        if self.state == STATE_BUY:
            if signal_list:
                signal = signal_list.pop(0)# takes first signal from the list (only focused on one trade at a time but maybe we need to add logic to enter multiple trades at once?!)
                print(self.state, "in!")
                self.enter_position(signal) 
            else:
                print(self.state, "money bot got no signals")
        elif self.state == STATE_SELL:
            # this is where our exit strategy logic should be
            print(self.state, "out")
            self.exit_position()
            
    






