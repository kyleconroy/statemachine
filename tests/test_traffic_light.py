from nose.tools import assert_equals, assert_true, assert_false
from examples.traffic_light import TrafficLight


def test_traffic_light_cycle():
    light = TrafficLight()
    light.cycle()
    assert_equals('proceed', light.state)
    light.cycle()
    assert_equals('caution', light.state)
    light.cycle()
    assert_equals('stop', light.state)


def test_traffic_light_cycle():
    light = TrafficLight()
    light.cycle()
    assert_equals(1, light.count)


def test_traffic_light_initial():
    light = TrafficLight()
    assert_equals('stop', light.state)
