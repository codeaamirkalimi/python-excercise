def fullName(*args):
    n = set(args)
    print(n)


fullName("aamir", "Kalimi", "imrank", "anju", "Kalimi")


def okayFunction(**kwargs):
    print(kwargs)
    pass


okayFunction(helo="helo", ko="ko")
