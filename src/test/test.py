import unittest
from os.path import abspath
import sys
sys.path.append('../')
import main.app

class test(unittest.TestCase):

    """
    Tests that an instance of History is created when launching the app.
    """
    # <!> Requires that ci.ini is completed. <!>
    #def test_main(self):
    #    main.app.main()
    #    self.assertFalse(main.app.history == None)
        

if __name__ == '__main__':
    unittest.main()
