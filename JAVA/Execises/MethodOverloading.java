class Calculator{
    public int add(int n1, int n2){
        return n1 + n2;
    }
    public int add(int n1, int n2, int n3){
        return n1 + n2 + n3;
    }
    public double add(double n1, int n2){
        return n1 + n2;
    }
}
public class MethodOverloading {
    public static void main(String[] args) {
       Calculator obj = new Calculator();
       double r = obj.add(2.2345678, 6);
       System.out.println(r);
    }
}
