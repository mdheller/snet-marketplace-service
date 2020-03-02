from enum import Enum


class JumioVerificationStatus(Enum):
    PENDING = "PENDING"
    SUBMIT_SUCCESS = "SUBMIT_SUCCESS"
    SUBMIT_ERROR = "SUBMIT_ERROR"
    APPROVED_VERIFIED = "APPROVED"
    DENIED_FRAUD = "DENIED"
    DENIED_UNSUPPORTED_ID_TYPE = "DENIED"
    DENIED_UNSUPPORTED_ID_COUNTRY = "DENIED"
    ERROR_NOT_READABLE_ID = "DENIED"
    NO_ID_UPLOADED = "DENIED"


class VerificationStatus(Enum):
    PENDING = "PENDING"
    SUBMIT = "SUBMITTED"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    FAILED = "FAILED"


class VerificationType(Enum):
    JUMIO = "JUMIO"
    DUNS = "DUNS"
