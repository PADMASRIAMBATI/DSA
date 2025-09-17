import tools.AdvCalc;

class Calc{
    public int add(int r1,int r2){
        return r1 + r2;
    }
    
}

class AdvCalc extends Calc{
    public int add(int n1,int n2){
        return n1  + n2 + 1;
    }
}
public class MethodOveridding {
    public static void main(String[] args) {
        AdvCalc obj = new AdvCalc();
        int p = obj.add(2,6);
        System.out.println(p);
    }
}
