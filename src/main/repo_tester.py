import json
import subprocess

def repo_test(json_payload):                                                        
    """                                                                             
    Clones repo, runs all tests as specified in ci.sh.                             
                                                                            
    + json_payload - parsed json payload                 
    
    + return                                                                         
        + -1 if ci.sh is malformed (returncode != {0,1,2}) or missing
        + 0 if all tests succeeded                                                    
        + 1 if compilation/static syntax check succeeds but tests fail                
        + 2 if compilation/static syntax check fails                                  
    """                                                                             
    # get important stuff                                                       
    branch_name = json_payload["ref"].split('/')[-1]
    ssh_url = json_payload["repository"]["ssh_url"]
    clone_url = json_payload["repository"]["clone_url"]
    repo_name = json_payload["repository"]["name"]
                                                                                
    # clone repo, switch branch                         
    subprocess.run(["git", "clone", clone_url])                                 
    subprocess.run(["git", "-C", repo_name, "checkout", branch_name])           
    
    # Check that ci.sh exists
    ci_exists = subprocess.run(["test", "-f", "ci.sh"])
    if ci_exists == 1:
        return -1
    
    # Run ci.sh, remove repo.
    exit_code = subprocess.run(["sh", repo_name + "/ci.sh"]).returncode         
    subprocess.run(["rm", "-rf", repo_name])

    # Check that ci.sh returns valid exit code
    if exit_code < 0 or exit_code > 2:
        return -1

    return exit_code
