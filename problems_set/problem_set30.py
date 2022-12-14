def problem_set30():
    problem_set = {
        "PROPOSAL": [
            {"cost": 161, "quality": 156},
            {"cost": 169, "quality": 159},
            {"cost": 172, "quality": 171},
            {"cost": 171, "quality": 162},
            {"cost": 154, "quality": 156},
            {"cost": 160, "quality": 168},
            {"cost": 163, "quality": 161},
            {"cost": 165, "quality": 173},
            {"cost": 168, "quality": 157},
            {"cost": 169, "quality": 172},
            {"cost": 160, "quality": 169},
            {"cost": 171, "quality": 166},
            {"cost": 159, "quality": 169},
            {"cost": 161, "quality": 159},
            {"cost": 159, "quality": 159},
            {"cost": 3, "quality": 1},
            {"cost": 2, "quality": 15},
            {"cost": 15, "quality": 2},
            {"cost": 2, "quality": 16},
            {"cost": 6, "quality": 19},
            {"cost": 16, "quality": 18},
            {"cost": 7, "quality": 1},
            {"cost": 8, "quality": 5},
            {"cost": 9, "quality": 19},
            {"cost": 15, "quality": 18},
            {"cost": 7, "quality": 4},
            {"cost": 9, "quality": 10},
            {"cost": 6, "quality": 10},
            {"cost": 9, "quality": 16},
            {"cost": 6, "quality": 4}
        ],
        "AVAILABLE_MONEY": 300,
        "OPTIMAL_QUALITY": 331
    }

    problem_set.update(SET_SIZE=len(problem_set.get("PROPOSAL")))
    return problem_set
