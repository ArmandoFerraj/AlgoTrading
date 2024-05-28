from CoinbaseFunctions import initialize_coinbase, get_unit, get_current_holdings, coinbase_buy, coinbase_sell

initialize_coinbase()

STATE_BUY = "BUY"
STATE_SELL = "SELL"

class FSM:
    def __init__(self):
        self.state = STATE_BUY #initialize in the BUY state because we are looking for an entry

    def enter_position(self, trading_signal): 
        """
        - takes in the the trading signal as input. This should be a dictionary {ticker:"DOGE", pos:"short", etc...} 
        - need to parse these values
        - run get_unit()
        - pass the dict values and the unit into coinbase_buy
        - conbase_buy should return something like successful purchase or an error
        - if that return is a succesful purchase then we switch state
        """
        unit = get_unit(initialize_coinbase())
        dummyvar = trading_signal
        coinbase_buy(dummyvar, unit) 
        self.state = STATE_SELL 

    def exit_position(self, trading_signal, signal_list): 
        """
        - takes in the trading signal as input. This should be a dictionary {ticker:"DOGE", pos:"short", etc...} 
        - only need to parse the symbol ie first key of trading_signal
        - run get_current_holdings
        - pass the symbol and holdings into coinbase_sell() to liquidate position
        - if succesful then switch state
        - if not succesful we have a problem and we need to think about how to handle. we do not want to be stuck in an open position indefinitely and we dont want to switch back to buy if it is stil open.
        """
        
        dummyvar = trading_signal
        dummy_symbol = 'BTC'
        holdings = get_current_holdings(initialize_coinbase(), dummy_symbol)
        coinbase_sell(dummyvar, holdings)
        #should return successful or not 
        #if success then delete signal from siganls and switch state
        del signal_list[0]
        self.state = STATE_BUY 

    def run(self, signal_list): #pass in our list of trading signals as the parameter
        if self.state == STATE_BUY:
            if signal_list:
                # signal = signal_list.pop(0) #take the first trading signal out -- i dont think we want to pop this. when we are in the sell state we will still need this signal!
                signal = signal_list[0]
                self.enter_position(signal) 
            else:
                print(self.state)#None #print(self.state, "money bot got no signals")
        elif self.state == STATE_SELL:
            # this is where our exit strategy logic should be
            #if no profit do nothing
            #if too much loss or if we have profit => sell
            signal = signal_list[0]
            self.exit_position(signal, signal_list)
            
    






