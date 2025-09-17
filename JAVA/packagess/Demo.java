package packagess;
import packagess.tools.*;
public class Demo {
    public static void main(String[] args) {
        Calc obj = new Calc();
        AdvCalc obj1 = new AdvCalc();

        int n1 = obj.add(1,1);
        int n2 = obj1.mult(2,2);

        System.out.println("Addition: "+n1);
        System.out.println("Multipication: "+n2);
    }
}
