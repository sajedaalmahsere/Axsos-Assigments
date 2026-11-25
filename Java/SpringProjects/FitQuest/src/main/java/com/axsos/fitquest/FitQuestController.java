package com.axsos.fitquest;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.Random;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import jakarta.servlet.http.HttpSession;

@Controller
public class FitQuestController {

	// Shows the dashboard with the current points and the activity log
	@GetMapping("/")
	public String index(HttpSession session) {
		if (session.getAttribute("points") == null) {
		    session.setAttribute("points", 0);
		}

		if (session.getAttribute("log") == null) {
		    session.setAttribute("log", new ArrayList<String>());
		}
		
		
		return "index";
	}

	// Handles all four activity forms
	@PostMapping("/process")
	public String process(@RequestParam("activity") String activity, HttpSession session) {
		Random random = new Random();
		int points = (int) session.getAttribute("points");
		@SuppressWarnings("unchecked")
		ArrayList<String> log = (ArrayList<String>) session.getAttribute("log");
		String time = new SimpleDateFormat("MMMM d, yyyy h:mm a").format(new Date());

		int earned = 0;
		String place = "";

		if (activity.equals("walk") ) {
			earned = random.nextInt(6) + 5;
			place = "went for a walk";
		} else if (activity.equals("yoga")) {
			earned = random.nextInt(11) + 10;
			place = "finished a yoga class";
		} else if (activity.equals("weights")) {
			earned = random.nextInt(16) + 15;
			place = "lifted weights at the gym";
		} else if (activity.equals("challenge")) {
			earned = random.nextInt(51);
			place = "took on the daily challenge";
		}

		points += earned;

		if (earned >= 0) {
			log.add(0, "You " + place + " and earned " + earned + " points. (" + time + ")");
		} else {
			log.add(0, "You " + place + " and lost " + Math.abs(earned) + " points. Ouch! (" + time + ")");
		}

		session.setAttribute("points", points);
		session.setAttribute("log", log);
		return "redirect:/";
	}
}

