import java.util.ArrayList;

public class Order {
    private String name;
    private boolean ready;
    private ArrayList<Item> items = new ArrayList<>();

    public Order(){
        this.name = "Guest";
    }

    public Order(String name, boolean ready){
        this.name = name;
        this.ready = ready;
    }
    // ORDER METHODS
        // Most of your code will go here, 
        // so implement the getters and setters first!

    public void addItem(Item item){
        this.items.add(item);
    }

    public String getStatusMessage(){
        if (this.ready == true){
            return "Your order is ready.";
        }
        else{
            return "Thank you for waiting. Your order will be ready soon.";
        }
    }

    public double getOrderTotal(){
        double total = 0;
        for (int i = 0; i < items.size(); i++){
            total += items.get(i).getPrice();
        }
        return total;
    }

    public void display(){
        System.out.println("Customer name:" + this.name);
        System.out.println("You ordered:");
        for (int i = 0; i < items.size(); i++){
            System.out.println(items.get(i).getName() + " - $" + items.get(i).getPrice());
        }
        System.out.println("Total: $" + this.getOrderTotal());
    }

    // GETTERS & SETTERS
    public String getName(){
        return name;
    }
    public boolean getReady(){
        return ready;
    }
    public ArrayList<Item> getItems(){
        return items;
    }

    //setters
    public void setName(String name){
        this.name = name;
    }
    public void setItems(ArrayList<Item> items){
        this.items = items;
    }

}
