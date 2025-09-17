public class ForEachloop {
    public static void main(String[] args) {
        int a[] = new int[4];
        a[0] = 9;
        a[1] = 5;
        a[2] = 8;
        a[3] = 7;

        for(int n : a){
            System.out.print(n + " ");
        }
        System.out.println();
    }
}
