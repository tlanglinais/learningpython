import unittest
from activities import eat, nap


class ActivityTests(unittest.TestCase):
	def test_eat_healthy(self):
		self.assertEqual(eat('broccoli', is_healthy=True), "I'm eating broccoli")

	def test_eat_unhealthy(self):
		self.assertEqual(eat('pizza', is_healthy=False), "I'm eating pizza...")

	def test_short_nap(self):
		self.assertEqual(nap(1), "I'm feeling refreshed")

	def test_long_nap(self):
		self.assertEqual(nap(3), "I overslept!")


if __name__ == '__main__':
	unittest.main()