package Casting;

class A{
      public void show1(){
        System.out.println("In A show");
      }                                                                                                       
}
class B extends A{
    public void show2(){
        System.out.println("In B show");
    }
}
public class UpCasting {
    public static void main(String[] args) {

        // Up Casting 
        A obj = (A) new B();
        obj.show1(); 

        // Down Casting
        B obj1 = (B) obj;
        obj1.show2();

    }
}
