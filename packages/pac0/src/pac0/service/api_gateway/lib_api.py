# SPDX-FileCopyrightText: 2026 Philippe ENTZMANN <philippe@entzmann.name>
#
# SPDX-License-Identifier: GPL-3.0-or-later

from typing import Annotated, Any, Union

from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel
from faststream.nats import NatsBroker
import asyncio

from pac0.service.api_gateway.lib_common import global_state, broker


router = APIRouter()



@router.get("/")
async def read_root():
    return {"Hello": "World"}


@router.post("/flows")
async def flows_post():
    return {"Hello": "World"}


@router.get("/flows/{flowId}")
async def flows_get():
    return {"Hello": "World"}


@router.get("/healthcheck")
async def healthcheck(
    request: Request,
):
    return {
        "status": "OK",
        "rank": request.app.state.rank,
    }


@router.get("/healthcheck/deep")
async def healthcheck_deep(
    request: Request,
    broker: Annotated[NatsBroker, Depends(broker)],
):
    # ping the broker
    await broker.ping(timeout=5.0)
    # ask every services how they feel
    await broker.publish("Hello, NATS!", "healthcheck")
    # wait for responses
    await asyncio.sleep(2.0)

    return {
        "status": "OK",
        "rank": request.app.state.rank,
        "healthcheck_resp": global_state["healthcheck_resp"],
    }

