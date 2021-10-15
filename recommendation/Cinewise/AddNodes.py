from .models import Node
from utils.Movies import load_nodes

nodes = load_nodes()
for node in nodes:
    Node(name=node).save()
