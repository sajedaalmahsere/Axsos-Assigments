package com.axsos.coffeeapp;

public class CoffeeKioskTest {

    public static void main(String[] args) {

        // Create a CoffeeKiosk object
        CoffeeKiosk kiosk = new CoffeeKiosk();

        // Add menu items
        kiosk.addMenuItem("banana", 2.00);
        kiosk.addMenuItem("coffee", 1.50);
        kiosk.addMenuItem("latte", 4.50);
        kiosk.addMenuItem("cappuccino", 3.00);
        kiosk.addMenuItem("muffin", 4.00);

        // Display menu
        kiosk.displayMenu();

        // Create a new order
        kiosk.newOrder();
    }
}