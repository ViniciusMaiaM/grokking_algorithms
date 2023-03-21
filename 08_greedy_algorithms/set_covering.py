# You pass an array in, and it gets converted to a set.
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
# The keys are the name of the stations and the values are the states that they cover
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])


def my_set_covering(states_needed, stations):
# Varible that will cover the final result of the stations
    final_stations = set()
    while states_needed:
        best_station = None
        # Conjunt of all the states that the stations takes, but were not yet covered
        states_covered = set()
        # Runinng throught all the stations to see wich is the best
        for station, states_for_station in stations.items():
            # Intersection to find items appearing in both sets
            covered = states_needed & states_for_station
            # Check if the station covers more states than the actual best
            if len(covered) > len(states_covered) and station not in final_stations:
                best_station = station
                states_covered = covered
        if best_station is not None:
            # A station for the states has already been found, so it's no longer necessary to search for them
            states_needed -= states_covered
            final_stations.add(best_station)
            stations.pop(best_station)
        else:
            return None
    return final_stations

print(my_set_covering(states_needed, stations))
