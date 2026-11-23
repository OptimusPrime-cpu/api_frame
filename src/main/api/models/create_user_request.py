from typing import Annotated
from src.main.api.generators.creation_rule import CreationRule
from src.main.api.models.base_model import BaseModel
from pydantic import Field

class CreateUserRequest(BaseModel):
        username: Annotated[str, CreationRule(regex=r'^[A-Za-z0-9]{3,15}$')] = Field(pattern=r'^[A-Za-z0-9]{3,15}$')
        password: Annotated[str, CreationRule(regex=r'^[A-Z]{3}[a-z]{1}[0-9]{2}[!$_]{4}$')] = Field(pattern=r'^[A-Z]{3}[a-z]{1}[0-9]{2}[!$_]{4}$')
        role: Annotated[str, CreationRule(regex=r'^ROLE_(USER|CREDIT_SECRET)$')] = Field(pattern=r'^ROLE_(USER|CREDIT_SECRET)$')