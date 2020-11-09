""" Commands """
from typing import List, Set, Dict, Tuple, Optional, Callable, Any


pretty_argspec = lambda a: str(a).strip("[]").replace("'", "").replace('"', "")


class Command:
    func: Callable[[Any], Any]
    args: List[str] = []
    kwargs: Dict[str, str] = {}

    def __init__(self, func, argspec):
        self.func = func
        self.argspec = argspec

    def __repr__(self):
        if self.argspec == [""]:
            return "Command<{}>".format(str(self))
        return "Command<{}({})>".format(str(self), pretty_argspec(self.argspec))

    __call__ = lambda self: self.func(*self.args, *self.kwargs)

    def __str__(self):
        return self.func.__name__

    def validate(self, args, kwargs):
        argspec = ",".join(self.argspec)
        # print(argspec)

        if argspec == "":
            return

        if "*" in argspec:
            # print("list expected: {}".format(self))
            if type(args) != type([]):
                raise ValueError("List of arguments expected.")
            if args == []:
                raise ValueError("List with atleast one argument expected.")
                exit(1)
            return  # if args present, kargs not expected
        else:
            if type(kwargs) != type({}):
                raise ValueError("Dictionary of arguments expected.")
            if kwargs == {}:
                raise ValueError("Non Empty Dictionary expected.")
            # Match keyword arguments by name:
            # print(self.kwargs)

            missing_kargs = []
            for karg in self.argspec:
                karg = karg.split("=")[0]
                # print("{} : {}".format(karg, karg in kwargs.keys()))
                if karg not in kwargs.keys():
                    missing_kargs.append(karg)
            # for key in kwargs.keys():
            #     print("{} : {}".format(key, key in self.argspec))

            if missing_kargs:
                raise TypeError(missing_kargs)
            return

        raise NotImplementedError
        # print(argspec)
        # print(args)
        # print(kwargs)

    def set_args(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs


class CommandsDeque(list):
    __init__ = lambda self, iterable=[]: list.__init__(self, iterable)  # , maxlen=100)
    __contains__ = lambda self, name: any([name == str(c) for c in self])

    def find(self, name):
        for item in self:
            if str(item) == name:
                # print(repr(item))
                return item
