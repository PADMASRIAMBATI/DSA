public class Operaters {
    public static void main(String[] args) {
        int num1 = 42;
        int num2 = 8;
        int result = num1 + num2;
        System.out.println("Addition:"+result);

        int result1 = num1 - num2;
        System.out.println("Subraction:"+result1);

        int result2 = num1 * num2;
        System.out.println("Multiplication:"+result2);

        int result3 = num1 / num2;
        System.out.println("Division:"+result3);

        int result4 = num1 % num2;
        System.out.println("Reminder:"+result4);

        //other
        //increment
        num2 += 3;
        System.out.println("Increment by 3 is :"+num2);

        int inc1 = num2++;
        System.out.println("Post Increment:"+inc1);
        System.out.println(inc1++);

        int num3 = 11;
        int inc2 = ++num3;
        System.out.println("Pre Increment:"+inc2);
        System.out.println(++inc2);

        //Decrement
        num2 -= 3;
        System.out.println("Decrement by 3 is :"+num2);

        int dec1 = num2--;
        System.out.println("Post Increment:"+dec1);
        System.out.println(dec1--);

        int num4 = 9;
        int dec2 = ++num4;
        System.out.println("Pre Increment:"+dec2);
        System.out.println(++dec2);
        
        //comparsion operator
        int x = 6;
        int y = 5;
        boolean a1 = x > y;
        System.out.println("Comparsion Operator :"+a1);

        boolean a2 = x < y;
        System.out.println("Comparsion Operator :"+a2);

        boolean a3 = x >= y;
        System.out.println("Comparsion Operator :"+a3);

        boolean a4 = x <= y;
        System.out.println("Comparsion Operator :"+a4);

        boolean a5 = x == y;
        System.out.println("Comparsion Operator :"+a5);

        boolean a6 = x != y;
        System.out.println("Comparsion Operator :"+a6);

        //Logical operators
        boolean b1 = x > y && x != y;
        System.out.println("Logical Operator :"+b1);

        boolean b2 = x > y && x < y;
        System.out.println("Logical Operator :"+b2);

        boolean b3 = x > y || x != y;
        System.out.println("Logical Operator :"+b3);

        boolean b4 = x < y || x == y;
        System.out.println("Logical Operator :"+b4);

        System.out.println("Logical Operator :"+ !b4);


    }
    
}
