# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 22:48:03 2024

@author: dasvestas
"""
#create the data structure 
class Member:
    def __init__(self, memberid):
        self.memberid = memberid
        self.followers = set()
        self.following = set()
        self.likes = {}  # {memberid: number_of_likes}
        self.comments = {}  # {memberid: number_of_comments}
    
    def follow(self, member):
        self.following.add(member)
        member.followers.add(self)
    
    def like(self, member, num_likes=1):
        if member.memberid in self.likes:
            self.likes[member.memberid] += num_likes
        else:
            self.likes[member.memberid] = num_likes
    
    def comment(self, member, nocomments=1):
        if member.memberid in self.comments:
            self.comments[member.memberid] += nocomments
        else:
            self.comments[member.memberid] = nocomments

class SocialNetwork:
    def __init__(self):
        self.members = {}
    
    def add_member(self, memberid):
        if memberid not in self.members:
            self.members[memberid] = Member(memberid)
    
    def get_member(self, memberid):
        return self.members.get(memberid)
    
    def follow(self, follower_id, followeeid):
        follower = self.get_member(follower_id)
        followee = self.get_member(followeeid)
        if follower and followee:
            follower.follow(followee)
    
    def like(self, likerid, likee_id, num_likes=1):
        liker = self.get_member(likerid)
        likee = self.get_member(likee_id)
        if liker and likee:
            liker.like(likee, num_likes)
    
    def comment(self, commenterid, commenteeid, nocomments=1):
        commenter = self.get_member(commenterid)
        commentee = self.get_member(commenteeid)
        if commenter and commentee:
            commenter.comment(commentee, nocomments)

#engagemnt rate

def calculate_engagement_rate(member):
    totallikes = sum(member.likes.values())
    totalcomments = sum(member.comments.values())
    totalfollowers = len(member.followers)
    if totalfollowers == 0:
        return 0
    return (totallikes + totalcomments) / totalfollowers * 100

def get_engagement_rates(network):
    engagementrates = {}
    for memberid, member in network.members.items():
        engagementrates[memberid] = calculate_engagement_rate(member)
    return engagementrates

from collections import deque

#shortest path 

def shortest_path(network, startid, endid):
    startmember = network.get_member(startid)
    endmember = network.get_member(endid)
    if not startmember or not endmember:
        return None
    
    queue = deque([(startmember, [startmember.memberid])])
    visited = set()
    
    while queue:
        currentmember, path = queue.popleft()
        if currentmember.memberid == endid:
            return path
        
        visited.add(currentmember)
        
        for follower in currentmember.following:
            if follower not in visited:
                queue.append((follower, path + [follower.memberid]))
    
    return None

def calculate_influence(ma, mb):
    totalengagement = calculate_engagement_rate(ma)
    if totalengagement == 0:
        return 0
    likes_to_b = ma.likes.get(mb.memberid, 0)
    comments_to_b = ma.comments.get(mb.memberid, 0)
    return (likes_to_b + comments_to_b) / totalengagement


#highest engageemnt 

def highest_engagement_path(network, startid, endid):
    startmember = network.get_member(startid)
    endmember = network.get_member(endid)
    if not startmember or not endmember:
        return None
    
    best_path = None
    highest_engagement = 0
    
    def dfs(currentmember, path, engagement):
        nonlocal best_path, highest_engagement
        if currentmember.memberid == endid:
            if engagement > highest_engagement:
                highest_engagement = engagement
                best_path = path
            return
        
        for follower in currentmember.following:
            if follower.memberid not in path:
                new_engagement = engagement + calculate_influence(currentmember, follower)
                dfs(follower, path + [follower.memberid], new_engagement)
    
    dfs(startmember, [startmember.memberid], 0)
    return best_path

# Example usage
network = SocialNetwork()
network.add_member(1)
network.add_member(2)
network.add_member(3)
network.follow(1, 2)
network.follow(2, 3)
network.like(1, 2, 5)
network.comment(1, 2, 2)
network.like(2, 3, 3)

engagementrates = get_engagement_rates(network)
print("Engagement Rates:", engagementrates)

shortest_path_result = shortest_path(network, 1, 3)
print("Shortest Path:", shortest_path_result)

highest_engagement_path_result = highest_engagement_path(network, 1, 3)
print("Highest Engagement Path:", highest_engagement_path_result)

