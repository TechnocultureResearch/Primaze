""" Commands """


pretty_argspec = lambda a: str(a).strip('[]').replace('\'', '').replace('\"','')


class Command():
    func = None
    args = []
    kwargs = {}
    def __init__(self, func, argspec):
        self.func = func
        self.argspec = argspec
    
    def __repr__(self):
        if self.argspec == ['']:
            return "Command<{}>".format(str(self))
        return "Command<{}({})>".format(str(self), pretty_argspec(self.argspec))
    
    __str__ = lambda self: self.func.__name__
    __call__ = lambda self: self.func(*self.args, *self.kwargs)

    def validate(self, args, kwargs):
        argspec = ','.join(self.argspec)
        # print(args)
        if '*' in argspec:
            print("list expected: {}".format(self))
            if args == []:
                raise ValueError("List of arguments or atleast one argument expected.")
                exit(1)
        print(argspec)
        print(args)
        print(kwargs)
    
    def set_args(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs


class CommandsDeque(list):
    __init__ = lambda self, iterable=[]: list.__init__(self, iterable) # , maxlen=100)
    __contains__ = lambda self, name: any([name == str(c) for c in self])
    def find(self, name):
        for item in self:
            if str(item) == name:
                # print(repr(item))
                return item