'''
Created on Dec 18, 2010

@author: ppa
'''
from BaseModule import BaseModule

class DefaultOutputer(BaseModule):
    ''' Default feeder '''
    def __init__(self):
        ''' constructor '''
        super(DefaultOutputer, self).__init__()

    def execute(self, input):
        ''' do output'''
        super(DefaultOutputer, self).execute(input)
        return None