import unittest
import sys
sys.path.append('../')
from animal import Animal, Dog

def setUpModule():
  print('set up module')

def tearDownModule():
  print('tear down module')

# In the test class' setUpClass() method, create an instance of Animal and Dog (Be sure to pass in a name argument). Write test cases to verify the I/O of the following methods of Animal and Dog.
class TestAnimal(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print('set up class')
        # Be sure to pass in a name argument
        self.animal = Animal("Amy")
        self.dog = Dog("Pup")

    @classmethod
    def tearDownClass(self):
        print('tear down class')

    def test_animal_name(self):
    # Animal object has the correct name property.
        result = self.animal.get_name()
        expected = "Amy"
        self.assertEqual(result, expected)

    def test_animal(self):
    # The animal object is an instance of Animal.
        bird = Animal("bird")
        self.assertIsInstance(bird, Animal)

    def test_dog(self):
    # The dog object is an instance of Dog.
        maci = Dog("Maci")
        self.assertIsInstance(maci, Dog)

    def test_species(self):
    # Set a species and verify that the object property of species has the correct value.
        self.assertEqual(self.dog.get_species(), "Dog")
        self.dog.set_species("Puppers")
        self.assertEqual(self.dog.get_species(), "Puppers")

    def test_walk(self):
    # Invoking the walk() method sets the correct speed on the both objects.
        self.dog.set_legs(4)
        speed = self.dog.speed
        self.dog.walk()
        self.assertEqual(self.dog.speed, speed + (0.2 * self.dog.legs))

        self.animal.set_legs(8)
        speed = self.animal.speed
        self.animal.walk()
        self.assertEqual(self.animal.speed, (speed + (0.1 * self.animal.legs)))


if __name__ == '__main__':
    unittest.main()
