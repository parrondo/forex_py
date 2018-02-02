import sys
import argparse

class Csv2db(object):
    def __init__(self):
        pass

    def parse_args(self, args):
        paser = argparse.ArgumentParser(description='')
        

def main():
    c = Csv2db()
    c.parse_args(sys.argv[1:])


if __name__ == '__main__':
    main()
        
