package com.axsosacademy.DojosAndNinjas.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

import com.axsosacademy.DojosAndNinjas.models.Dojo;
import com.axsosacademy.DojosAndNinjas.services.DojoService;

import jakarta.validation.Valid;

@Controller
public class DojoController {
	
	@Autowired
	private DojoService dojoService;
	
	@GetMapping("/")
	public String redirect() {
		return "redirect:/dojo";
	}
	
	@GetMapping("/dojo")
	public String dojos(@ModelAttribute("dojo") Dojo dojo) {
		System.out.println("######## I am Here");
		return "dojo.jsp";
	}
	
	@PostMapping("/add/dojo")
	public String createDojo(@Valid @ModelAttribute("dojo") Dojo dojo,
			BindingResult result) {
		if (result.hasErrors()) {
            return "dojo.jsp";
        } else {
            dojoService.createDojo(dojo);
            return "redirect:/dojo";
        }	
	}
	

}
