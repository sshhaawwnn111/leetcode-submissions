/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    bool canAttendMeetings(vector<Interval>& intervals) {
        sort(intervals.begin(), intervals.end(),
            [](Interval& a, Interval& b){
                return a.start < b.start;
            });
        int curEnd = 0;
        for(auto& interval : intervals){
            if(interval.start < curEnd){
                return false;
            }
            curEnd = interval.end;
        }
        return true;
    }
};
