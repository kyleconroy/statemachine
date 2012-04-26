from functools import wraps


class MetaMachine(type):

    def __new__(cls, name, bases, d):
        state = d.get('initial_state')

        if state == None:
            for base in bases:
                try:
                    state = base.initial_state
                    break
                except AttributeError:
                    pass

        before, after = [], []

        for name, method in d.iteritems():
            try:
                after += [(from_, to, method) for from_, to in method.after]
            except AttributeError:
                pass

            try:
                before += [(from_, to, method) for from_, to in method.before]
            except AttributeError:
                pass

        d['_after_transitions'] = after
        d['_before_transitions'] = before
        d['_state'] = state
        return type.__new__(cls, name, bases, d)


class Machine(object):
    __metaclass__ = MetaMachine

    @property
    def state(self):
        return self._state


def after_transition(from_state, to_state):
    def wrapper(f):
        try:
            f.after.append((from_state, to_state))
        except AttributeError:
            f.after = [(from_state, to_state)]
        return f
    return wrapper


def before_transition(from_state, to_state):
    def wrapper(f):
        try:
            f.before.append((from_state, to_state))
        except AttributeError:
            f.before = [(from_state, to_state)]
        return f
    return wrapper


def around_transition(f):
    return f


def is_transition(start, end, current, future):
    return (start in current or start == '*') and (end in future or end == '*')


def event(f):
    @wraps(f)
    def wrapper(self, *args, **kwargs):
        for current, next_state in f(self, *args, **kwargs):
            if self.state in current or '*' in current:

                for start, end, method in self._before_transitions:
                    if is_transition(start, end, current, next_state):
                        method(self, *args, **kwargs)

                self._state = next_state

                for start, end, method in self._after_transitions:
                    if is_transition(start, end, current, next_state):
                        method(self, *args, **kwargs)

                return 
    return wrapper
