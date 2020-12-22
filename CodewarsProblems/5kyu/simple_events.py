# https://www.codewars.com/kata/52d3b68215be7c2d5300022f/train/python


import unittest


class Event():
    def __init__(self):
        self.handlers = []
    
    def subscribe(self, new_function):
        self.handlers.append(new_function)

    def unsubscribe(self, rm_function):
        self.handlers.remove(rm_function) # cannot use del here since it's a function

    def emit(self, *args):
        for f in self.handlers:
            [f(*args)] # very different from f(a) with a in args --> would have call more times the function f


# test 


class Test(unittest.TestCase):

    def test_event(self):

        event = Event()

        class Testf():
            def __init__(self):
                self.calls = 0
                self.args = []

            def __call__(self, *args):
                self.calls += 1
                self.args += args

        f = Testf()

        event.subscribe(f)

        event.emit(1, 'foo', True)

        self.assertEqual(f.calls, 1)  # calls a handler
        self.assertEqual(f.args, [1, 'foo', True])  # passes arguments

        event.unsubscribe(f)
        event.emit(2)

        self.assertEqual(f.calls, 1)  # no second call

        


if __name__ == "__main__":
    unittest.main()




# clever emit() method :

def emit(self, *args):
    map(lambda f: f(*args), self.handlers)
