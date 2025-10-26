import pytest


@pytest.fixture(scope="session")
def browser():
    print("Setting up browser")
    yield
    print("Tearing down browser")


@pytest.fixture
def login_page(browser):
    print("Navigating to login page")   
    pass

@pytest.fixture
def user():
    return "user" , "password" 

def test_login(user, login_page):
    username, password = user

    assert username == "user"
    assert password == "password"
