from unittest import TestCase

from vessel.vessel import Vessel



class TestVessel(TestCase):

    def test_fire_at(self):
        coordinates= (2,3,6)
        weapon = Weapon(munitions: 30, range:5)
        vessel=Vessel(coordinates, max_hits=40, weapon)
        vessel.fire_at(x:2,y:3,z:4)
        self.assertEqual(29,vessel.munitions)



    