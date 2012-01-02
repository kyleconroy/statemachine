class FSM(object):

    def __init__(self, initial=None):
        self.state = "parked"


class TransitionError(Exception):
    pass

def before_transition(start, end):
    def inner_func(func):
        return func
    return inner_func

def state(*args):
    def inner_func(func):
        return func
    return inner_func

def after_transition(start, end):
    def inner_func(func):
        return func
    return inner_func

def event(func):
    return func

def around_transition(func):
    return func


class Vehicle(FSM):


    def __init__(self):
        self.seatbelt_on = False
        self.time_used = 0
        self.auth_shop_busy = False
        self.state = "parked"

    @before_transition("on", "crash")
    def tow(self):
        pass

    @before_transition("on", "repair")
    def fix(self):
        pass

    #@before_transition("parked", state.any - "parked")
    #@after_transition(state.any, "parked")
    def put_on_seatbelt(self):
        self.seatbelt_on = True


    @event
    def park(self):
        yield ("idling", "first_gear"), "parked"

    @event
    def ignite(self):
        yield "stalled", state.same
        yield "parked", "idling"

    @event 
    def idle(self):
        yield "first gear", "idling"

    @event
    def shift_up(self):
        yield "idling", "first gear"
        yield "first gear", "second gear"
        yield "second gear", "third year"

    @event 
    def shift_down(self):
        yield "third gear", "second gear"
        yield "second gear", "first gear"

    @event
    def crash(self):
        if self.passed_inspection:
            yield ("parked", "stalled"), "stalled"
            #yield state.any - ["parked", "stalled"], "stalled"

    @event
    def repair(self):
        if not self.auth_shop_busy:
            yield "stalled", "parked"
        else:
            yield "stalled", state.same

    @state("parked")
    def speed(self):
        return 0

    @state("idling", "first gear")
    def speed(self):
        return 10

    @state("parked", "stalled", "idling")
    def is_moving(self):
        return False

    #@machine("alarm")
    #class Alarm(FSM):
    #    initial = "active"
    #    
    #    @event
    #    def enable(self):
    #        yield state.any, "active"

    #    @event
    #    def disable(self):
    #        yield state.any, "off"

    #    @property
    #    def value(self):
    #        return {
    #            "off": 0,
    #            "active": 1
    #        }

    def passed_inspection(self):
        return False

