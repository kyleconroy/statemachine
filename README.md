# `statemachine`

[![Build Status](https://secure.travis-ci.org/tnhu/jsface.png?branch=master)](http://travis-ci.org/tnhu/jsface)

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

We can add state transitions using the `event` decorator. These functions return an iterable of transitions. A transition is just a two-tuple. The first element is an iterable of states, the wilcard '*', or a single state. The second element is the target state.

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

You can listen for transition events using the `before_installation` and `after_installation`  decorators`.

```python
import statemachine

class TrafficLight(statemachine.Machine):
    initial_state = 'red'

    @statemachine.event
    def cycle(self):
        yield 'red', 'green'
        yield 'green', 'yellow'
        yield 'yellow', 'red'

    @statemachine.after_transition('red', 'green')
    def announce(self):
        print "GO GO GO"
```

Initiate the transition by calling `cycle`

```python
>>> stoplight = TrafficLight()
>>> stoplight.cycle()
'GO GO GO'
```

## Installation

    $ pip install statemachine


