package com.axsos.counter;

import org.springframework.stereotype.Controller;
//import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
//import org.springframework.web.bind.annotation.PostMapping;

import jakarta.servlet.http.HttpSession;

@Controller
public class CounterController {
	@GetMapping("/")
	public String render() {
		return "redirect:/your_server";
	}
	
	@GetMapping("/your_server")
	public String welcome() {
		return "Welcome.jsp";
	}
	
	@GetMapping("/your_server/counter")
	public String counter(HttpSession session) {
		// Initialize counter if the visitor opens this page first
		if (session.getAttribute("count") == null) {
	        session.setAttribute("count", 1);
	    } else {
	    	
	        int count = (int) session.getAttribute("count");
	        session.setAttribute("count", count + 1);
	    }

        return "Counter.jsp";
		}
	}
	

