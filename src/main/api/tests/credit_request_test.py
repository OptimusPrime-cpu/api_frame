import pytest
from src.main.api.models.request_credit_request import RequestCreditRequest
@pytest.mark.api

class TestRequestCredit:
    def test_request_credit(self, api_manager, create_credit_user_request):
        response = api_manager.user_steps.create_account(create_credit_user_request)
        request_credit = RequestCreditRequest(accountId=response.id, amount=5000, termMonths=12)
        response_take_credit = api_manager.user_steps.take_credit(create_credit_user_request, request_credit)

        assert response_take_credit.amount == request_credit.amount


    @pytest.mark.parametrize(
        "amount, termMonths",
        [
            (-1, 12),
            (499, 12),
            (15001, 12)
        ]
    )
    def test_request_credit_invalid(self, api_manager, create_credit_user_request,amount, termMonths):
        response = api_manager.user_steps.create_account(create_credit_user_request)
        request_credit = RequestCreditRequest(accountId=response.id, amount=amount, termMonths=termMonths)
        api_manager.user_steps.take_credit_invalid(create_credit_user_request, request_credit)



