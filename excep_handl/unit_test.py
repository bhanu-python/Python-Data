import cap
import unittest

class Capital(unittest.TestCase):
        def test_one(self):
            text="python"
            result=cap.text_upper_case(text)
            self.assertEqual(result,"Python")

if __name__=='__main__':
    unittest.main()

