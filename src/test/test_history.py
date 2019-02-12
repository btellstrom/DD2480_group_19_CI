import unittest
from src.main.history import History
import datetime

class test_history(unittest.TestCase):

    def test_serialize(self):        
        """
        Serialize creates a dictionary based on its input. This test that 
        the dictionary is indeed created correctly.
        """
        build_id = 1
        temp = datetime.datetime.today()
        date_rec = (temp + datetime.timedelta(days=-1))
        date_end = temp
        status = "PASSED"
        commit_url = "example.com"
        
        dictionary = History.serialize(build_id,
                                       date_rec.isoformat(),
                                       date_end.isoformat(),
                                       status,
                                       commit_url)
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
        self.assertTrue(
            dictionary["commitURL"] == commit_url
        )
        
if __name__ == '__main__':
    unittest.main()
