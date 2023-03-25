import requests
from configloader import ConfigLoader


class JenkinsAPI:
    def __init__(self, configfile):
        self.config_loader = ConfigLoader(configfile)
        self.config = self.config_loader.load_config()

    def build_job(self):
        # -- choose only one url : the first url is correct only if the job is not located on a folder -- #
        # -- url = f"{self.config['jenkins_url']}/job/{self.config['job_name']}/build" -- #
        url = f"{self.config['jenkins_url']}/job/{self.config['folder_name']}/job/{self.config['job_name']}/build"
        auth = (self.config['username'], self.config['api_token'])
        params = {'token': self.config['build_token']}

        resp = requests.post(url, auth=auth, params=params)

        if resp.status_code == 201:
            print(f"[INFO] : Successfully triggered {self.config['job_name']}")
        else:
            print(f"[ERROR] : Failed to trigger build for job {self.config['job_name']}")
            print(f"[FAIL] resp status code: {resp.status_code}")


if __name__ == '__main__':
    api = JenkinsAPI('config.yaml')
    api.build_job()
