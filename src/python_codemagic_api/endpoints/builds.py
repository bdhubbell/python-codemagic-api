from python_codemagic_api.base_endpoint import BaseEndpoint

class Builds(BaseEndpoint):

    ENDPOINT = 'builds'

    def __init__(self, api_token, app_id):
        self.app_id = app_id
        super().__init__(api_token)

    def start_build(self, app_id, workflow_id, branch=None, tag=None, environment={}, labels=[]):
        if not (branch or tag):
            raise Exception

        data =  {
            'appId': app_id,
            'workflowId': workflow_id,
        }

        if branch:
            data['branch'] = branch
        
        if tag:
            data['tag'] = tag
        
        if environment:
            data['environment'] = environment
        
        if labels:
            data['labels'] = labels


        return self.post(f'{self.ENDPOINT}', data)

    def get_builds(self, app_id=None, workflow_id=None, branch=None, tag=None):

        if not (app_id or workflow_id or branch or tag):
            raise Exception

        query_parameters = {}

        if app_id:
            query_parameters['appId'] = app_id
        
        if workflow_id:
            query_parameters['workflowId'] = workflow_id

        if branch:
            query_parameters['branch'] = branch

        if tag:
            query_parameters['tag'] = tag
        
        query_string = ""
        for key, value in query_parameters.items():
            query_string += f'{key}={value}'

        return self.get(f'{self.ENDPOINT}?{query_string}')

    def get_build_status(self, build_id):
        return self.get(f'{self.ENDPOINT}/{build_id}')

    def cancel_build(self, build_id):
        return self.get(f'{self.ENDPOINT}/{build_id}/cancel')
        