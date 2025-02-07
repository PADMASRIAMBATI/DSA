public class MultiDimensionalArray {
    public static void main(String[] args) {
        int n[][][] = new int[3][4][5];

        for(int i =0;i<3;i++){
            for(int j=0;j<4;j++){
                for(int k=0;k<5;k++){

                    n[i][j][k] = (int)(Math.random() * 10);
                }
            }
        }

        for(int num[][] : n){
            for(int num1[] : num){
                for(int num2 : num1){
                    System.out.print(num2+" ");
                }
                System.out.println();
            }
            System.out.println();
        }

        int a[] = new int[4];
        a[0] = 10;
        a[1] = 2;
        a[2] = 5;
        a[3] = 6;

        for(int p=0;p<a.length;p++){
            System.out.print(a[p]+" ");
        }
        System.out.println();

    }
}
