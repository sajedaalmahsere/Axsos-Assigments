public class TestOrder {
    public static void main(String[] args) {
    
        Item item1 = new Item("mocha", 3.5);
        Item item2 = new Item("latte", 4.5);    
        Item item3 = new Item("drip coffee", 2.5);

        Order order1 = new Order("Sajeda", true);
        Order order2 = new Order("Mariam", false);

        order1.addItem(item1);
        order1.addItem(item2);
        order2.addItem(item3);

        // System.out.println(order1.getStatusMessage());
        // System.out.println(order2.getStatusMessage());
        System.out.println(order1.getOrderTotal());
        order1.display();
        
    }
}
