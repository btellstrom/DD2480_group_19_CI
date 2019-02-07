
import requests
import json

"""
update_status sends a POST request to the GitHub API to update the commit status.
:param commit_url: The url should be retrieved from PR data['pull_request']['statuses_url']
:param status: The status of the commit can be 'pending', 'success' or 'failure'.
:param auth_token: The access token must be included to authenticate to GitHub
:return: Returns the POST request if the input is valid  

"""
def update_status(commit_url, status, auth_token):
	# post_url stores the correct form of the url to be used in the POST request 
	post_url = commit_url[:8] + auth_token + ':x-oauth-basic@' + commit_url[8:]
	
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
		print('invalid input for status')