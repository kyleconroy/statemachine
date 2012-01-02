from nose.tools import assert_equals, assert_false, assert_true, raises
from statemachine import Vehicle, TransitionError


def test_initial_state():
    vehicle = Vehicle()
    assert_equals(vehicle.state, "parked")
    assert_equals(vehicle.speed(), 0)
    assert_false(vehicle.is_moving())

def test_state_checkers():
    vehicle = Vehicle()
    assert_true(vehicle.is_parked)

def test_get_state_transitions():
    vehicle = Vehicle()
    print vehicle.ignite.transitions

def test_current_state():
    vehicle = Vehicle()
    print vehicle.state.events()
    print vehicle.state.transitions()

def test_ignite():
    vehicle = Vehicle()
    vehicle.ignite()

    assert_false(vehicle.is_parked)
    assert_true(vehicle.is_idling)
    assert_equals(vehicle.speed(), 10)

def test_shift_up():
    vehicle = Vehicle()
    vehicle.state = "ignite"
    vehicle.shift_up()

    assert_equals(vehicle.speed(), 10)
    assert_true(vehicle.is_moving, 10)

def test_ignite_manurl():
    vehicle = Vehicle()
    assert_true(vehicle.fire_state_event("ignite"))

@raises(TransitionError)
def test_transition_error():
    vehicle = Vehicle()
    vehicle.park()
