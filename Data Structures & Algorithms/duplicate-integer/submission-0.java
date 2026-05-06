class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> dupeCheck = new HashSet<>();

        for(int i = 0; i < nums.length; ++ i) {
            dupeCheck.add(nums[i]);
        }

        int dupeSize = dupeCheck.size();
        int numsLen = nums.length;

        if(dupeSize < numsLen){
            return true;
        }
        else {
            return false;
        }
    }
}