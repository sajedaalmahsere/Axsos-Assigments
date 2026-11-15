package com.axsos.coffeeapp;
import java.util.ArrayList;
import java.util.Scanner;

public class CoffeeKiosk {
	private ArrayList<Item> menu;
	private ArrayList<Order> orders;
	
	public CoffeeKiosk () {
		this.menu = new ArrayList<>();
		this.orders = new ArrayList<>();
	}
	
	public void addMenuItem(String name, double price) {
	    int index = menu.size();
	    Item newItem = new Item(name, price, index);
	    menu.add(newItem);
	}
	
	public void displayMenu() {
		for (int i = 0 ; i< menu.size(); i++ ) {
			System.out.println(menu.get(i).getIndex() +" "+ menu.get(i).getName() +"----" + menu.get(i).getPrice() + "$");
		}
	}
	
	public void newOrder() {

	    // Ask for customer name
	    System.out.println("Please enter customer name for new order:");
	    Scanner scanner = new Scanner(System.in);
	    String name = scanner.nextLine();

	    // Create a new order
	    Order newOrder = new Order(name, 0, false, new ArrayList<Item>());

	    // Display the menu
	    displayMenu();

	    // Ask the customer to choose an item
	    System.out.println("Please enter a menu item index or q to quit:");
	    String itemNumber = scanner.nextLine();

	    // Collect order items
	    while (!itemNumber.equals("q")) {

	        // Convert String to int
	        int index = Integer.parseInt(itemNumber);

	        // Get the selected item from the menu
	        Item selectedItem = menu.get(index);

	        // Add the selected item to the order
	        newOrder.getItems().add(selectedItem);

	        // Ask for another item
	        System.out.println("Please enter a menu item index or q to quit:");
	        itemNumber = scanner.nextLine();
	    }

	    // Add the completed order to the orders list
	    orders.add(newOrder);

	    // Display order details
	    System.out.println("Order for: " +newOrder.getName());
	    for (int i = 0; i < newOrder.getItems().size(); i++) {
	        System.out.println(
	            newOrder.getItems().get(i).getName() + " -- $" +
	            newOrder.getItems().get(i).getPrice()
	        );
	    }
	    
	
	
	}
	
}
