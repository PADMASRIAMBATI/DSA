public class Array {
    public static void main(String[] args) {
        int nums[] = {1,2,3,4,5};
        nums[2] = 6;
        System.out.println(nums[2]);

        System.out.println("**********");

        int num2[] = new int[5];
        num2[0] = -1;
        num2[1] = 5;
        num2[2] = 7;
        num2[3] = 9;
        num2[4] = -3;
        for(int i=0;i<5;i++){
            System.out.println("num2["+i+"] = "+num2[i]);
        }

        System.out.println("***** Two Dimensional Array*****");

        //Two Dimensional Array
        int num[][] = {{3,8,6,1}, {11,12,2,9}, {4,10,7,5}};
        for(int i=0;i<3;i++){
            for(int j=0;j<4;j++){
                System.out.print(num[i][j]+" ");
            }
            System.out.println();
        }

        System.out.println("**********");

        int num1[][] = new int[3][4];
        for(int i=0;i<3;i++){
            for(int j=0;j<4;j++){
                num1[i][j] = (int)(Math.random() * 10);
                System.out.print(num1[i][j]+" ");
            }
            System.out.println();
        }

        System.out.println("***** Enhance For loop *****");
        
        //Enhance For loop
        for(int n[] : num1){
            for(int m : n){
                System.out.print(m+" ");
            }
            System.out.println();
        }

        

    }
}
