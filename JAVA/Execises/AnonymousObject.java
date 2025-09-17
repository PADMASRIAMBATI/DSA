class A{
    public A(){
        System.out.println("In Constructor");
    }
    public void show(){
        System.out.println("In method");
    }
}
public class AnonymousObject {
    public static void main(String[] args) {
        new A(); // Anonymous object

        System.out.println("**********");

        new A().show(); //Anonymous object with method call
    }
}
