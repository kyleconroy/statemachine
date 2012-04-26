# Head of State

Simple finite state machines for Python

## Lead by Example

```python
from statemachine import event, Machine

class TrafficLight(Machine):
    initial_state = 'stop'

    @event
    def cycle(self):
        yield 'stop', 'proceed'
        yield 'proceed', 'caution'
        yield 'caution', 'stop'

light = TrafficLight()
light.cycle()
```
