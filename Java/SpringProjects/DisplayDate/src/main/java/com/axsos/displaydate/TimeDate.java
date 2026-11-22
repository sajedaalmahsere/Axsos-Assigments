package com.axsos.displaydate;

import java.util.Date;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class TimeDate {
	
	@GetMapping("/")
	public String home() {
		return "Home.jsp";
	}
	
	@GetMapping("/date")
	public String date(Model model) {
		Date date = new Date();
	    model.addAttribute("date", date);
		return "Date.jsp";
	}
	
	@GetMapping("/time")
	public String time(Model model) {
		Date date = new Date();
	    model.addAttribute("date", date);
		return "Time.jsp";
	}
}
