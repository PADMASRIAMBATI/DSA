public class typeConversionCasting {
    public static void main(String[] args) {
        byte b = 127;
        int a = b;
        System.out.println(a);

        int u= 127;
        byte k = (byte) u;
        System.out.println(k);

        //modulus operation
        //257 % byte range 256 = 1
        int o = 257;
        byte p = (byte) o;
        System.out.println(p);

        float g = 5.9f;
        int d = (int) g;
        System.out.println(d);

        //Type Promotion
        byte l = 10;
        byte s =30;
        int result = l * s;
        System.out.println(result);
    }
}
