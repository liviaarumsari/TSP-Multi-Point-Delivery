from typing import DefaultDict

INT_MAX = 2147483647

# Function to find the minimum cost path for all the paths
def findMinRoute(tsp, isBack):
	sum = 0
	counter = 0
	j = 0
	i = 0
	min = INT_MAX
	visitedRouteList = DefaultDict(int)

	# Starting from the 0th indexed city i.e., the first city
	visitedRouteList[0] = 1
	route = [0] * (len(tsp) - 1)

	# Traverse the adjacency matrix tsp[][]
	while i < len(tsp) and j < len(tsp[i]):

		# Corner of the Matrix
		if counter >= len(tsp[i]) - 1:
			break

		# If this path is unvisited then and if the 
		# cost is less then update the cost
		if j != i and (visitedRouteList[j] == 0):
			if tsp[i][j] < min:
				min = tsp[i][j]
				route[counter] = j + 1

		j += 1

		# Check all paths from the ith indexed city
		if j == len(tsp[i]):
			sum += min
			min = INT_MAX
			visitedRouteList[route[counter] - 1] = 1
			j = 0
			i = route[counter] - 1
			counter += 1
	
	# Update the ending city in array from city which was last visited
	# Update the route to go back to the starting point
	if (isBack):
		i = route[counter - 1] - 1
		route += [1]
		sum += tsp[i][0]

	return sum, route

