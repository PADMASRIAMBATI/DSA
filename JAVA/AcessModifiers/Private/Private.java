package AcessModifiers.Private;

class A{
    private int x = 1;
    public int getx(){
        return x;
    }
}

public class Private {
    public static void main(String[] args) {
        
        A obj = new A();
        System.out.println("Same class: "+obj.getx());

    }
    
}
