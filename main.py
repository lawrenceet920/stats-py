# Ethan Lawrence
# Oct 28 2024
# Min-Max-Sum

# Quiz Scores
quiz_scores = [75, 80, 85, 90, 95, 100]
quiz_mean = sum(quiz_scores) / len(quiz_scores)
print(f'The average score for the quiz is {quiz_mean:.2f}')


# Driving Distances
distances = []
destinations = []
# City 1
distances.append(799)
destinations.append('Kansas City')
# City 2
distances.append(685)
destinations.append('Nashville')
# City 3
distances.append(853.7)
destinations.append('New York City')
# City 4
distances.append(442)
destinations.append('Toronto')
# City 5
distances.append(711.2)
destinations.append('Ottawa')

short_index = distances.index(min(distances))
long_index = distances.index(max(distances))
average_dist = sum(distances) / len(distances)

print(f'The avalable destinations for this calculation are: {destinations}')
print(f'The shortest trip from Traverce City is to {destinations[short_index]} ({min(distances)} miles)')
print(f'The longest trip from Traverce City is to {destinations[long_index]}. ({max(distances)} miles)')
print(f'The average trip driving distance is between Traverse City and the five destinations is {average_dist:.2f} miles')