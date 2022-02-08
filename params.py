import sys

class Params:
    paramlist = []
    
    def __init__(self) -> None:
        self.paramlist = sys.argv

    def get(self,index):
        return self.paramlist[index] if index<len(self.paramlist) else None