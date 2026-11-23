import pytest
@pytest.mark.api

class TestAccountCreate:
    def test_account_create(self, api_manager, create_user_request):
        response = api_manager.user_steps.create_account(create_user_request)
        assert response.balance == 0