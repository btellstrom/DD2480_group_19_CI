import unittest
import json
from src.main.repo_tester import *                                                  
                                                                                
class test_repo_tester(unittest.TestCase):                                      
                                                                                
    def test_1(self):                                                           
        """                                                                         
        Should, given a pull request type event, clone the repo,                    
        switch to the correct branch, run "ci.sh" in the root                       
        of the repository, remove the repo, and finally return                      
        the exit code of "ci.sh". for json_pull_request_example.txt
        the exit code should be 10.
        """                                                                         
        with open('test/json_push_example.txt', 'r') as payloadfile:         
            payload = payloadfile.read()                                        
            self.assertTrue(repo_test(json.loads(payload)) == 10)                           

if __name__ == '__main__':                                                      
    unittest.main()                                                             
                                                                                
                                                                                                      
                                  
