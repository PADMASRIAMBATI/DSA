package AcessModifiers.Public;

class B {
    public int y = 2;
}

class C extends B{
    public int getx(){
        return y;
    }
}
