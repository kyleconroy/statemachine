from nose.tools import assert_true, assert_false
from statemachine import event, Machine, transition_to, transition_from

class MyMachine(Machine):
    initial_state = 'a'

    # these are for asserting things
    became_b = False
    left_b = False

    # when we change the default timing
    # of transition_from/transition_to,
    # we want to ensure that we were
    # triggerd at the right time
    was_a_when_becoming_b = False
    was_c_when_leaving_b = False

    @event
    def advance(self):
        yield 'a', 'b'
        yield 'b', 'c'

    @transition_to('b')
    def becoming_b(self):
        self.became_b = True

    @transition_from('b')
    def leaving_b(self):
        self.left_b = True

    @transition_to('b', 'before')
    def becoming_b_early(self):
        self.was_a_when_becoming_b = self.state == 'a'

    @transition_from('b', 'after')
    def leaving_be_late(self):
        self.was_c_when_leaving_b = self.state == 'c'

def test_transition_to():
    m = MyMachine()
    assert_false(m.became_b)
    assert_false(m.was_a_when_becoming_b)

    m.advance()
    assert_true(m.became_b)
    assert_true(m.was_a_when_becoming_b)

def test_transition_from():
    m = MyMachine()
    assert_false(m.left_b)
    assert_false(m.was_c_when_leaving_b)

    m.advance()
    assert_false(m.left_b)
    assert_false(m.was_c_when_leaving_b)

    m.advance()
    assert_true(m.left_b)
    assert_true(m.was_c_when_leaving_b)

