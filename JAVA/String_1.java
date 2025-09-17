public class String_1 {
    public static void main(String[] args) {
        String name = new String("Padmasri");
        System.out.println(name);
        System.out.println(name.hashCode());

        System.out.println("Concatnation: "+"Hello "+name);
        System.out.println("Concatnation: "+name.concat(" Ambati"));
        System.out.println("Index: "+
        name.charAt(0));

        String n = "Tinku";
        n = n + " Ambati";
        System.out.println(n);

        String n1 = "Devi";
        String n2 = "Devi";
        System.out.println(n1 == n2);

        System.out.println(n);
    }
}
