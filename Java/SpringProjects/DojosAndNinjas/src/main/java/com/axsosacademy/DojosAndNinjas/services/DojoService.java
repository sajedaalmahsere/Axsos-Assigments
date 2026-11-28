package com.axsosacademy.DojosAndNinjas.services;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

import com.axsosacademy.DojosAndNinjas.models.Dojo;
import com.axsosacademy.DojosAndNinjas.repositories.DojoRepository;

import jakarta.validation.Valid;

@Service
public class DojoService {
	
	@Autowired
	private DojoRepository dojoRepository;

	public DojoService(DojoRepository dojoRepository) {
		this.dojoRepository = dojoRepository;
		
	}
	
	public List<Dojo> allDojos(){
		return dojoRepository.findAll();
		}
	
	public Dojo createDojo(Dojo dojo) {
		return dojoRepository.save(dojo);
	}

	public DojoRepository getDojoRepository() {
		return dojoRepository;
	}

}
