# This curl command makes an HTTP POST request to trigger a Jenkins build job named JOB_NAME. 
# It uses the credentials of user USER with API token USER_API_TOKEN and includes 
# a build token BUILD_TOKEN_NAME as a parameter in the URL.
# This curl command perform the same task as build.py



curl -X POST -u "USER:USER_API_TOKEN" "JENKINS_URL/job/JOB_NAME/build?token=BUILD_TOKEN_NAME"
