import unittest

from whiteboard import move as move

class moved(unittest.TestCase):

    def test_move(self):
       result = move('Hello world !')
       expect_result = 'elloHay orldway !'
       self.assertEqual(result, expect_result)

if __name__ == '__main__':
    unittest.main()