import yaml


class ConfigLoader:
    def __init__(self, configfile):
        self.configfile = configfile

    def load_config(self):
        with open(self.configfile) as c:
            config = yaml.safe_load(c)

        jenkins_configs = config['jenkins']
        return {
            'username': jenkins_configs['user'],
            'api_token': jenkins_configs['apitoken'],
            'jenkins_url': jenkins_configs['server'],
            'folder_name': jenkins_configs['folder'],
            'job_name': jenkins_configs['job'],
            'build_token': jenkins_configs['buildtoken']
        }
