"""Demonstrate an undirected weighted graph."""
from pydsa_lite.structures import Graph

routes = Graph[str]()
routes.add_edge("Nairobi", "Naivasha", 90)
routes.add_edge("Naivasha", "Nakuru", 75)
routes.add_edge("Nairobi", "Thika", 45)
for city in routes:
    print(city, "connects to", routes.neighbors(city))
