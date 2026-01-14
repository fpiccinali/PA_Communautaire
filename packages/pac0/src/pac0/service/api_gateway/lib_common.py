from typing import Any
from fastapi import Request


def broker(
    request: Request,
):
    """dependency shortcut to access the broker"""
    return request.app.state.broker


# global state from api router or broker router"""
global_state: dict[str, Any] = {
    'healthcheck_resp': [],
}

