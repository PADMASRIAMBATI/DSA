class Computer{
    public void Playmusic(){
        System.out.println("Playing music...");
    }
    public String Getmepen(int cost){
        if(cost >= 10){
            return "pen";
        }
        return "no pen";
    }
}

public class Methods {
    public static void main(String[] args) {
        Computer obj = new Computer();
        obj.Playmusic();
        String a = obj.Getmepen(1);
        System.out.println(a);

    }
}
