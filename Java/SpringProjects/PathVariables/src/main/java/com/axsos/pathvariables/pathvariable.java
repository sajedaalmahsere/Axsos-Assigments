package com.axsos.pathvariables;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class pathvariable {
	
	@GetMapping("/daikichi/travel/{placename}")
	public String Travel(@PathVariable("placename") String placename) {
		return "Congratulations! You will soon Travel to " + placename;
	}
}
