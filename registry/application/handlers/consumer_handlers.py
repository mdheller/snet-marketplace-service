from common.constant import StatusCode
from common.exception_handler import exception_handler
from common.logger import get_logger
from common.utils import generate_lambda_response
from registry.config import IPFS_URL, NETWORKS, NETWORK_ID, SLACK_HOOK
from registry.consumer.organization_event_consumer import OrganizationCreatedAndModifiedEventConsumer
from registry.consumer.service_event_consumer import ServiceCreatedEventConsumer
from registry.exceptions import EXCEPTIONS
from registry.infrastructure.repositories.organization_repository import OrganizationPublisherRepository
from registry.infrastructure.repositories.service_publisher_repository import ServicePublisherRepository

logger = get_logger(__name__)

org_repository = OrganizationPublisherRepository()
service_repository = ServicePublisherRepository()


def get_event_consumer(event):
    if event['name'] in ["OrganizationCreated", 'OrganizationModified']:
        return OrganizationCreatedAndModifiedEventConsumer(NETWORKS[NETWORK_ID]["ws_provider"], IPFS_URL['url'],
                                                           IPFS_URL['port'], org_repository)
    elif event['name'] in ['ServiceCreated', 'ServiceMetadataModified']:
        return ServiceCreatedEventConsumer(NETWORKS[NETWORK_ID]["ws_provider"], IPFS_URL['url'],
                                           IPFS_URL['port'], service_repository, org_repository)


@exception_handler(SLACK_HOOK=SLACK_HOOK, NETWORK_ID=NETWORK_ID, logger=logger, EXCEPTIONS=EXCEPTIONS)
def organization_event_consumer_handler(event, context):
    logger.info(f"Got Organization Event {event}")
    organization_event_consumer = get_event_consumer(event)
    organization_event_consumer.on_event(event)

    return generate_lambda_response(200, StatusCode.OK)


@exception_handler(SLACK_HOOK=SLACK_HOOK, NETWORK_ID=NETWORK_ID, logger=logger, EXCEPTIONS=EXCEPTIONS)
def service_event_consumer_handler(event, context):
    logger.info(f"Got Service Event {event}")
    organization_event_consumer = get_event_consumer(event)
    organization_event_consumer.on_event(event)

    return generate_lambda_response(200, StatusCode.OK)
