import yaml
import requests

class JenkinsAPI:
    def __init__(self):
        configfile = r'config.yaml'
        with open(configfile) as c:
            # config = yaml.safe_load(c)
            config = yaml.load(c, Loader=yaml.FullLoader)

        jenkinsconfigs = config['jenkins']
        self.username = jenkinsconfigs['user']
        self.api_token = jenkinsconfigs['apitoken']
        self.jenkins_url = jenkinsconfigs['server']
        self.job_name = jenkinsconfigs['job']
        self.build_token = jenkinsconfigs['buildtoken']

    def build_job(self):
        url = f"{self.jenkins_url}/job/{self.job_name}/build"
        auth = (self.username, self.api_token)
        params = {'token': self.build_token}

        resp = requests.post(url, auth=auth, params=params)

        if resp.status_code == 201:
            print(f"[INFO] : Successfully triggered {self.job_name}")
        else:
            print(f"[ERROR] : Failed to trigger build for job {self.job_name}")
            print(f"[FAIL] resp status code: {resp.status_code}")

if __name__ == '__main__':
    api = JenkinsAPI()
    api.build_job()
