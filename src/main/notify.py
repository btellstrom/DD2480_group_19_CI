
import requests
import json

"""
update_status sends a POST request to the GitHub API to update the commit status.
:param json_payload: The JSON data coming from the push
:param status: The status of the commit can be 'pending', 'success' or 'failure'.
:param auth_token: The access token must be included to authenticate to GitHub
:return: Returns the POST request if the input is valid 

"""
def update_status(json_payload, status, auth_token):
	sha = json_payload['head_commit']['id'] 
	status_url = json_payload["repository"]['statuses_url'] # gets url of form https://.../{sha}
	status_url_sha = status_url.replace('{sha}',sha) # replaces '{sha}' in status_url with actual sha
	#post_url stores the correct form of the url to be used in the POST request 
	post_url = status_url_sha[:8] + auth_token + ':x-oauth-basic@' + status_url_sha[8:]
	
	try:
		if status == 'pending':
			payload = {'state':status, 
			'description':'The CI service is currently running',
			'context': 'CI for group 19'}
		elif status == 'success':
			payload = {'state':status, 
			'description':'The build succeeded!',
			'context': 'CI for group 19'}
		elif status == 'failure':
			payload = {'state':status, 
			'description':'The build failed',
			'context': 'CI for group 19'}
		post_req = requests.post(post_url, json=payload)
		return post_req

	
	except Exception:
		return None
		


