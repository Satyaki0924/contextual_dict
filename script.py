import os

from functions.grammar import *


class Script(object):
    def __init__(self):
        self.main()

    @staticmethod
    def main():
        try:
            path = os.path.dirname(os.path.abspath(__file__))
            for f in os.listdir(path + '/stdin'):
                search, pos, scrapped = Grammar(path + '/stdin/' + f).grammar()
                with open(path + '/stdout/' + f, 'w') as out:
                    out.write(search + '\n' + str(pos) + '\n' + str(scrapped))
                    out.close()
                    print('File printed at : ' + path + '/stdout/' + f)
        except Exception as exception:
            print(exception)
