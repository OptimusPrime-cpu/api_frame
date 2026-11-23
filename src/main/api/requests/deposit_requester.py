from src.main.api.models.deposit_user_request import DepositUserRequest
from src.main.api.models.deposit_user_response import DepositUserResponse
from src.main.api.requests.requester import Requester
import requests

class DepositRequester(Requester):
    def post(self, deposit_user_request: DepositUserRequest):
        url = f"{self.base_url}/account/deposit"
        response = requests.post(
            url=url,
            json=deposit_user_request.model_dump(),
            headers=self.headers,
        )
        self.response_spec(response)
        return DepositUserResponse(**response.json())