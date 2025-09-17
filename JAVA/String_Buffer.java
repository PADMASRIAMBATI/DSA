public class String_Buffer {
    public static void main(String[] args) {
        StringBuffer n = new StringBuffer();
        System.out.println("Empty Buffer Capacity: "+n.capacity());

        StringBuffer num = new StringBuffer("Tinku");
        System.out.println("Capacity of Buffer: "+num.capacity());
        System.out.println("Length of Buffer: "+num.length());

        num.append(" Ambati");
        System.out.println("Append: "+num);

        System.out.println("Data Type: "+num.getClass().getSimpleName()); // to know which data type
        //We cannot store or assign strinbuffer to string 
        //for that we have to convert stringbuffer to string
        String str = num.toString();
        System.out.println("Data Typr: "+str.getClass().getSimpleName()); // to know which data type

        System.out.println(num.deleteCharAt(9)); //to delete a character 

        System.out.println(num.insert(9,"a"));

        num.ensureCapacity(100); //to put a capacity to buffer
        System.out.println(num);

        num.setLength(5);
        System.out.println(num);


    }
}
