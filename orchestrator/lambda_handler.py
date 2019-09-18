import traceback

from common.repository import Repository
from common.utils import (
    Utils,
    generate_lambda_response,
    extract_payload,
    validate_dict,
    format_error_message,
)
from orchestrator.order_service import OrderService
from orchestrator.config import NETWORKS, NETWORK_ID
from orchestrator.constant import REQUIRED_KEYS_FOR_LAMBDA_EVENT

NETWORKS_NAME = dict((NETWORKS[netId]["name"], netId) for netId in NETWORKS.keys())
db = dict((netId, Repository(net_id=netId)) for netId in NETWORKS.keys())
obj_util = Utils()


def route_path(path, method, payload_dict, request_context=None):
    obj_order_service = OrderService(obj_repo=db[NETWORK_ID])
    path_exist = True
    if "order/initiate" == path:
        response_data = obj_order_service.initiate_order(
            user_data=request_context, payload_dict=payload_dict
        )

    elif "order/execute" == path and method == "POST":
        response_data = obj_order_service.execute_order(
            user_data=request_context, payload_dict=payload_dict
        )
    else:
        path_exist = False

    return path_exist, response_data


def request_handler(event, context):
    try:
        valid_event = validate_dict(
            event=event, required_keys=REQUIRED_KEYS_FOR_LAMBDA_EVENT
        )
        if not valid_event:
            return generate_lambda_response(400, "Bad Request")

        path = event["path"].lower()
        method = event["httpMethod"]

        method_found, payload_dict = extract_payload(method=method, event=event)
        if not method_found:
            return generate_lambda_response(405, "Method Not Allowed")

        path_exist, response_data = route_path(
            path=path,
            method=method,
            payload_dict=payload_dict,
            request_context=event["requestContext"],
        )
        if not path_exist:
            return generate_lambda_response(404, "Not Found")

        if response_data is None:
            error_message = format_error_message(
                status="failed",
                error="Bad Request",
                resource=path,
                payload=payload_dict,
                net_id=NETWORK_ID,
            )
            obj_util.report_slack(1, error_message)
            response = generate_lambda_response(500, error_message)
        else:
            response = generate_lambda_response(
                200, {"status": "success", "data": response_data}
            )
    except Exception as e:
        error_message = format_error_message(
            status="failed",
            error="Bad Request",
            resource=path,
            payload=payload_dict,
            net_id=NETWORK_ID,
        )
        obj_util.report_slack(1, error_message)
        response = generate_lambda_response(500, error_message)
        traceback.print_exc()
    return response
