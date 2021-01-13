##################################################################################################################
#
#    Aufgage 3.3 Traveling Salesman PRoble
#    Lösungsansatz mit Dijkstra-Algorithmus für ungerichtete gewichtete Graphen mit Hashtabellen
#    "Welcher Pfad von Kiel nach Kiel über alle Punkte ist der "günstigste" ?"
#    Tjark Ziehm
#    12.Januar 2021
#    Mtr. 936030
#    Referenz: Algorithmen kapieren (MITP Professionals) - Aditya Y. Bhargava
##################################################################################################################

# from . import Kiel
# from . import Flensburg
# from . import Hamburg
# from . import Oldenburg
# from . import Bremen
# from . import Rostock
# from . import Braunschweig
# from . import Magdeburg


#import dijkstra
# Erstellung der Grapghen Kiel als Start- und End-Punkt

graph = {}


##################################################################################################################
# Erstellung des Graphen-Beziehungen
#################################################################################################################


# Kiel-Start ####################################################################################################
print("Creating Kiel-Start")
graph["Kiel-Start"] = {}

graph["Kiel-Start"]["Flensburg"] = 2
graph["Kiel-Start"]["Hamburg"] = 2
graph["Kiel-Start"]["Oldenburg"] = 6
graph["Kiel-Start"]["Bremen"] = 3
graph["Kiel-Start"]["Rostock"] = 5
graph["Kiel-Start"]["Braunschweig"] = 4
graph["Kiel-Start"]["Magdeburg"] = 5


# Flensburg ####################################################################################################
print("Creating Flensburg")
graph["Flensburg"] = {}

graph["Flensburg"]["Hamburg"] = 2
graph["Flensburg"]["Oldenburg"] = 6
graph["Flensburg"]["Bremen"] = 3
graph["Flensburg"]["Rostock"] = 5
graph["Flensburg"]["Braunschweig"] = 4
graph["Flensburg"]["Magdeburg"] = 5

graph["Flensburg"]["Kiel-Ende"] = 2


# Hamburg ####################################################################################################
print("Creating Hamburg")
graph["Hamburg"] = {}

graph["Hamburg"]["Flensburg"] = 2
graph["Hamburg"]["Oldenburg"] = 4
graph["Hamburg"]["Bremen"] = 1
graph["Hamburg"]["Rostock"] = 2
graph["Hamburg"]["Braunschweig"] = 2
graph["Hamburg"]["Magdeburg"] = 3

graph["Hamburg"]["Kiel-Ende"] = 2


# Oldenburg ####################################################################################################
print("Creating Oldenburg")
graph["Oldenburg"] = {}

graph["Oldenburg"]["Flensburg"] = 6
graph["Oldenburg"]["Hamburg"] = 4
graph["Oldenburg"]["Bremen"] = 2
graph["Oldenburg"]["Rostock"] = 5
graph["Oldenburg"]["Braunschweig"] = 4
graph["Oldenburg"]["Magdeburg"] = 6

graph["Oldenburg"]["Kiel-Ende"] = 6


# Bremen ####################################################################################################
print("Creating Bremen")
graph["Bremen"] = {}

graph["Bremen"]["Flensburg"] = 2
graph["Bremen"]["Hamburg"] = 1
graph["Bremen"]["Oldenburg"] = 2
graph["Bremen"]["Rostock"] = 3
graph["Bremen"]["Braunschweig"] = 3
graph["Bremen"]["Magdeburg"] = 4

graph["Bremen"]["Kiel-Ende"] = 3

# Rostock ####################################################################################################
print("Creating Rostock")
graph["Rostock"] = {}

graph["Rostock"]["Flensburg"] = 5
graph["Rostock"]["Hamburg"] = 2
graph["Rostock"]["Oldenburg"] = 5
graph["Rostock"]["Bremen"] = 3
graph["Rostock"]["Braunschweig"] = 4
graph["Rostock"]["Magdeburg"] = 4

graph["Rostock"]["Kiel-Ende"] = 5

# Braunschweig ####################################################################################################
print("Creating Braunschweig")
graph["Braunschweig"] = {}

graph["Braunschweig"]["Flensburg"] = 4
graph["Braunschweig"]["Hamburg"] = 2
graph["Braunschweig"]["Oldenburg"] = 4
graph["Braunschweig"]["Bremen"] = 3
graph["Braunschweig"]["Rostock"] = 4
graph["Braunschweig"]["Magdeburg"] = 2

graph["Braunschweig"]["Kiel-Ende"] = 4

# Magedeburg ####################################################################################################
print("Creating Magdeburg")
graph["Magdeburg"] = {}


graph["Magdeburg"]["Flensburg"] = 4
graph["Magdeburg"]["Hamburg"] = 2
graph["Magdeburg"]["Oldenburg"] = 4
graph["Magdeburg"]["Bremen"] = 3
graph["Magdeburg"]["Rostock"] = 4
graph["Magdeburg"]["Braunschweig"] = 2
graph["Magdeburg"]["Kiel-Ende"] = 4

#Kiel-Ende ####################################################################################################
print("Creating Kiel-Ende")
graph["Kiel-Ende"] = {}


##################################################################################################################
#    Erstellung der Cost-HashTabelle
##################################################################################################################
print("Init Cost-Hashtable")
infinity = float("inf")
costs = {}
costs["Flensburg"] = 2
costs["Hamburg"] = 2
costs["Oldenburg"] = 6
costs["Bremen"] = 3
costs["Rostock"] = 5
costs["Braunschweig"] = 4
costs["Magdeburg"] = 5

costs["Kiel-Ende"] = infinity


##################################################################################################################
#    Erstellung der Parent Hashtabelle
##################################################################################################################
print("Init Parent HashTable")
parents = {}
parents["Flensburg"] = "Kiel"
parents["Hamburg"] = "Kiel"
parents["Oldenburg"] = "Kiel"
parents["Bremen"] = "Kiel"
parents["Rostock"] = "Kiel"
parents["Braunschweig"] = "Kiel"
parents["Magdeburg"] = "Kiel"
parents["Kiel-Ende"] = None


processed = []


##################################################################################################################
#    Dijkstra-Algorithmus mit Ausgabefunktion
##################################################################################################################
print("Function")


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None

    # durchsuche die knoten nach günstigsten
    for node in costs:
        cost = costs[node]
        # nimm das günstigesten der unverarbeitet ist
        if cost < lowest_cost and node not in processed:
            # ... verarbeite diesen Knoten mit dem Value
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


# finde den knoten mit den niedrigsten kosten
node = find_lowest_cost_node(costs)


# Wiederhole den Prozess als Loop ( While-Schleife)
while node is not None:
    cost = costs[node]
    # überprüfe die Nachbarn
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # überprüfe günstigere Alternative
        if costs[n] > new_cost:
            # ... aktualisieren die kosten
            costs[n] = new_cost
            # setze günstigsten als Parentdevice
            parents[n] = node
    # "Ist verarbeitet" Marker
    processed.append(node)
    # finde die nächste günstigste Edge
    node = find_lowest_cost_node(costs)

print("Kosten von Kiel über:")
print(costs)
