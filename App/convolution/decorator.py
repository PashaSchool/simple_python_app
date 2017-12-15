def decorator(f):
    def wapper():
        ptint("before actiona")
        f()
        print("After action")
    return wrapper