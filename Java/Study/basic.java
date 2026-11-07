public class basic {
    public static void main(String[] args) {
        int temperature = 85;
        boolean isCloudy = true;

        if(temperature < 40 && isCloudy){ //skip
            System.out.println("It might snow.");
            }
        else if(isCloudy){
            System.out.println("It might rain.");
            }
        else{
            System.out.println("We should have nice weather today.");
        }
    }
}
