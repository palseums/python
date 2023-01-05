class Test:
    # class attribute
    x = 10

    def __init__(self):
        # Instance attribute
        self.x = 20


test = Test()
print(test.x)  # 20
print(Test.x)  # 10