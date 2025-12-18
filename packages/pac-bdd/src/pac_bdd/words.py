from pytest_bdd import scenario, given, when, then
import pytest
from pytest_bdd import parsers



@pytest.fixture
def auth():
    return {}

@pytest.fixture
def author():
    return "bob"


@given("un utilisateur")
def author_user(auth, author):
    auth["user"] = author


@given(
    parsers.parse("la PA #{pa}"),
)
def pa_given(pa):
    ...


@given(
    parsers.parse("l'entreprise #{company} enregistrée sur la PA #{pa}"),
)
def company_given(company, pa): ...


@given(
    parsers.parse(
        "la facture #{invoice} de #{company1} à #{company2}"
    ),
)
def invoice_given(invoice, company1, company2): ...


@when("je dépose une facture")
@when(
    parsers.parse(
        "je dépose la facture #{invoice} sur #{pa}"
    ),
)
def submit_invoice():
    ...


@then("j'obtiens un numéro de tâche")
def job_id():
    ...


@when("j'interroge la tâche")
def task_status(): ...



@then(
    parsers.parse("j'obtiens le statut #{status}"),
)
def job_status(status):
    ...
