public class CafeJava {
    public static void main(String[] args) {
        // APP VARIABLES
        // Lines of text that will appear in the app. 
        String generalGreeting = "Welcome to Cafe Java, ";
        String pendingMessage = ", your order will be ready shortly";
        String readyMessage = ", your order is ready";
        String displayTotalMessage = "Your total is $";

        // Menu variables (add yours below)
        double mochaPrice = 3.5;
        double dripCoffee = 5.5;
        double latte = 7.5;
        double cappuccino = 8;
        // Customer name variables (add yours below)
        String customer1 = "Ahmad";
        String customer2 = "Sali";
        String customer3 = "Adam";

        // Order completions (add yours below)
        boolean isReadyOrderAhmad = true;
        boolean isReadyOrderSali = true;
        boolean isReadyOrderAdam = true;
        if (isReadyOrderSali){
            System.out.println(customer2 + pendingMessage);
        }
        if (isReadyOrderAhmad){
            System.out.println(customer1 + pendingMessage);
        }
        if (isReadyOrderAdam){
            System.out.println( customer3 + pendingMessage);
        }
    
        // APP INTERACTION SIMULATION (Add your code for the challenges below)
        // Example:
        System.out.println(generalGreeting + customer1); // Displays "Welcome to Cafe Java, Shatha"
        // ** Your customer interaction print statements will go here ** //
        boolean ready = true;
        if (ready == true){
            System.out.println(customer2 + readyMessage);
        }
        //Ahmad ordered a cappuccino. Use an if statement to check the status of his order and print the correct status message. If it is ready, also print the message to display the total. Note: Outcomes may be different depending on what you assigned as the status.
        boolean ahmadOrder = true;
        if (ahmadOrder == true){
            System.out.println(customer1 + readyMessage + displayTotalMessage + cappuccino);
        }
        // Sali just ordered 2 lattes, print the message to display their total. Next, use an if statement to print the appropriate order status message. Change the isReady flag value from true to false or vice versa in order to test your control logic (if-statement).
        double total = latte + latte;
        System.err.println(displayTotalMessage + total);
        boolean isReadyOrderSali2 = false;
        if (isReadyOrderSali2){
            System.out.println(pendingMessage + customer2);
        }
        //Adam just realized he was charged for a coffee but had ordered a latte. Print the total message with the new calculated total (what he owes) to make up the difference.
        double Adamtotal = dripCoffee + latte;
        System.out.println(displayTotalMessage + Adamtotal);

        //Try changing the price values for each drink and isReady flags (booleans), to test if all of your logic works, even when prices and statuses are changed.
        double mochaNewPrice = 3.5;
        double dripCoffeeNew = 5.5;
        double latteNew = 7.5;
        double cappuccinoNew = 8;

        boolean isReadyOrderAhmadNew = false;
        boolean isReadyOrderSaliNew = false;
        boolean isReadyOrderAdamNew = false;
        if (isReadyOrderSaliNew){
            System.out.println(customer2+pendingMessage);
        }
        if (isReadyOrderAhmadNew){
            System.out.println(customer1 + pendingMessage );
        }
        if (isReadyOrderAdamNew){
            System.out.println(customer3 + pendingMessage);
        }
    }
}
