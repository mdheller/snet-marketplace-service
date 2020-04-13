import os
from enum import Enum

COMMON_CNTRCT_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'node_modules', 'singularitynet-platform-contracts'))
REG_CNTRCT_PATH = os.path.join(COMMON_CNTRCT_PATH, 'abi', 'Registry.json')
MPE_CNTRCT_PATH = os.path.join(COMMON_CNTRCT_PATH, "abi", "MultiPartyEscrow.json")
REG_ADDR_PATH = os.path.join(COMMON_CNTRCT_PATH, "networks", "Registry.json")
MPE_ADDR_PATH = os.path.join(COMMON_CNTRCT_PATH, "networks", "MultiPartyEscrow.json")

TEST_COMMON_CNTRCT_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'test', 'node_modules', 'singularitynet-platform-contracts'))
TEST_REG_CNTRCT_PATH = os.path.join(TEST_COMMON_CNTRCT_PATH, 'abi', 'Registry.json')
TEST_REG_ADDR_PATH = os.path.join(TEST_COMMON_CNTRCT_PATH, "networks", "Registry.json")


class OrganizationStatus(Enum):
    ONBOARDING = "ONBOARDING"
    ONBOARDING_APPROVED = "ONBOARDING_APPROVED"
    DRAFT = "DRAFT"
    APPROVAL_PENDING = "APPROVAL_PENDING"
    APPROVED = "APPROVED"
    PUBLISH_IN_PROGRESS = "PUBLISH_IN_PROGRESS"
    PUBLISHED = "PUBLISHED"
    REJECTED = "REJECTED"
    FAILED = "FAILED"
    PUBLISHED_UNAPPROVED = "PUBLISHED_UNAPPROVED"
    ONBOARDING_REJECTED = "ONBOARDING_REJECTED"
    CHANGE_REQUESTED = "CHANGE_REQUESTED"


ORG_STATUS_LIST = [OrganizationStatus.APPROVED.value, OrganizationStatus.REJECTED.value, OrganizationStatus.CHANGE_REQUESTED.value]


class OrganizationActions(Enum):
    DRAFT = "DRAFT"
    SUBMIT = "SUBMIT"
    CREATE = "CREATE"


class OrganizationMemberStatus(Enum):
    PUBLISHED = "PUBLISHED"
    PENDING = "PENDING"
    PUBLISH_IN_PROGRESS = "PUBLISH_IN_PROGRESS"
    ACCEPTED = "ACCEPTED"


class Role(Enum):
    OWNER = "OWNER"
    MEMBER = "MEMBER"


# Should be subset of with verification.constants.VerificationStatus
class VerificationStatus(Enum):
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"


class Action(Enum):
    CREATE = "CREATE"
    SUBMIT = "SUBMIT"
    PUBLISH = "PUBLISH"
    UPDATE = "UPDATE"
    READ = "READ"


class ServiceAvailabilityStatus(Enum):
    AVAILABLE = "AVAILABLE"
    UNAVAILABLE = "UNAVAILABLE"


class OrganizationIDAvailabilityStatus(Enum):
    AVAILABLE = "AVAILABLE"
    UNAVAILABLE = "UNAVAILABLE"


class ServiceStatus(Enum):
    DRAFT = "DRAFT"
    APPROVAL_PENDING = "APPROVAL_PENDING"
    APPROVED = "APPROVED"
    PUBLISH_IN_PROGRESS = "PUBLISH_IN_PROGRESS"
    PUBLISHED = "PUBLISHED"
    CHANGE_REQUESTED = "CHANGE_REQUESTED"
    REJECTED = "REJECTED"
    FAILED = "FAILED"
    PUBLISHED_UNAPPROVED = "PUBLISHED_UNAPPROVED"


class OrganizationAddressType(Enum):
    MAIL_ADDRESS = "mailing_address"
    HEAD_QUARTER_ADDRESS = "headquarters_address"


class OrganizationType(Enum):
    ORGANIZATION = "organization"
    INDIVIDUAL = "individual"


ORG_TYPE_VERIFICATION_TYPE_MAPPING = {"JUMIO": OrganizationType.INDIVIDUAL.value,
                                      "DUNS": OrganizationType.ORGANIZATION.value}


class EnvironmentType(Enum):
    TEST = "TEST"
    MAIN = "MAIN"


class ServiceSupportType(Enum):
    SERVICE_APPROVAL = "SERVICE_APPROVAL"


class UserType(Enum):
    SERVICE_APPROVER = "SERVICE_APPROVER"
    SERVICE_PROVIDER = "SERVICE_PROVIDER"


DEFAULT_SERVICE_RANKING = 1
