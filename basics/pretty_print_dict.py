import pprint

# test dictionary
dict = {
    "id": 34,
    "name": "Jason",
    "class": 5,
    "marks": {"math": 92, "science": 95, "social_science": 88, "english": 78},
}

# {'id': 34, 'name': 'Jason', 'class': 5, 'marks': {'math': 92, 'science': 95, 'social_science': 88, 'english': 78}}
print(dict)

# {'class': 5,
# 'id': 34,
# 'marks': {'english': 78, 'math': 92, 'science': 95, 'social_science': 88},
# 'name': 'Jason'}
pprint.pprint(dict)
