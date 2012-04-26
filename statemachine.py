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

        for name, func in d.items():
            try:
                after += [(start, end, func) for start, end in func.after]
            except AttributeError:
                pass

            try:
                before += [(start, end, func) for start, end in func.before]
            except AttributeError:
                pass

        d['_after_transitions'] = after
        d['_before_transitions'] = before
        d['_state'] = state

        return type.__new__(cls, name, bases, d)

# Python 2/3 Metaclass
# http://mikewatkins.ca/2008/11/29/python-2-and-3-metaclasses/
Machine = MetaMachine('Machine', (object, ), {
    'state': property(lambda x: x._state),
    })


def create_transition(attr, from_state, to_state):
    def wrapper(f):
        try:
            getattr(f, attr).append((from_state, to_state))
        except AttributeError:
            setattr(f, attr, [(from_state, to_state)])
        return f
    return wrapper


def after_transition(from_state, to_state):
    return create_transition('after', from_state, to_state)


def before_transition(from_state, to_state):
    return create_transition('before', from_state, to_state)


def around_transition(f):
    return f


def is_transition(start, end, current, future):
    return (start in current or start == '*') and (end in future or end == '*')

def transition_from(from_state, timing='before'):
    """Trigger the decorated function whenever transitioning
    `from` the specified state (to anything else). By default,
    fires before the state transition has taken place, so the
    :attr:`~Machine.state` will be `from_state`.
    """
    return create_transition(timing, from_state, '*')

def transition_to(to_state, timing='after'):
    """Trigger the decorated function whenever transitioning
    `to` the specified state (from anything else). By default,
    fires after the state transition has taken place, so the
    :attr:`~Machine.state` will be `to_state`.
    """
    return create_transition(timing, '*', to_state)

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
