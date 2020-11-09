# from ProjectContext import command
# from collections import deque


# def func(): return True

# # Command()
# def test_command_lambda():
#     lam = lambda: True
#     assert lam() == True

#     c = command.Command(lam)
#     assert str(c) == '<lambda>'
#     assert c.func() == lam()
#     assert c() == lam()
#     assert repr(c) == 'Command<{}>'.format(c)

#     # print(repr(c))


# def test_command_function():
#     assert func() == True

#     c = command.Command(func)
#     assert c.func() == func()
#     assert repr(c) == 'Command<{}>'.format(c)
#     assert str(c) == 'func'
#     assert c() == func()

#     # print(repr(c))


# # CommandDeque
# def test_commands_deque():
#     c = command.CommandsDeque()
#     for _ in range(100):
#         c.append(command.Command(func))
#     lam = lambda: True
#     c.append(command.Command(lam))
#     assert len(c) == 101
#     assert str(c.pop()) == '<lambda>'
#     assert str(c.pop()) == 'func'


# # def test_available_commands():
# #     # assert type(command.available_commands) == type(deque())
# #     i = len(command.available_commands)
# #     command.available_commands.append(command.Command(func))
# #     assert len(command.available_commands) == i + 1

# #     # print(len(command.available_commands))
# #     # print(i)


# # if __name__=='__main__':
# #     test_command_lambda()
# #     test_command_function()
# #     test_commands_deque()
