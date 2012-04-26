from nose.tools import assert_equals, assert_true, assert_false
from examples.traffic_light import TrafficLight


def test_traffic_light_cycle():
    light = TrafficLight()
    light.cycle()
    assert_equals('green', light.state)
    light.cycle()
    assert_equals('yellow', light.state)
    light.cycle()
    assert_equals('red', light.state)


def test_traffic_light_cycle():
    light = TrafficLight()
    light.cycle()
    assert_equals(1, light.count)


def test_traffic_light_initial():
    light = TrafficLight()
    assert_equals('red', light.state)
