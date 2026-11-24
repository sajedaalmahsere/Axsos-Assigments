
package com.axsos.ninjagold;

import java.util.ArrayList;
import java.util.Random;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import jakarta.servlet.http.HttpSession;

@Controller
public class NinjaController {

    @GetMapping("/")
    public String index(HttpSession session) {

        // Initialize gold
        if (session.getAttribute("Gold") == null) {
            session.setAttribute("Gold", 0);
        }

        // Initialize activity list
        if (session.getAttribute("activities") == null) {
            session.setAttribute("activities", new ArrayList<String>());
        }

        // Check if the ninja is in debtors' prison
        int gold = (int) session.getAttribute("Gold");

        if (gold < -50) {
            return "prison.jsp";
        }

        return "game.jsp";
    }

    @PostMapping("/process")
    public String process(
        @RequestParam("place") String place,
        HttpSession session
    ) {

        // Handle reset first
        if (place.equals("reset")) {
            session.invalidate();
            return "redirect:/";
        }

        // Get current gold
        int gold = (int) session.getAttribute("Gold");

        // Generate random number
        Random random = new Random();

        // Determine the amount
        int amount = 0;

        if (place.equals("farm")) {
            amount = random.nextInt(11) + 10;
        } else if (place.equals("cave")) {
            amount = random.nextInt(6) + 5;
        } else if (place.equals("house")) {
            amount = random.nextInt(4) + 2;
        } else if (place.equals("quest")) {
            amount = random.nextInt(101) - 50;
        } else if (place.equals("spa")) {
            amount = -(random.nextInt(16) + 5);
        } else {
            return "redirect:/";
        }

        // Update gold
        gold += amount;
        session.setAttribute("Gold", gold);

        // Create timestamp
        LocalDateTime now = LocalDateTime.now();

        DateTimeFormatter formatter =
            DateTimeFormatter.ofPattern("MMM dd, yyyy HH:mm");

        String timestamp = now.format(formatter);

        // Create activity message
        String activity;

        if (amount >= 0) {
            activity = "You earned " + amount
                + " gold from the " + place + "!";
        } else {
            activity = "You lost " + Math.abs(amount)
                + " gold from the " + place + "!";
        }

        activity += " (" + timestamp + ")";

        // Get activities
        ArrayList<String> activities =
            (ArrayList<String>) session.getAttribute("activities");

        // Add newest activity first
        activities.add(0, activity);

        // Save activities
        session.setAttribute("activities", activities);

        return "redirect:/";
    }
}
