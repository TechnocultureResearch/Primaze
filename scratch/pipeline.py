from logging import info, debug
from pipeless import pipeline


error_handler = lambda item, exception: None
function, run, _ = pipeline(error_handler)


@function
def add_one(_):
    return _ + 1


print(list(run([1, 2, 3])))
print(list(run([1, 2, 3, 4])))


@function
def doubler(_):
    yield _, _ * 2


print(list(run([1, 2, 3])))
print(list(run([1, 2, 3, 4])))
