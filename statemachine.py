from functools import wraps


class MetaMachine(type):

    def __new__(cls, name, bases, d):
        d['_state'] = d.get('initial_state')
        return type.__new__(cls, name, bases, d)


class Machine(object):
    __metaclass__ = MetaMachine

    @property
    def state(self):
        return self._state


def after_transition(from_state, to_state):
    def wrapper(f):
        return f
    return wrapper


def before_transition(from_state, to_state):
    def wrapper(f):
        return f
    return wrapper


def around_transition(f):
    return f


def event(f):
    @wraps(f)
    def wrapper(self, *args, **kwargs):
        for current_states, next_state in f(self, *args, **kwargs):
            if self.state in current_states:
                self._start_transition(self.state, next_state)
                self._state = next_state
                self._stop_transition(self.state, next_state)
                return 
    return wrapper


def around_transition(func):
    return func


