import pytest
from src.main.api.models.deposit_user_request import DepositUserRequest

@pytest.mark.api
class TestDeposit:
    def test_deposit(self, api_manager, create_user_request):
        account_response = api_manager.user_steps.create_account(create_user_request)
        deposit_request = DepositUserRequest(accountId=account_response.id, amount=9000)
        response = api_manager.user_steps.deposit_user(create_user_request, deposit_request)
        assert deposit_request.amount == response.balance

    @pytest.mark.parametrize(
        "deposit_invalid", [-100, 10000, 0]
    )
    def test_deposit_invalid(self, api_manager, create_user_request, deposit_invalid):
        account_response = api_manager.user_steps.create_account(create_user_request)
        deposit_request = DepositUserRequest(accountId=account_response.id, amount=-deposit_invalid)
        api_manager.user_steps.deposit_user_invalid(create_user_request, deposit_request)
