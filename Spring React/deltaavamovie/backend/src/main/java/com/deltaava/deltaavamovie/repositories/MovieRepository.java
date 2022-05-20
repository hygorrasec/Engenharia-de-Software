package com.deltaava.deltaavamovie.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import com.deltaava.deltaavamovie.entities.Movie;

public interface MovieRepository extends JpaRepository<Movie, Long> {

}
