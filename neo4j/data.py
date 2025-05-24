from faker import Faker
from py2neo import Graph, Node, Relationship
import random

fake = Faker()
graph = Graph("bolt://localhost:7687", auth=("neo4j", "cr8UuA6Te6Gyt_U"))

# Categories and cities
categories = ["Museum", "Park", "Hotel", "Beach", "Restaurant"]
cities = ["Addis Ababa", "Hawassa", "Bahir Dar", "Lalibela", "Gondar"]

# Create and merge categories and cities
category_nodes = {cat: Node("Category", name=cat) for cat in categories}
city_nodes = {city: Node("City", name=city) for city in cities}

for node in category_nodes.values():
    graph.merge(node, "Category", "name")

for node in city_nodes.values():
    graph.merge(node, "City", "name")

# Create places
places = []
for _ in range(500):
    place_name = fake.company()
    city = random.choice(cities)
    category = random.choice(categories)
    place = Node("Place", name=place_name)
    graph.create(place)
    graph.create(Relationship(place, "LOCATED_IN", city_nodes[city]))
    graph.create(Relationship(place, "BELONGS_TO", category_nodes[category]))
    places.append(place)

# Create users and relationships
users = []
for _ in range(1000):
    user = Node("User", name=fake.name(), email=fake.email())
    graph.create(user)
    users.append(user)

    liked_categories = random.sample(categories, k=2)
    for cat in liked_categories:
        graph.create(Relationship(user, "LIKES", category_nodes[cat]))

    visited_places = random.sample(places, k=5)
    for place in visited_places:
        graph.create(Relationship(user, "VISITED", place))
        graph.create(Relationship(user, "CLICKED", place))
        rating = random.randint(1, 5)
        graph.create(Relationship(user, "RATED", place, value=rating))

# Create FRIEND relationships
for i in range(1000):
    user1 = random.choice(users)
    user2 = random.choice(users)
    if user1 != user2:
        graph.create(Relationship(user1, "FRIEND_WITH", user2))

# Optional: Make some places similar to each other
for i in range(200):
    p1 = random.choice(places)
    p2 = random.choice(places)
    if p1 != p2:
        graph.create(Relationship(p1, "SIMILAR_TO", p2))