//Passing Argument as object
class Human{
    private String name;
    private int age;
    public void setName(String name,Human obj){
        obj.name = name;
    }
    public void setAge(int age,Human obj){
        obj.age = age;
    }
    public String getName(){
        return name;
    }
    public int getAge(){
        return age;
    }

}

//Using "This" keyword
class Human_1{
    String name;
    int age;
    public void setName_1(String name){
        this.name = name;
    }
    public void setAge_1(int age){
        this.age = age;
    }
    public String getName_1(){
        return name;
    }
    public int getAge_1(){
        return age;
    }

}
public class ThisKeyword {
    public static void main(String[] args) {
        Human obj = new Human();
        obj.setName("Padmasri",obj);
        obj.setAge(17,obj);
        System.out.println(obj.getName()+" : "+obj.getAge());

        Human_1 obj1 = new Human_1();
        obj1.setName_1("Tinku");
        obj1.setAge_1(15);
        System.out.println(obj1.getName_1()+" : "+obj1.getAge_1());

    }
}
