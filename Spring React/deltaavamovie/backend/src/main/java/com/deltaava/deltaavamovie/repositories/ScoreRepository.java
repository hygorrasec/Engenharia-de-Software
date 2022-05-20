package com.deltaava.deltaavamovie.repositories;

import org.springframework.data.jpa.repository.JpaRepository;

import com.deltaava.deltaavamovie.entities.Score;
import com.deltaava.deltaavamovie.entities.ScorePK;

public interface ScoreRepository extends JpaRepository<Score, ScorePK> {

}
