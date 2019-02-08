import json
import subprocess

"""                                                                             
Clones repo, runs all tests as specified in ci.sh.                              
                                                                                
Input:                                                                          
    json_payload - parsed json payload                 
                                                                                
Output:                                                                         
    0 if all tests succeeded                                                    
    1 if compilation/static syntax check succeeds but tests fail                
    2 if compilation/static syntax check fails                                  
"""                                                                             
def repo_test(json_payload):                                                        
    # get important stuff                                                       
    branch_name = json_payload["ref"].split('/')[-1]
    ssh_url = json_payload["repository"]["ssh_url"]
    clone_url = json_payload["repository"]["clone_url"]
    repo_name = json_payload["repository"]["name"]
                                                                                
    # clone repo, switch branch, run ci.sh, remove repo                         
    subprocess.run(["git", "clone", clone_url])                                 
    subprocess.run(["git", "-C", repo_name, "checkout", branch_name])           
    exit_code = subprocess.run(["sh", repo_name + "/ci.sh"]).returncode         
    subprocess.run(["rm", "-rf", repo_name])                                    
                                                                                
    return exit_code
