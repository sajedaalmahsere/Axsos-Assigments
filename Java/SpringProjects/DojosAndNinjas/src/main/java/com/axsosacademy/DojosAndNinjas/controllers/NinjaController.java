package com.axsosacademy.DojosAndNinjas.controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

import com.axsosacademy.DojosAndNinjas.models.Ninja;
import com.axsosacademy.DojosAndNinjas.services.DojoService;
import com.axsosacademy.DojosAndNinjas.services.NinjaService;

import jakarta.validation.Valid;

@Controller
public class NinjaController {
	@Autowired
	private NinjaService ninjaService;
	private DojoService dojoService;
	
	public NinjaController(NinjaService ninjaService,DojoService dojoService) {
		
		this.ninjaService = ninjaService;
		this.dojoService = dojoService;
	}

	@GetMapping("/ninja")
	public String ninjas(@ModelAttribute("ninja") Ninja ninja,
		    Model model) {
		model.addAttribute("dojos", dojoService.allDojos());
		System.out.println("######## I am Here");
		return "ninja.jsp";
	}
	
	@PostMapping("/ninja/add")
	public String createNinja(@Valid @ModelAttribute("ninja") Ninja ninja,
			BindingResult result) {
		if (result.hasErrors()) {
            return "ninja.jsp";
        } else {
            ninjaService.createNinja(ninja);
            return "redirect:/ninja";
        	}
        }
		
	@GetMapping("/ninja/burbank") 
	String burbank(Model model) {
		model.addAttribute("ninja", ninjaService.allNinjas());
		return "burbank.jsp";
	}
	
}
