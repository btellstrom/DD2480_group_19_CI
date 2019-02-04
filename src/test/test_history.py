import unittest
import main
from src import history
import datetime

class test_history(unittest.TestCase):

    """
    Serialize creates a dictionary based on its input. This test that 
    the dictionary is indeed created correctly.
    """
    def test_serialize():        
        build_id = 1
        temp = datetime.now().isoformat()
        date_rec = temp - timedelta(days=-1)
        date_end = temp
        status = "PASSED"
        
        dictionary = history.serialize(build_id,
                                       date_rec.isoformat(),
                                       date_end.isoformat(),
                                       status)
        self.assertTrue(dictionary["buildID"] == build_id)
        self.assertTrue(
            dictionary["dateReceivedBuild"] == date_rec.isoformat()
        )
        self.assertTrue(
            dictionary["dateFinishedBuild"] == date_end.isoformat()
        )
        self.assertTrue(
            dictionary["status"] == status
        )
        
if __name__ == '__main__':
    unittest.main()
