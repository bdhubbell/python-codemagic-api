from python_codemagic_api.base_endpoint import BaseEndpoint


class Applications(BaseEndpoint):

    ENDPOINT = "apps"

    def __init__(self, api_token, app_id):
        self.app_id = app_id
        super().__init__(api_token)

    # def get_all_apps(self):
    #     return self.get(f'{ENDPOINT}/{self.app_id}/variables')

    def get_all_environment_variables(self):
        return self.get(f'{self.ENDPOINT}/{self.app_id}/variables')

    def get_application_by_id(self, id):
        return self.get(f'{self.ENDPOINT}/{id}')

    def create_application_from_public_repository(self, repository_url, team_id):
        pass
        # return self.post(
        #     f'{ENDPOINT}',
        #     data={
        #         'repositoryUrl': repository_url,
        #         'team_id': team_id
        #     }
        # )

    def create_applcation_from_private_repository(self, repository_url, ssh_key, project_type, team_id):
        pass

    def get_env_vars(self, app_id):
        return self.get(f'{self.ENDPOINT}/{app_id}/variables')

    def create_env_var(self, app_id, key, value, group=None, workflow_id=None, is_secure=False):
        data = {
            'key': key,
            'value': value,
            'secure': is_secure
        }

        if group:
            data['group'] = group
        
        if workflow_id:
            data['workflowId'] = workflow_id

        return self.post(f'{selfENDPOINT}/{app_id}/variables', data)

    def update_env_var(app_id, env_var_id, value, is_secure=False):
        return self.post(
            f'{self.ENDPOINT}/{app_id}/variables/{env_var_id}',
            {
                'value': value,
                'secure': is_secure
            }
        )

    def delete_env_var(app_id, env_var_id):
        return self.delete(f'{self.ENDPOINT}/{app_id}/variables/{env_var_id}')
