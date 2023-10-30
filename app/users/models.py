import uuid

from pydantic import Field
from pydantic.main import BaseModel

from app.core.models import TimestampAbstractModel


class User(TimestampAbstractModel):
    id: int = Field(primary_key=True)
    name: str
    email: str
    is_confirmed: bool
    uuid: str


class InvitationKey(TimestampAbstractModel):
    id: int = Field(primary_key=True)
    uuid: str
    user_uuid: str
    user_email: str
    is_used: bool


class UserInvitation(BaseModel):
    user_email: str
    name: str
    message_limit: int
    is_used: bool
    uuid: str = Field(default=str(uuid.uuid4()))
