import unittest
import lib

class TestLib(unittest.TestCase):

	def test_bytes_to_time(self):
		self.assertEqual(lib.bytes_to_time(b'\x82@'), 320)
		self.assertEqual(lib.bytes_to_time(b'\x00'), 0)

	def test_time_to_bytes(self):
		self.assertEqual(lib.time_to_bytes(320), b'\x82@')
		self.assertEqual(lib.time_to_bytes(0), b'\x00')

if __name__ == '__main__':
	unittest.main()