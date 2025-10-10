import pytest , csv

@pytest.fixture
def users(): 
    with open("users.csv") as file: 
        users = list(csv.DictReader(file,delimiter=';'))
    return users 

@pytest.fixture
def workers(users):
    workers = []
    for user in users: 
        if user["status"] == "worker":
            workers.append(user)

    return workers

def user_is_adult(user):
    return int(user["age"]) >= 18


def test_worker_age(workers):
    for worker in workers:
        assert user_is_adult(worker), f"worker {worker["name"]} under 18"