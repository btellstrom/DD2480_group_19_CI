import unittest
from os.path import abspath
import sys
sys.path.append('../')
import src.main.app

class test(unittest.TestCase):

    # <!> Requires that ci.ini is completed. <!>
    #def test_main(self):
        """
        Tests that an instance of History is created when launching the app.
        """
    #    main.app.main()
    #    self.assertFalse(main.app.history == None)
        

if __name__ == '__main__':
    unittest.main()
