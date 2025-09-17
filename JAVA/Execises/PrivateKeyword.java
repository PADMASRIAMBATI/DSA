class Human{
    private String name ="Padmasri";
    private int age = 25;

    public int getAge(){
        return age;
    }
    public String getName(){
        return name;
    }
}

class Human_1{
    private String name_1;
    private int age_1;
    
    public void setAge_1(int a){ // we can use any name for method declaration
        age_1 =a;
    }
    public int getAge_1(){
        return age_1;
    }
    public void setName_1(String b){
        name_1 = b;
    }
    public String getName_1(){
        return name_1;
    }
}

class PrivateKeyword{
    public static void main(String[] args) {
        Human obj = new Human();
        System.out.println(obj.getName()+" : "+obj.getAge());

        Human_1 obj1 = new Human_1();
        obj1.setName_1("Tinku");
        obj1.setAge_1(23);
        System.out.println(obj1.getName_1()+" : "+obj1.getAge_1());

    }
}