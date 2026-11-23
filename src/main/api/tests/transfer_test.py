import pytest
from src.main.api.models.deposit_user_request import DepositUserRequest
from src.main.api.models.transfer_request import TransferRequest

@pytest.mark.api
class TestTransfer:
    def test_transfer(self, api_manager, create_user_request):
        account_first = api_manager.user_steps.create_account(create_user_request)
        deposit_resp = DepositUserRequest(accountId=account_first.id, amount=9000)
        api_manager.user_steps.deposit_user(create_user_request, deposit_resp)
        account_second = api_manager.user_steps.create_account(create_user_request)
        transfer = TransferRequest(fromAccountId=account_first.id, toAccountId=account_second.id,amount=2000)
        response = api_manager.user_steps.transfer_between_acc(create_user_request, transfer)
        expected_balans = deposit_resp.amount - transfer.amount
        assert response.fromAccountIdBalance == expected_balans

# здесь я просто хотел проверить граничные значения. не стал убирать то, что выше, подумал, мол, гибридный подход
    @pytest.mark.parametrize(
        "deposit_amount, transfer_amount, expected_balance", [
            (9000, 2000, 7000),  # Обычный перевод
            (5000, 500, 4500),  # Перевод на минимальную сумму
            (9000, 9000, 0),  # Перевод на максимальную сумму
        ])
    def test_transfer_all_positive(self, api_manager, create_user_request, deposit_amount, transfer_amount,expected_balance):
        account_first = api_manager.user_steps.create_account(create_user_request)
        deposit_resp = DepositUserRequest(accountId=account_first.id, amount=deposit_amount)
        api_manager.user_steps.deposit_user(create_user_request, deposit_resp)
        account_second = api_manager.user_steps.create_account(create_user_request)
        transfer = TransferRequest(fromAccountId=account_first.id, toAccountId=account_second.id, amount=transfer_amount)
        response = api_manager.user_steps.transfer_between_acc(create_user_request, transfer)
        assert response.fromAccountIdBalance == expected_balance

    @pytest.mark.parametrize(
        "invalid_transfer", [499, 11000, 0]
    )
    def test_transfer_invalid(self, api_manager, create_user_request, invalid_transfer):
        account_first = api_manager.user_steps.create_account(create_user_request)
        deposit_resp = DepositUserRequest(accountId=account_first.id, amount=9000)
        api_manager.user_steps.deposit_user(create_user_request, deposit_resp)
        account_second = api_manager.user_steps.create_account(create_user_request)
        transfer = TransferRequest(fromAccountId=account_first.id, toAccountId=account_second.id, amount=invalid_transfer)
        response = api_manager.user_steps.transfer_acc_invalid(create_user_request, transfer)
        assert "Amount must be between 500 and 10000" in response.json()["error"]