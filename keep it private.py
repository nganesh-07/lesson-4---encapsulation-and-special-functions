class myclass:
    __privatevar = 19;

    def __privmethod(self):
        print("I'm inside the class, myclass.")

    def hello(self):
        print("Private variable value:", myclass.__privatevar)


# object creation and method call (to acc print the function):

foo = myclass()
foo.hello()
foo.__privmethod