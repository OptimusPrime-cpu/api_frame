from src.main.api.models.base_model import BaseModel


class RequestCreditResponse(BaseModel):
    id: int
    amount: int | float
    termMonths: int
    balance: int | float
    creditId: int