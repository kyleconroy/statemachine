from __future__ import print_function
import statemachine as fsm

class TrafficLight(fsm.Machine):
    initial_state = 'red'
    count = 0

    @fsm.after_transition('red', 'green')
    def chime(self):
        print('GO GO GO')
        self.count += 1

    @fsm.after_transition('*', 'red')
    def apply_brakes(self):
        self.stopped = True

    @fsm.event
    def cycle(self):
        yield 'red', 'green'
        yield 'green', 'yellow'
        yield 'yellow', 'red'

