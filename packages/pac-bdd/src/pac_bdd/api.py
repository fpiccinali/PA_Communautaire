# SPDX-FileCopyrightText: 2026 Philippe ENTZMANN <philippe@entzmann.name>
#
# SPDX-License-Identifier: GPL-3.0-or-later

import asyncio
import functools
from typing import Any

import httpx
from pydantic import BaseModel
import pytest
from pac0.shared.test.world import WorldContext, world, world1
from pytest_bdd import given, parsers, scenario, then, when


# local BDD context class
class LocalTestCtx(BaseModel):
    result: Any | None = None
    # TODO: make a typed result_request


# local BDD context fixture
@pytest.fixture
def ctx():
    """Contexte pour les tests BDD"""
    return LocalTestCtx()


# Soit une pa communautaire
@given("""une pa communautaire""")
def api_call(
    world1: WorldContext,
):
    pass


# Quand j'appele l'API GET /healthcheck
@when(
    parsers.parse("j'appele l'API {verb} {path}"),
)
def api_call(
    ctx: LocalTestCtx,
    world1: WorldContext,
    verb: str,
    path: str,
):
    with world1.pa1.get_client() as client:
        # response = client.get(path)
        ctx.result = client.request(verb, path)

    """
    async with world1pac.pac1.HttpxAsyncClient() as client:
        print(f"testing pac {world1pac.pac1} ...")
        print(world1pac.pac1.info())
        await asyncio.sleep(60)
        response = await client.get("/")
        assert response.status_code == 200
        assert response.json() == {"Hello": "World"}
    """
    raise NotImplementedError()


# Alors j'obtiens le code de retour 200
@then(parsers.parse("j'obtiens le code de retour {code}"))
def api_return_code(
    ctx: LocalTestCtx,
    code,
):
    # assert response.status_code == 200
    assert ctx.result.status_code == code
    # assert response.json() == {"Hello": "World"}
