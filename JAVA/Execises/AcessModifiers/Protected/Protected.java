package AcessModifiers.Protected;
import Protected1.*;
class A{
    protected int x = 10;
}
class B extends A{
    public int getx(){
        return x;
    }
}

public class Protected {
    public static void main(String[] args) {
        B obj = new B();
        System.out.println("Same class: "+obj.x);
        System.out.println("same package sub class: "+obj.getx());

        C obj1 = new C();
        System.out.println("Same package without sub class: "+obj1.y);

        F obj2 = new F();
        //System.out.println("Differnt package without sub class: "+obj2.a);
        System.out.println("different package with sub class: "+obj2.getx());
    }
}
