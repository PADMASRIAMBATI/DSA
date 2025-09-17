package ObjectClass;
class Laptop{
    String model;
    int price;

    public String toString(){
        return model+" : "+price;
    }
}

class Laptop1{
    String model;
    int price;

}




public class ToString {
    public static void main(String[] args) {
        Laptop obj = new Laptop();
        obj.model = "Samsung";
        obj.price = 5000;
        System.out.println(obj.toString()); 
        System.out.println(obj); // it calls by default .toString()

        Laptop1 obj1 = new Laptop1();
        obj1.model = "Samsung";
        obj1.price = 5000;
        System.out.println("Hex String: "+obj1.toString()); 
        System.out.println("Hex String: "+obj1); // it calls by default .toString()

        

    }
}
