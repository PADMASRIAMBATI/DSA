class Mobile{
    String brand;
    int price;
    static String name;

    //Constructor
    public Mobile(){
        brand = ""; //default values
        price = 200; //default values
    }

    static{
        name = "Mobile";
    }

    public void show(){
        System.out.println(brand+" : "+price+" : "+name);
    }
}
public class StaticMethod {
    public static void main(String[] args) {
        Mobile obj1 = new Mobile();
        obj1.brand = "Apple";
        obj1.price = 2000;

        obj1.show();
    }
}
