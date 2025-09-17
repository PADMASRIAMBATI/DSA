class A{
    public A(){
        System.out.println("A class constructor");
    }
    public A(int a){
        System.out.println("A class parameter constructor");
    }

}
class B extends A{
    public B(){
        super(9);
        System.out.println("B class constructor");
    }
    public B(int a){
        super(a);
        System.out.println("B class paramaeter constructor");
    }
}

class C{
    public C(){
        System.out.println("C class constructor");
    }
    public C(int h){
        System.out.println("C class paramaeter constructor");
    }
}
class D extends C{
    public D(){
        System.out.println("D class constructor");
    }
    public D(int h){
        this();
        System.out.println("D class paramaeter constructor");
    }
}

public class ThisSuperKeyword {
    public static void main(String[] args) {
        B obj = new B();

        System.out.println("**********");

        D obj1 = new D(3);

    }
}
