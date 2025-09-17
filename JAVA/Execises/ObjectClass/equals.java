package ObjectClass;
class Laptop2{
    String model;
    int price;
    
    //It defaultly generates this code by using IDE
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + ((model == null) ? 0 : model.hashCode());
        result = prime * result + price;
        return result;
    }
    
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        Laptop2 other = (Laptop2) obj;
        if (model == null) {
            if (other.model != null)
                return false;
        } else if (!model.equals(other.model))
            return false;
        if (price != other.price)
            return false;
        return true;
    }

    public boolean equals(Laptop2 that)
    {
        return this.model.equals(that.model) && this.price == that.price;
    } 
         
}

public class equals {
    public static void main(String[] args) {
        Laptop2 obj = new Laptop2();
        obj.model="Apple";
        obj.price=2000;

        Laptop2 obj2 = new Laptop2();
        obj2.model="Apple"; //add 1 then it shows false
        obj2.price=2000;

        boolean result  = obj.equals(obj2);
        System.out.println(result);

    }
}
