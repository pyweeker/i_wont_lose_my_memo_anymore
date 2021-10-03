How do you create an incremental ID in a Python Class

import itertools

class resource_cl():
    newid = itertools.count().next
    def __init__(self):
        self.id = resource_cl.newid()
        
----------------------------

