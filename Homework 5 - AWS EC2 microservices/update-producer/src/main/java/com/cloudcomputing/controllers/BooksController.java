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
	
	@PostMapping("/add")
	public boolean AddNewBook(@RequestParam(value="title") String title, @RequestParam(value="author") String author, @RequestParam(value="genre") String genre) 
	{
		Book b = new Book();
		b.setAuthor(author);
		b.setGenre(genre);
		b.setTitle(title);
		
		try {
			bookRepository.save(b);
		}
		catch (Exception e) {
			return false;
		}
		
		return true;
	}
	
	@PutMapping("/update/{bookId}")
	public boolean UpdateExistingBook(@PathVariable(value = "bookId") Integer bookId, @RequestParam(value="title") String title, @RequestParam(value="author") String author, @RequestParam(value="genre") String genre)
	{
		Book b = bookRepository.findById(bookId).get();
		b.setAuthor(author);
		b.setGenre(genre);
		b.setTitle(title);
		
		try {
			bookRepository.save(b);
		}
		catch (Exception e) {
			return false;
		}
		
		return true;
	}

}
