# SPDX-FileCopyrightText: 2026 Philippe ENTZMANN <philippe@entzmann.name>
#
# SPDX-License-Identifier: GPL-3.0-or-later

import os
from fastapi import FastAPI
from pac0.service.api_gateway.lib import router
from faststream.nats import NatsBroker
from faststream.nats.fastapi import NatsRouter

app = FastAPI()
app.state.rank = "dev"

nats_url = os.environ.get("NATS_URL", "nats://localhost:4222")
print(f"Connecting to NATS {nats_url} ...")
nats_router = NatsRouter(nats_url)

app.include_router(nats_router)

app.state.broker = nats_router.broker

app.include_router(router)
