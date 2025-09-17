public class Whileloop {
    public static void main(String[] args) {
        int i = 1;
        while(i<=4)
        {
            System.out.println("Hi "+i);
            i++;
        }
        System.out.println("Bye "+i);


        int a = 1;
        while(a<=3)
        {
            System.out.println("Hi "+a);
            int b = 1;
            while(b <= 2)
            {
                System.out.println("Hello "+b);
                b++;
            }
            a++;
        }
        System.out.println("Bye "+a);
    }
}
