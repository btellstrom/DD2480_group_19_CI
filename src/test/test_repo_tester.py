import unittest
import subprocess
import json
from src.main.repo_tester import *                                                  

"""
repo_tester should, given a valid json formatted push type event, clone the repo,                    
switch to the correct branch, run "ci.sh" in the root of the repository, remove
the repo, and finally return the exit code of "ci.sh".

Note: Whether the tests or the compilation/syntax check fails is determined
by ci.sh. ci.sh should be a script that returns 0 if everything is 
successful, 1 if one or more tests fail, 2 if the compilation/syntax
check fails. If ci.sh does not exit or returns something other than 0, 1 or 2,
then repo_tester should return -1.
"""
class test_repo_tester(unittest.TestCase):                                      
    
    """                                                                         
    Clones demo_repo and switches to a branch where ci.sh returns 
    something other than 0, 1, 2. If ci.sh is malformed or missing,
    repo_test should return -1.
    """                                                                               
    def test_invalid1(self):                                                           
        with open('test/json_push_invalid1.txt', 'r') as payloadfile:         
            payload = payloadfile.read()                                        
            self.assertTrue(repo_test(json.loads(payload)) == -1)
        # Check that demo_repo is removed.
        self.assertTrue(subprocess.run(["test", "-d", "demo_repo"]).returncode == 1)

    """
    Clones demo_repo and switches to a branch without a ci.sh. If ci.sh is
    malformed or missing, repo_test should return -1.
    """
    def test_invalid2(self):                                                           
        with open('test/json_push_invalid2.txt', 'r') as payloadfile:         
            payload = payloadfile.read()                                        
            self.assertTrue(repo_test(json.loads(payload)) == -1)
        # Check that demo_repo is removed.
        self.assertTrue(subprocess.run(["test", "-d", "demo_repo"]).returncode == 1)

    """
    Clones demo_repo and switches to a branch which has a ci.sh which returns
    exitcode 0 (everything succeeded). repo_test should also return 0.
    """
    def test_valid1(self):                                                           
        with open('test/json_push_valid1.txt', 'r') as payloadfile:              
            payload = payloadfile.read()                                        
            self.assertTrue(repo_test(json.loads(payload)) == 0)                           
        # Check that demo_repo is removed.
        self.assertTrue(subprocess.run(["test", "-d", "demo_repo"]).returncode == 1)

if __name__ == '__main__':                                                      
    unittest.main()                                                             
                                                                                
                                                                                                      
                                  
