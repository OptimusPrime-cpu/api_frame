from src.main.api.foundation.endpoint import Endpoint
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.credit_repay_request import CreditRepayRequest
from src.main.api.models.credit_repay_response import CreditRepayResponse
from src.main.api.models.deposit_user_request import DepositUserRequest
from src.main.api.models.deposit_user_response import DepositUserResponse
from src.main.api.models.request_credit_request import RequestCreditRequest
from src.main.api.models.request_credit_response import RequestCreditResponse
from src.main.api.models.transfer_request import TransferRequest
from src.main.api.models.transfer_response import TransferResponse
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps
from src.main.api.foundation.requesters.crud_requester import CrudRequester


class UserSteps(BaseSteps):
    def create_account(self, create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.request_created()
        ).post()
        return response

    def deposit_user(self, create_user_request: CreateUserRequest, deposit_user_request: DepositUserRequest) -> DepositUserResponse:
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.DEPOSIT_ACCOUNT,
            ResponseSpecs.request_ok()
        ).post(deposit_user_request)
        return response

    def deposit_user_invalid(self, create_user_request: CreateUserRequest, deposit_user_request: DepositUserRequest):
        response = CrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.DEPOSIT_ACCOUNT,
            ResponseSpecs.request_bad()
        ).post(deposit_user_request)
        return response

    def transfer_between_acc(self, create_user_request: CreateUserRequest, transfer_request: TransferRequest ) -> TransferResponse:
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.TRANSFER_BETWEEN_ACCOUNT,
            ResponseSpecs.request_ok()
        ).post(transfer_request)
        return response

    def transfer_acc_invalid(self, create_user_request: CreateUserRequest, transfer_request: TransferRequest ) -> TransferResponse:
        response = CrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.TRANSFER_BETWEEN_ACCOUNT,
            ResponseSpecs.request_bad()
        ).post(transfer_request)
        return response

    def take_credit(self, create_user_request: CreateUserRequest, request_credit_request: RequestCreditRequest) -> RequestCreditResponse:
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.TAKE_CREDIT_USER,
            ResponseSpecs.request_created()
        ).post(request_credit_request)
        return response

    def take_credit_invalid(self, create_user_request: CreateUserRequest, request_credit_request: RequestCreditRequest) -> RequestCreditResponse:
        response = CrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.TAKE_CREDIT_USER,
            ResponseSpecs.request_bad()
        ).post(request_credit_request)
        return response

    def credit_repay(self, create_user_request: CreateUserRequest, credit_repay_request: CreditRepayRequest) -> CreditRepayResponse:
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.REPAY_CREDIT_USER,
            ResponseSpecs.request_ok()
        ).post(credit_repay_request)
        return response

    def credit_repay_invalid(self, create_user_request: CreateUserRequest, credit_repay_request: CreditRepayRequest) -> CreditRepayResponse:
        response = CrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.REPAY_CREDIT_USER,
            ResponseSpecs.request_422()
        ).post(credit_repay_request)
        return response