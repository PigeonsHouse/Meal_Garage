import pytest
from .fixtures import client, use_test_db_fixture, session_for_test, user_for_test
from cruds.users import gen_password_hash

@pytest.mark.usefixtures('use_test_db_fixture')
class TestFood:
    pass
