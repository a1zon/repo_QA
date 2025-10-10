import csv 

def test_adults():
    with open("users.csv") as file: 
        users = csv.DictReader(file, delimiter=";")
        users = list(users)
        workers = [user for user in users if user["status"] == "worker"]


        for worker in workers: 
            assert int(worker["age"]) >= 18, f"worker {worker["name"] } under 18"
    print(users)
    


            # workers = []
        # for user in users : 
        #     if user["status"] == "woeker": 
        #         workers.append(user)