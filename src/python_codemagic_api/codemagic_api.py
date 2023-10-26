from python_codemagic_api.endpoints.applications import Applications
from python_codemagic_api.endpoints.artifacts import Artifacts
from python_codemagic_api.endpoints.builds import Builds
from python_codemagic_api.endpoints.caches import Caches
from python_codemagic_api.endpoints.teams import Teams

class CodemagicApi:

    def __init__(self, api_token, app_id):
        self.applications = Applications(api_token, app_id)
        self.artifacts = Artifacts(api_token, app_id)
        self.builds = Builds(api_token, app_id)
        self.caches = Caches(api_token, app_id)
        self.teams = Teams(api_token, app_id)

