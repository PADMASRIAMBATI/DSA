class Calculator
{
    public int add(int n ,int m)
    {
        int result = n + m ;
        return result;
    }
}

public class ReferenceObject {
    public static void main(String a[]) 
    {
        Calculator obj = new Calculator();
        int r = obj.add(1,2);
        System.out.println(r);
    }
}
