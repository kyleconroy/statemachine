# `statemachine`

If you aren't programming with state machines, [you should be](http://www.shopify.com/technology/3383012-why-developers-should-be-force-fed-state-machines).

`statemachine` offers a simple and easy-to-use finite-state machine that can adapted into almost any code base.

## Usage

To create a state machine, mix in the `statemachine.Machine` class. The only requirement is an initial state, which are represented as strings. 

```python
import statemachine

class TrafficLight(statemachine.Machine):
    initial_state = 'red'
```

This machine won't do much, but we can get the current state

```python
>>> stoplight = TrafficLight()
>>> stoplight.state
'red'
```

We can add state transitions using the `event` decorator. These functions must return an iterable of transitions. A transition is just a two-tuple. The first element is an iterable of states (or the wilcard '*') and the second element is the target state.

```python
import statemachine

class TrafficLight(statemachine.Machine):
    initial_state = 'red'

    @statemachine.event
    def cycle(self):
        yield 'red', 'green'
        yield 'green', 'yellow'
        yield 'yellow', 'red'
```

Calling the `cycle` method will transition the machine into the next state.

```python
>>> stoplight = TrafficLight()
>>> stoplight.state
'red'
>>> stoplight.cycle()
>>> stoplight.state
'green'
```

## Installation

    $ pip install statemachine


