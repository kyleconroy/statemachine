from nose.tools import assert_equals, assert_true, assert_false
from statemachine import event, Machine, before_transition


class Hunger(Machine):
    initial_state = 'hungry'

    @event
    def eat(self):
        yield 'hungry', 'satisfied'
        yield 'satisfied', 'full'
        yield 'full', 'sick'

    @event
    def rest(self):
        yield ('hungry', 'satisfied', 'full', 'sick'), 'hungry'


class WildHunger(Hunger):

    @event
    def rest(self):
        yield '*', 'hungry'


def test_hunger():
    light = Hunger()
    assert_equals('hungry', light.state)

    light.eat()
    assert_equals('satisfied', light.state)

    light.eat()
    assert_equals('full', light.state)

    light.eat()
    assert_equals('sick', light.state)


def test_wild_hunger():
    light = WildHunger()
    assert_equals('hungry', light.state)

    light.eat()
    assert_equals('satisfied', light.state)

    light.rest()
    assert_equals('hungry', light.state)


