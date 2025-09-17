class Calender{
    int num = 5;
    public int add(int n1 , int n2){ // n1 and n2 are local variables
        System.out.println(num); //Instance also print in the method
        return n1 + n2;
    }
}
public class DataArea {
    public static void main(String[] args) {
        int data = 10;
        Calender obj = new Calender();
        int r = obj.add(3,4);
        System.out.println(r);
        System.out.println(data);
    }
}
