"""Geek wants to scan N documents using two scanners. If S1 and S2 are the time taken by the scanner 1 and scanner 2 to scan a single document, find the minimum time required to scan all the N documents.


Example 1:

Input: 
S1 = 2, S2 = 4, N = 2
Output: 4
Explaination: Here we have two possibilities. 
Either scan both documents in scanner 1 or
scan one document in each scanner. 
In both the cases time required is 4.
 

Example 2:

Input: 
S1 = 1, S2 = 3, N = 2
Output: 2
Explaination: Here the optimal approach is to 
scan both of them in the first scanner.
 

Your Task:
You do not need to read input or print anything. Your task is to complete the function minTime() which takes S1, S2 and N as input parameters and returns the minimum tme required to scan the documents.

 

Expected Time Complexity: O(logN)
Expected Auxiliary Space: O(1)

 

Constraints:
1 ≤ S1, S2, N ≤ 106
1 ≤ S1*N, S2*N ≤ 109

"""

class Solution{
public:
    int minTime(int S1, int S2, int N){
        int a = S1, b = S2;
        if(a > b)
            swap(a, b);
        int low = 0, high = N, mid, mini = b*N;
        while(low <= high){
            mid = low +(high-low)/2;
            mini = min(mini , max(mid*a , (N - mid)*b));
            if(mid*a <= (N - mid)*b)
                low = mid + 1;
            else
                high = mid - 1;
        }
        return mini;
    }
};
