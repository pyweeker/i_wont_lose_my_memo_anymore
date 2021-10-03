How do you create an incremental ID in a Python Class

import itertools

class resource_cl():
    newid = itertools.count().next
    def __init__(self):
        self.id = resource_cl.newid()
        
----------------------------

Comparing two dictionaries and checking how many (key, value) pairs are equal

shared_items = {k: x[k] for k in x if k in y and x[k] == y[k]}

----------------------------

Mixin  :  https://dev.to/bikramjeetsingh/write-composable-reusable-python-classes-using-mixins-6lj
