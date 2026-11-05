public class Sajeda {
    public static void main(String[] args) {
        String developer = "AXSOS Academy is great!";
        int length = developer.length();
        // System.out.println( "String Length is : " + length );

        String string1 = "My name is ";
        String string2 = "Shatha";
        String string3 = string1.concat(string2);
        System.out.println(string3);
        // string1.concat

        String developer1 = String.format("Hi %s, you owe me $%.2f !", "Sara", 25.0);
        System.out.println(developer1);
        // Will print out Hi Sara, you owe me $25.00 !
        // Where %s is expecting a string
        // And %.2f is expecting a float data type. The value 2 will just place two values to right of the decimal point.

        String ninja = "Welcome to AXSOS Academy!";
        int a = ninja.indexOf("AXSOS"); // a is 11
        int b = ninja.indexOf("ca"); // b is 18
        int c = ninja.indexOf("pizza"); // c is -1, "pizza" is not found
        System.out.println(a);

        long start = System.currentTimeMillis();
        int sum = 0;
        for (int i = 0; i < Integer.MAX_VALUE; i++) {
            sum += i;
        }
        System.out.println("Sum: " + sum);
        long end = System.currentTimeMillis();
        double total = (double) (end - start) / 1000;
        System.out.println("Time of execution: " + total + " seconds");
    }
}
