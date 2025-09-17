class Mobile{
    String brand;
    static String name;
    int price;

    public void show(){
        System.out.println(brand+" : "+price+" : "+name);
    }    

    public static void show1(Mobile obj){
        System.out.println(obj.brand+" : "+obj.price+" : "+name);
    }
}
public class StaticMethods_1 {
    public static void main(String[] args) {
        Mobile obj1 = new Mobile();
        obj1.brand = "Apple";
        obj1.price = 300;
        Mobile.name = "SmartPhone";

        Mobile obj2 = new Mobile();
        obj2.brand = "Samsung";
        obj2.price = 400;
        Mobile.name = "SmartPhone";

        obj1.show();
        obj2.show();

        System.out.println("**********");
        
        Mobile.show1(obj1);
        Mobile.show1(obj2);
    }
}
