package com.cloudcomputing.repositories;

import org.springframework.data.repository.CrudRepository;

import com.cloudcomputing.models.Book;

public interface BookRepository extends CrudRepository<Book, Integer> {

}
