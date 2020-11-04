class Command():
    func = None
    def __init__(self, func, *args, **kwargs):
        self.func = func
        # self.args = args
        self.kwargs = kwargs
    __repr__ = lambda self: "Command<{}>".format(str(self))
    __str__ = lambda self: self.func.__name__
    __call__ = lambda self: self.func()
    # is_available = lambda self: self.name in available_commands


class CommandsDeque(list):
    __init__ = lambda self, iterable=[]: list.__init__(self, iterable) # , maxlen=100)
    __contains__ = lambda self, name: any([name == str(c) for c in self])
    def find(self, name):
        for item in self:
            if str(item) == name:
                # print(repr(item))
                return item