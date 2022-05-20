package com.deltaava.deltaavamovie.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import com.deltaava.deltaavamovie.entities.User;

public interface UserRepository extends JpaRepository<User, Long> {

	User findByEmail(String email);
}
