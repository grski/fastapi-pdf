from enum import StrEnum

COOKIE_EXPIRE_TIME = 60 * 60 * 24 * 30  # 30 days


class FailureConstants(StrEnum):
    USER_NOT_FOUND = "User not found"
    USER_NOT_CONFIRMED = "User is not confirmed"
