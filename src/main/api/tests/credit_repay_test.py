import pytest
from src.main.api.models.credit_repay_request import CreditRepayRequest
from src.main.api.models.request_credit_request import RequestCreditRequest

@pytest.mark.api

class TestRepayCredit:
    def test_credit_repay(self, api_manager, create_credit_user_request):
        account_response = api_manager.user_steps.create_account(create_credit_user_request)
        request_credit = RequestCreditRequest(accountId=account_response.id, amount=5000, termMonths=12)
        credit_response = api_manager.user_steps.take_credit(create_credit_user_request, request_credit)
        repay_request = CreditRepayRequest(accountId=credit_response.id, creditId=credit_response.creditId, amount=5000)
        repay_response = api_manager.user_steps.credit_repay(create_credit_user_request, repay_request)

        assert repay_response.amountDeposited == repay_request.amount

    def test_repay_invalid(self, api_manager, create_credit_user_request):
        account_response = api_manager.user_steps.create_account(create_credit_user_request)
        request_credit = RequestCreditRequest(accountId=account_response.id, amount=5000, termMonths=12)
        credit_response = api_manager.user_steps.take_credit(create_credit_user_request, request_credit)
        repay_request = CreditRepayRequest(accountId=account_response.id, creditId=credit_response.creditId, amount=6000)
        response = api_manager.user_steps.credit_repay_invalid(create_credit_user_request, repay_request)

        assert response.json()["error"] == "Insufficient funds. Current balance: 5000.00, required: 6000.00"