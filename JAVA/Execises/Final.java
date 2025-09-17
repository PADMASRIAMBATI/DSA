final class Calc{
    public final void show(){
        System.out.println("Hii Padmasri");
    }
    public void add(int a,int b){
        System.out.println(a+b);
    }
}
// class AdvCalc extends Calc{
//     public void show(){
//         System.out.println("Hii Tinku");
// }
// }

public class Final {
    public static void main(String args[]) {
        final int num = 10;
        System.out.println("Final Variable: "+num);

        Calc obj = new Calc();
        obj.show();
        obj.add(5,4);
    }
}
