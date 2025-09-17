class Solution{
    public void reverse(int x){
        int INT_MAX = Integer.MAX_VALUE;
        int INT_MIN = Integer.MIN_VALUE;
        int result = 0;

        while(x!=0){
            int digit = x%10; // iteration 3 , 2 , 1
            x = x/10; // iteration 12 , 1 , 0
        

            if(result > INT_MAX || (result == INT_MAX/10 && digit > 7)){
                System.out.println(0);
            }
            if(result < INT_MIN || (result == INT_MIN/10 && digit < -8)){
                System.out.println(0);
            }


            System.out.println(result = result*10+digit); 
        }
        
    }
}
public class reverse {
    public static void main(String[] args) {
        Solution obj = new Solution();
        obj.reverse(-123);
    }
}

/*Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1*/
