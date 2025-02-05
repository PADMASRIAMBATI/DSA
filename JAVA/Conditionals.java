public class Conditionals {
    public static void main(String[] args) {
        int a = 1;
        if(a == 1)
            System.out.println("IF Block");
        else
            System.out.println("ELSE Block");

        int x = 13;
        int y = 7;
        if(x > y)
        {
            System.out.println(x +" is greatest number");
            System.out.println("Thank You");
        }
        else
            System.out.println(y +" is greatest number");
        

        //Ternary operator
        int n = 14;
        int m = 5;
        int result = 0;
        result = n>m ? n : m;
        System.out.println("Ternary operator: "+result);

        int b = 12;
        int c = 19;
        int d = 23;
        if(b > c && b > d)
            System.out.println(b+" is greatest number");
        else if(c > d)
            System.out.println(c+" is greatest number");
        else
            System.out.println(d +" is greatest number");

        
        if(b > c){
            if(b > d){
                System.out.println(b+" is greatest number");
            }
        }
            
        else if(c > b){
            if(c > d){
                System.out.println(c+" is greatest number");
            }
            else{
                System.out.println(d+" is greatest number");
            }
        }
        else{
            System.out.println(d+" is greatest number");
        }
            
    }
}
    

