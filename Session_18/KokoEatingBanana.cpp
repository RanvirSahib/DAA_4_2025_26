class Solution {
public:

    bool ispos(vector<int> &piles, int mid, int h){
        long long count = 0;
        for (int i = 0; i < piles.size(); i++){
            //count+= (piles[i]+mid -1)/mid;

            count += piles[i] /mid; 
            if (piles[i] % mid != 0) count++;

           
        }
        return count <= h;
    }
    int minEatingSpeed(vector<int>& piles, int h) {
        
        int l = 1;
        int r = *max_element(piles.begin(),piles.end());
        
        int ans = 0;

        while ( l <= r){

            int mid = (l+r) / 2;
            if(ispos(piles, mid, h)){
                ans = mid;
                r = mid - 1;
            }
            else l = mid + 1;
        }
        return ans;

    }
};