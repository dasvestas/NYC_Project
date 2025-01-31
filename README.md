# NYC_Project
 Assesment 002 Data Structure and Algorithms
# X2 Social Network

## Description
This project implements a simplified social network platform named X2. It allows members to follow other members, like posts, and comment on posts. The platform calculates engagement rates and finds paths between members based on different criteria.

## Features
- **Follow members**: Members can follow other members.
- **Like and comment**: Members can like and comment on posts of the members they follow.
- **Engagement rate**: Calculate the engagement rate of each member.
- **Shortest path**: Find the shortest path between two members.
- **Highest engagement path**: Find the path with the highest engagement between two members.

## Installation
1. Clone the repository or download the zip file.
2. Python 
3. Navigate to the project directory.

## Usage
1. Run the `pyhton code.py` file

## Example
Here's an example of how to use the `pyhton code.py` class:
```python
network = SocialNetwork()
network.add_member(1)
network.add_member(2)
network.add_member(3)
network.follow(1, 2)
network.follow(2, 3)
network.like(1, 2, 5)
network.comment(1, 2, 2)
network.like(2, 3, 3)

engagement_rates = get_engagement_rates(network)
print("Engagement Rates:", engagement_rates)

shortest_path_result = shortest_path(network, 1, 3)
print("Shortest Path:", shortest_path_result)

highest_engagement_path_result = highest_engagement_path(network, 1, 3)
print("Highest Engagement Path:", highest_engagement_path_result)
