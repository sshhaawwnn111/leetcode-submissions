"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x : x.start)

        prevEnd = 0
        for t in intervals:
            if t.start < prevEnd:
                return False
            else:
                prevEnd = t.end
        return True
        