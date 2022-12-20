class Solution {
public:

    void dfs(vector<vector<int>> &rooms, int s, vector<bool> &record){
        record[s] = true;
        for(int i = 0; i < rooms[s].size(); i++){
            if(!record[rooms[s][i]]){
                dfs(rooms, rooms[s][i], record);
            }
        }
    }

    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int i, n=rooms.size();
        vector<bool> record(n, false);
        dfs(rooms, 0, record);
        for(i = 0; i < n; i++){
            if(!record[i]){
                return false;
            }
        }
        return true;
    }
};
