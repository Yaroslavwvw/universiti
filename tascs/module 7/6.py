towns_db = []
towns_search = []

db_input_count = int(input())

for i in range(0, db_input_count):
    towns_db.append(input().split())

search_input_count = int(input())

for j in range(0, search_input_count):
    towns_search.append(input())

for town in towns_search:
    for data in towns_db:
        if town in data:
            print(data[0])
            break