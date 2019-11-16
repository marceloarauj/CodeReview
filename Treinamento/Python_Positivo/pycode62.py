import weakref


class WeakList(list):

    def __add__(self, y):
        l = [i() for i in self]
        return list.__add__(l, y)

    def __contains__(self, y):
        ref = weakref.ref(y)
        return list.__contains__(self, ref)

    def __eq__(self, y):
        l = [i() for i in self]
        return list.__eq__(l, y)

    def __repr__(self):
        return "<WeakList at %s>" % id(self)

    def __getitem__(self, i):
        ref = list.__getitem__(self, i)
        return ref()

    def __setitem__(self, i, y):
        ref = weakref.ref(y)
        list.__setitem__(self, i, ref)
    
    def append(self, y):
        list.append(self, weakref.ref(y))

    def count(self, y):
        l = [x() for x in self]
        return list.count(l, y)

    def extend(self, y):
        for o in y:
            list.append(self, weakref.ref(o))

    def index(self, y):
        ref = weakref.ref(y)
        return list.index(self, ref)

    def insert(self, i, y):
        ref = weakref.ref(y)
        list.insert(self, i, ref)        

    def pop(self):
        ref = list.pop(self)
        return ref()

    def remove(self, y):
        ref = weakref.ref(y)
        list.remove(self, ref)

    def sort(self, cmpfunc=None):

        if cmpfunc is None:
            def n_cmpfunc(x, y):
                if x() >  y(): return 1
                if x() == y(): return 0
                if x() <  y(): return -1
            
        else:
            def n_cmpfunc(x, y):
                return cmpfunc(x(), y())

        list.sort(self, n_cmpfunc) 