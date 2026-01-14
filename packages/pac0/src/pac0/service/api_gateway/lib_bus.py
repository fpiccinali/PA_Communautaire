# SPDX-FileCopyrightText: 2026 Philippe ENTZMANN <philippe@entzmann.name>
#
# SPDX-License-Identifier: GPL-3.0-or-later

import os

from fastapi import FastAPI
from faststream.nats.fastapi import NatsRouter
from pac0.service.api_gateway.lib_common import global_state
from pac0.shared.esb import get_nats_url


router = NatsRouter(get_nats_url())


@router.after_startup
async def test(app: FastAPI):
    await router.broker.publish("Startup!!!", "test")



@router.subscriber("healthcheck")
async def healthcheck_sub(
    # message: Incoming,
    # logger: Logger,
):
    # logger.info("Incoming value: %s, depends value: %s" % (message.m, dependency))
    await router.broker.publish("I am alive !", "healthcheck_resp")

@router.subscriber("healthcheck_resp")
async def healthcheck_resp_sub(
    # message: Incoming,
    # logger: Logger,
    #state: Annotated[dict[str, Any], Depends(global_state)],
):
    # logger.info("Incoming value: %s, depends value: %s" % (message.m, dependency))
    global_state["healthcheck_resp"].append("xx")
