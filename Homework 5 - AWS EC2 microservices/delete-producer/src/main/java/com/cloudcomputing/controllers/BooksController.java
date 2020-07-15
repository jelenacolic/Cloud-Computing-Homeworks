package com.cloudcomputing.controllers;

import java.util.Collections;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.cloudcomputing.models.Book;
import com.cloudcomputing.repositories.BookRepository;

@RestController
@CrossOrigin(origins = "*", allowedHeaders = "*")
@RequestMapping("/")
public class BooksController {
	@Autowired
	private BookRepository bookRepository;
	
	
	@DeleteMapping("/delete")
	public boolean DeleteBook(@RequestParam(value="bookId") Integer bookId) 
	{
		try {
			bookRepository.deleteById(bookId);
		}
		catch (Exception e) {
			return false;
		}
		
		return true;
	}
}
