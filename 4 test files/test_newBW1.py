import pytest , csv 
from models.users import User , USER_ADULT_AGE , Status

@pytest.fixture
def users()->list[User]: 
    with open("users.csv") as file: 
        users = list(csv.DictReader(file,delimiter=';'))
    return [User(
        name=user["name"],
        age=int(user["age"]),
        status=Status(user["status"]),
        items=user.get("items", "").split(",") if user.get("items") else []
    ) for user in users]

@pytest.fixture
def workers(users) -> list[User]:
    workers = []
    for user in users: 
        if user.status == Status.WORKER:
            workers.append(user)

    return workers

def user_is_adult(user: User) -> bool:
    return user.age >= USER_ADULT_AGE


def test_worker_age(workers):
    for worker in workers:
        assert worker.is_adult(), f"worker {worker.name} under 18"