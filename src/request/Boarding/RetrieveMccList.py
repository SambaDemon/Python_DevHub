from . .Request import Request
from . .Utilities import RemoveFromJson


class RetrieveMccList (Request):

    

    def __init__(self):
        super(RetrieveMccList, self).__init__("boarding", "services", "retrieveMccList", "GET")
        

    