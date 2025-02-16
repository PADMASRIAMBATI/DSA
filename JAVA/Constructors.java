class Human{
    private String name;
    private int age;

    public Human(){ // default Constructor
        name = "Padmasri";
        age = 20;
    }
    public Human(String n,int a){ //parameterized Constructor
        name = n;
        age = a;
    }

    public void setName(String name){
        this.name = name;
    }
    public void setAge(int age){
        this.age = age;
    }
    public int getAge(){
        return age;
    }
    public String getName(){
        return name;
    }
    
}
public class Constructors {
    public static void main(String[] args) {
        Human obj = new Human();
        System.out.println(obj.getName()+" : "+obj.getAge()); //it prints default constructor

        obj.setName("Tinku");
        obj.setAge(8);
        System.out.println(obj.getName()+" : "+obj.getAge()); 

        Human obj1 = new Human("Devi",32);
        System.out.println(obj1.getName()+" : "+obj1.getAge()); //it prints parameterized Constructor
    }
}
