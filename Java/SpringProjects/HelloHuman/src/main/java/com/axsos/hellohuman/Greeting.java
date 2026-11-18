package com.axsos.hellohuman;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;


@RestController
public class Greeting {
	
	@GetMapping("/")
	public String index(
			@RequestParam(value = "username", defaultValue = "human")String username,
			@RequestParam(value = "lastname", required = false)String lastname,
			@RequestParam(value = "times", defaultValue = "1") int times
					 ) {
		String result ="";
		for (int i = 0 ; i< times ; i++) {
			result += "Hello " + username +  lastname;
				 
		}
	return result;
}
	
}
