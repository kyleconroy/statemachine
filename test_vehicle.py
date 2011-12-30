from nose.tools import assert_equals, assert_false, assert_true
from statemachine import Vehicle, TransitionError

# Refactor these tests
vehicle = Vehicle()

assert_equals(vehicle.state, "parked")

assert_true(vehicle.is_parked)

print vehicle.ignite.transitions

print vehicle.state.events()
print vehicle.state.transitions()

assert_equals(vehicle.speed, 0)
assert_false(vehicle.is_moving)

vehicle.ignite()

assert_false(vehicle.is_parked)
assert_true(vehicle.is_idling)
assert_equals(vehicle.speed, 10)

vehicle.shift_up()

assert_equals(vehicle.speed, 10)
assert_true(vehicle.is_moving, 10)

# A generic event helper is available to fire without going 
# through the event's instance method
assert_true(vehicle.fire_state_event("shift_up"))

# Call state-driven behavior that's undefined for the state raises a NoMethodError
# TODO vehicle.speed

# The bang (!) operator can raise exceptions if the event fails
try:
    vehicle.park()
except TransitionError:
    pass

# Namespaced machines have uniquely-generated methods
# Not sure how inner things should work
# vehicle.alarm_state             # => 1
# vehicle.alarm_state_name        # => :active
# 
# vehicle.can_disable_alarm?      # => true
# vehicle.disable_alarm           # => true
# vehicle.alarm_state             # => 0
# vehicle.alarm_state_name        # => :off
# vehicle.can_enable_alarm?       # => true
# 
# vehicle.alarm_off?              # => true
# vehicle.alarm_active?           # => false
# 

# Events can be fired in parallel
vehicle.fire_events("shift_down", "enable_alarm") # => true

assert_equals(vehicle.state, "first_gear")
#assert_equals(vehicle.alarm.state, "active") 

# Available transition paths can be analyzed for an object
#print vehicle.state_paths()

# vehicle.state_paths().to_states
# vehicle.state_paths.events

# Find all paths that start and end on certain states
#print vehicle.state_paths(start="parked", end="first_gear")
