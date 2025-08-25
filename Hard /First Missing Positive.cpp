class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
   int n=nums.size();
   bool contains1=false;
   for(int i=0;i<n;i++){
        if(nums[i]==1) contains1=true;
    if(nums[i]<=0 || nums[i]>n) nums[i]=1;

   }
   if(contains1==false) return 1;

   for(int i=0;i<n;i++){
    int val=abs(nums[i]);
    int index=val-1;
    if(nums[index]<0) continue;
    nums[index]*=-1;
   }
   for(int i=0;i<n;i++){
    if(nums[i]>0) return i+1;
   }
return n+1;
    }
};
