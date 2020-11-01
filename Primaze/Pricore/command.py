from collections import UserList

class Commands(UserList):
    def __init__(self, lst=[]):
        self.data = lst

    def __contains__(self, obj):
        """Return True if any item in the list has a title, and the title matches that of the passed-in dict"""
        return any(obj['name'] == x['name'] for x in self.data if 'name' in x) or any(obj['func'] == x['func'] for x in self.data if 'func' in x)

# class Commands():
#     available_commands = []
#     __len__ = lambda self: len(self.available_commands)
#     # __repr__ = lambda self: "\n".join(self.available_commands)
#     def append(self, item): self.available_commands.append(item)
#     __contains__ = lambda self, item: self.available_commands.__contains__(item)


available_commands = Commands()

def register(f):
    available_commands.append(Command(f))
    return(f)


class Command():
    def __init__(self, func):
        self.func = func
        self.name = func.__name__
    
    execute = lambda self: self.func()
    is_available = lambda self: self.name in available_commands
    __repr__ = lambda self: "Command<{}>".format(self.name)
    __call__ = lambda self: self.execute()


# print(available_commands)
# print('Command<fetch_genome>' in available_commands)
# print('fetch_genome' in available_commands)
# print(fetch_genome in available_commands)
# print(Command(fetch_genome) == available_commands)