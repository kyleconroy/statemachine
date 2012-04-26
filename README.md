# `statemachine`

If you aren't programming with state machines, [you should be](http://www.shopify.com/technology/3383012-why-developers-should-be-force-fed-state-machines).

`statemachine` offers a simple and easy-to-use finite-state machine that can adapted into almost any code base.

## Introduction

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

## Installation

    $ pip install statemachine


