STATE_BUY = "BUY"
STATE_SELL = "SELL"

class Statemachine:
    def __init__(self):
        self.state = STATE_BUY

    def enter_position(self, trading_signal):
        # trading_signal is an element from signals. it should have all of the information needed to enter a trade ie: ticker, long/short
        #send request to coinbase to enter a position
        self.state = STATE_SELL #switch state

    def exit_position(self):
        #send request to coinbase to exit position
        self.state = STATE_BUY #switch state

    def run(self, signal_list): #pass in signals as the parameter
        if self.state == STATE_BUY:
            if signal_list:
                signal = signal_list.pop(0)# takes first signal from the list
                self.enter_position(signal) 
                return 
            else:
                print("no signals yet")
        elif self.state == STATE_SELL:
            # this is where our exit strategy logic should be
            self.exit_position()
            
    






