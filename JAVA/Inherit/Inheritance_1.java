public class Inheritance_1 {
    public static void main(String args[]) {
        VeryAdvCalc obj = new VeryAdvCalc();

        int n1 = obj.add(5,8);
        int n2 = obj.sub(10,6);

        System.out.println("Addition: "+n1+" and Subraction: "+n2);

        int n3 = obj.multi(5,8);
        int n4 = obj.div(10,6);

        System.out.println("Multiplication: "+n3+" and Division: "+n4);

        double n5 = obj.power(2,2);

        System.out.println("Powers: "+n5);
    }
}
