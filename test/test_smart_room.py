import unittest
import mock.GPIO as GPIO
from unittest.mock import patch, PropertyMock
from unittest.mock import Mock

from mock.adafruit_bmp280 import Adafruit_BMP280_I2C
from src.smart_room import SmartRoom, SmartRoomError
from mock.senseair_s8 import SenseairS8


class TestSmartRoom(unittest.TestCase):

    @patch.object(GPIO, "input")
    def test_check_person_in_room_infrared_on(self, mock_infrared_sensor: Mock):
        mock_infrared_sensor.return_value = True
        smart_home = SmartRoom()
        self.assertTrue(smart_home.check_room_occupancy())

    @patch.object(GPIO, "input")
    def test_check_person_in_room_infrared_off(self, mock_infrared_sensor: Mock):
        mock_infrared_sensor.return_value = False
        smart_home = SmartRoom()
        self.assertFalse(smart_home.check_room_occupancy())

    @patch.object(GPIO, "input")
    def test_check_enough_light_in_room_photoresistor_on(self, mock_photoresistor: Mock):
        mock_photoresistor.return_value = True
        sr = SmartRoom()
        self.assertTrue(sr.check_enough_light())

    @patch.object(GPIO, "input")
    def test_check_enough_light_in_room_photoresistor_off(self, mock_photoresistor: Mock):
        mock_photoresistor.return_value = False
        sr = SmartRoom()
        self.assertFalse(sr.check_enough_light())




