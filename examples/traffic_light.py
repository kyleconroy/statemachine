from statemachine import event, Machine
from statemachine import before_transition, after_transition, around_transition


class TrafficLight(Machine):
    initial_state = 'stop'
    count = 0

    @after_transition('stop', 'proceed')
    def chime(self):
        self.count += 1

    @after_transition('*', 'stop')
    def apply_brakes(self):
        self.stopped = True

    @event
    def cycle(self):
        yield 'stop', 'proceed'
        yield 'proceed', 'caution'
        yield 'caution', 'stop'

