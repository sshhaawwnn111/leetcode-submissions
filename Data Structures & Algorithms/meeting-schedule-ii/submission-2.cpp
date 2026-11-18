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
    int minMeetingRooms(vector<Interval>& intervals) {
        vector<vector<int>> times;
        for(const auto& i : intervals){
            times.push_back({i.start, 1});
            times.push_back({i.end, -1});
        }
        sort(times.begin(), times.end(), 
            [](auto& a, auto& b){
                return a[0] == b[0] ? a[1] < b[1] : a[0] < b[0];
            });

        int count = 0, res = 0;
        for(auto& t : times){
            count += t[1];
            res = max(res, count);
        }
        return res;
    }
};
