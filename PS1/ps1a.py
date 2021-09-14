###########################
# 6.0002 Problem Set 1a: Space Cows
# Name: Vu Thanh Dat
# Collaborators: None
# Time:

from time import time
from os import pardir
import time
from typing import Counter

from ps1_partition import get_partitions, partitions

# ================================
# Part A: Transporting Space Cows
# ================================

# Problem 1


def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    cows = {}
    with open(filename) as f:
        lines = f.readlines()
    for line in lines:
        line_word = line.split(",")
        cows[line_word[0]] = int(line_word[1])

    return cows


cows = load_cows("ps1_cow_data.txt")

# Problem 2


def greedy_cow(cows, limit):
    trip = []
    weight = 0
    for cow, w in cows.items():
        if w + weight <= limit:
            trip.append(cow)
            weight += w
    return trip


def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # cows = load_cows('ps1_cow_data.txt')
    cows_copy = dict(
        sorted(cows.items(), key=lambda item: item[1], reverse=True))
    trips = []
    while len(cows_copy) > 0:
        trip = greedy_cow(cows_copy, limit)
        trips.append(trip)
        for cow in trip:
            del cows_copy[cow]
    return trips


print(greedy_cow_transport(cows))

# Problem 3


def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    least_trip = [i for i in range(len(cows) + 1)]
    result = []
    for p in partitions(cows):
        check = True
        for trip in p:
            sum = 0
            for cow in trip:
                sum += cows[cow]
            if sum > 10:
                check = False
        if check and len(p) < len(least_trip):
            least_trip = p
    for trip in least_trip:
        result.append(list(trip))
    return result


print(brute_force_cow_transport(cows))
# Problem 4


def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    start = time()
    greedy_cow_transport(cows)
    end = time()
    brute_force_cow_transport(cows)
    end2 = time()
    print(f'time excute greedy algorithms is {1000*(end-start)} ms')
    print(f'time excute brute force algorithms is {1000*(end2-end)} ms')


compare_cow_transport_algorithms()
