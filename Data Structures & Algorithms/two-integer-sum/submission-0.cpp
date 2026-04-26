class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m;

        for(int i=0; i < nums.size(); i++){
            if(m.find(nums[i]) == m.end()){
                m[target - nums[i]] = i;
            }
            else{
                return {m[nums[i]], i};
            }
        }

        // for(auto it: m){
        //     cout<<it.first<<" "<<it.second<<endl;
        // }
        // return {0, 1};
    }
};
