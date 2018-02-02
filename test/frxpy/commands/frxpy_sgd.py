import sys
import argparse

class FrxpySGDCommand(object):
    def __init__(self):
        self.model_path = None
        self.optimizer_path = None
        self.train_controller_path = None

        self.model = None
        self.optimizer = None
        self.train_controller = None

    def train(self):
        """
        main loop.
        """
        pass

    def parse_args(self, args):
        parser = argparse.ArgumentParser(description='')

        parser.add_argument('--model', type=str, required=True,
                            help='set your dnn model.')

        parser.add_argument('--optimizer', type=str, required=True,
                            help='set optimizer.')
        
        parser.add_argument('--train_controller', type=str, required=True,
                            help='set train_controller.')

        _args = parser.parse_args(args)

        
        self.model_path = _args.model
        self.optimizer_path = _args.optimizer
        self.train_controller_path = _args.train_controller
        
    def set(self):
        pass


def main():
    fsgd = FrxpySGDCommand()
    fsgd.parse_args(sys.argv[1:])
    fsgd.train()

if __name__ == '__main__':
    main()
        

        
