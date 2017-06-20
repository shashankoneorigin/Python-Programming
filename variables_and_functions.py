def print_two(*args):
    arg1, arg2 = args
    print("arg1:%r and arg2:%r" % (arg1, arg2))


def print_two_again(arg1, arg2):
    print("arg1:%r and arg2:%r" % (arg1, arg2))


def print_one(arg1):
    print("arg1:%r" % (arg1))


def print_none():
    print("i have got nothing")


print_two("one", "two")
print_two_again("one_again", "two_again")
print_one("only one")
print_none()
