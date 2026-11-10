import java.util.ArrayList;
public class TestOrders {
    public static void main(String[] args) {
    
        // Menu items
        Item item1 = new Item();
        item1.name = "katshap";
        item1.price = 14.5;

        Item item2 = new Item();
        item2.name = "tomato";
        item2.price = 2;

        // Order variables -- order1, order2 etc.
        Order order1 = new Order();
        order1.name = "Sajeda";
        order1.total = 16.5;
        order1.ready = true;
        order1.items.add (item1) ;
        order1.items.add(item2);

        Order order2 = new Order();
        order2.name = "Shatha";
        order2.total = 2;
        order2.ready = false;
        order2.items.add (item2) ;
        // Application Simulations
        // Use this example code to test various orders' updates
        System.out.printf("Name: %s\n", order1.name);
        System.out.printf("Total: %s\n", order1.total);
        System.out.printf("Ready: %s\n", order1.ready);
    }
}