"""

"""

class Simulator(object):
    """
    This class simulates forex trading with provied data. You can set directly sell-positions and buy-positions and then
    you get results of simulation after Simulator running. Or, you can set crteria or smoething to set buy or sell postions.
    Simulator can show 1-step results or some provided steps.

    :param str filename: here 
    :param float total_money: here


    Usage::

        >>> import Simulator
        >>> s = Simulator()
        >>> s.setup()
        >>> s.run()
        >>> s.onestep()
        >>> s.reload()

    """
    
    def __init__(self, total_money=None, predictor=None):
        self.total_money = total_money
        self.buy_position = []
        self.sell_position = []
        self.now = 0
        self.predictor = predictor
        self.data = []
        self.idx = 0

    def set_up(self):
        pass

    def onsstep(self):
        _data = self.data[self.idx]
        self.idx += 1
        return _data
    
    def run(self):
        pass

    def set_buy_positions(self, position=[], buy_type=''):
        """
        
        :params list position: set

        :returns :
        """
        pass

    def set_sell_positions(self):
        pass
    
    def read_csv(self, csv, order=''):
        pass

    def write(self):
        pass

    def set_period(self):
        pass

    def set_initial(self, init_money):
        """
        """
        pass

    def steps(self, nstep=1):
        """
        """
        self.idx += nstep
        return self.data[self.idx]

    def load_data(self, data) -> bool:
        if 'CSV' == type(data).__name__:
            self.data = data
            self.data_type = type(data).__name__
            return type(data).__name__
        
    def learn(self):
        pass


