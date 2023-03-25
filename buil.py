import yaml
import requests

class JenkinsAPI:
    def __init__(self):
        configfile = r'config.yaml'
        with open(configfile) as file:
            config = yaml.load(file, Loader=yaml.FullLoader)

        jenkins_config = config['jenkins']
        self.username = jenkins_config['user']
        self.api_token = jenkins_config['apitoken']
        self.jenkins_url = jenkins_config['server']
        self.job_name = jenkins_config['job']
        self.build_token = jenkins_config['buildtoken']

    def build_job(self):
        url = f"{self.jenkins_url}/job/{self.job_name}/build"
        auth = (self.username, self.api_token)
        params = {'token': self.build_token}
        response = requests.post(url, auth=auth, params=params)
        if response.status_code == 201:
            print(f"[INFO] Successfully triggered {self.job_name}")
        else:
            print(f"Failed to trigger build for job {self.job_name}. Response status code: {response.status_code}")

if __name__ == '__main__':
    api = JenkinsAPI()
    api.build_job()
