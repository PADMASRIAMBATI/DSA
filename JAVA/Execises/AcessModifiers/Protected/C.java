package AcessModifiers.Protected;

public class C {
    protected int y = 2;
}

class D extends C{
    public int getx(){
        return y;
    }
}
