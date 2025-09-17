package DynamicMethodDispatch;
class A{
public void show(){
    System.out.println("In A Show");
}
}
class B extends A{
    public void show(){
        System.out.println("In B show");
}
}
class C extends A{
    public void show(){
        System.out.println("In C show");
    }
}

public class RuntimePolymorphism {
    public static void main(String[] args) {
        A obj = new A();
        obj.show();

        obj = new B();
        obj.show();
        
        obj = new C();
        obj.show();
    }
}
