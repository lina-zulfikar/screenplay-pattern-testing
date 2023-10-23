# """
# These tests cover Admin CGAA.
# """

import pytest

from screenplay.pattern import Actor
from testlib.interactions import *
from testlib.pages import LoginPage, AddMultipleChoicePage

# @pytest.mark.parametrize('phrase', ['panda', 'python', 'parakeet'])
def test_cgaa_login(actor: Actor):
        actor.attempts_to(Load(LoginPage.URL))
        actor.attempts_to(LogInCgaa())


def test_add_multiplechoice(actor: Actor):
        actor.attempts_to(AddMultipleChoicePage())

