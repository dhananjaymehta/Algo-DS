"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
Given 4 points: (1,2), (3,6), (0,0), (1,3).

The maximum number is 3.
"""

"""
# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
# @param {int[]} points an array of point
# @return {int} an integer
"""
from fractions import gcd


def maxPoints(points):
    map_points={}   # key : slope
    l=len(points)  # total points

    for i in range(l):
        for j in range(i+1,l):
            x=abs(points[i][0]-points[j][0])
            y=abs(points[i][1]-points[j][1])
            slope = gcd(x,y)
            x=int(x/slope)
            y = int(y/ slope)
            #print(slope, x,y,points[i],points[j])
            if (x,y) in map_points:
                if i<=map_points[(x,y)][1]:
                    print(map_points[(x, y)])
                    map_points[(x,y)][0]+=1
            else:
                map_points[(x,y)]=[1,i]   # [0]: count and [1]: index
    print(sorted(map_points.values()))


def maxPoints2(self, points):
    # Write your code here
    len_points = len(points)
    if len_points <= 1:
        return len_points
    max_count = 0
    for index1 in range(0, len_points):
        p1 = points[index1]
        gradients = {}
        infinite_count = 0
        duplicate_count = 0
        for index2 in range(index1, len_points):
            p2 = points[index2]
            dx = p2.x - p1.x
            dy = p2.y - p1.y
            if 0 == dx and 0 == dy:
                duplicate_count += 1
            if 0 == dx:
                infinite_count += 1
            else:
                g = float(dy) / dx
                gradients[g] = (gradients[g] + 1 if gradients.has_key(g) else 1)
        if infinite_count > max_count:
            max_count = infinite_count
        for k, v in gradients.items():
            v += duplicate_count
            if v > max_count:
                max_count = v
    return max_count
#sol=Solution()
P=[[1,2],[3,6],[0,0],[1,3],[2,4]]
maxPoints(points=P)