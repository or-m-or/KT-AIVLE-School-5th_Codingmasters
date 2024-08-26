'''
Type : 
'''
import sys
from itertools import combinations
from itertools import permutations
readline = sys.stdin.readline


def solution(K, houses):
    # (1, 1) is the restaurant's location
    restaurant = (1, 1)

    def manhattan_distance(p1, p2):
        return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

    # Generate all combinations of houses where Cheolsu delivers exactly K houses
    min_time = float('inf')

    for house_combination in combinations(houses, K):
        # We need to consider all permutations of visiting these houses because
        # the order in which houses are visited affects the total distance traveled.
        # We use brute-force here since K <= 8, thus at most factorial(8) permutations,
        # which is manageable.

        # Iterate over all permutations of the K houses
        for permutation in permutations(house_combination):
            # Calculate the distance for this permutation
            # Start at the restaurant, visit all houses in the permutation, and return to restaurant
            total_distance = 0
            current_location = restaurant

            # Visit each house in the permutation
            for house in permutation:
                total_distance += manhattan_distance(current_location, house)
                current_location = house

            # Return to the restaurant
            total_distance += manhattan_distance(current_location, restaurant)

            # Update the minimum time if the current distance is less
            min_time = min(min_time, total_distance)

    return min_time


if __name__ == "__main__":
    N, K = map(int, readline().split())
    houses = [tuple(map(int, readline().split())) for _ in range(N)]

    print(solution(K, houses))
