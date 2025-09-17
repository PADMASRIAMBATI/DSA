package AcessModifiers.Default;
class C{
    int b= 1;
}

public class Default {
    public static void main(String[] args) {
        B obj = new B();
        System.out.println("Same Package without sub class: "+obj.a);
        System.out.println("Same Package Sub class: "+obj.getx());

        C obj1 = new C();
        System.out.println("Same class: "+obj1.b);
    }
}
