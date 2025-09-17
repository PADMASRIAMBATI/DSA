package AcessModifiers.Public;
import Public1.*;

class A{
    public int x = 1;
}

public class Public {
    public static void main(String a[]){
        A obj = new A(); //same class
        System.out.println("same class: "+obj.x);

        C obj1 = new C();
        System.out.println("sub class: "+obj1.y);
        System.out.println("same package without subclass: "+obj1.getx());

        E obj3 = new E();
        System.out.println("different package without subclass: "+obj3.b);
        System.out.println("different package with subclass: "+obj3.getx());
    }
}
