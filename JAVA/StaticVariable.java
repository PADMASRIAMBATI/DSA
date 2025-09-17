class Mobile{
    static String name;
    String brand;
    int price;

    public void show(){
    System.out.println(brand+" : "+price+" : "+name);
    }
}
public class StaticVariable {
    public static void main(String[] args) {
        Mobile obj1 = new Mobile();
        Mobile.name = "SmartPhone";
        obj1.brand = "Apple";
        obj1.price = 1500;

        Mobile obj2 = new Mobile();
        Mobile.name = "SmartPhone";
        obj2.brand = "Samsung";
        obj2.price = 1700;
        
        Mobile.name = "Phone";
        
        obj1.show();
        obj2.show();
    }
}
