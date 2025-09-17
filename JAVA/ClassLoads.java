class Mobile{
    static{
        System.out.println("Static Block");
    }
}
public class ClassLoads {
    public static void main(String[] args) throws ClassNotFoundException
    {
        Class.forName("Mobile");
    }
}
