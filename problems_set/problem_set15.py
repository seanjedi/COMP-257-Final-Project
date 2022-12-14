def problem_set15():
    problem_set = {
        "PROPOSAL": [
            {"cost": 86, "quality": 90},
            {"cost": 90, "quality": 87},
            {"cost": 96, "quality": 95},
            {"cost": 86, "quality": 87},
            {"cost": 91, "quality": 90},
            {"cost": 80, "quality": 81},
            {"cost": 92, "quality": 95},
            {"cost": 91, "quality": 77},
            {"cost": 20, "quality": 4},
            {"cost": 1, "quality": 15},
            {"cost": 16, "quality": 11},
            {"cost": 11, "quality": 17},
            {"cost": 17, "quality": 13},
            {"cost": 3, "quality": 9},
            {"cost": 19, "quality": 20}
        ],
        "AVAILABLE_MONEY": 150,
        "OPTIMAL_QUALITY": 169
    }

    problem_set.update(SET_SIZE=len(problem_set.get("PROPOSAL")))
    return problem_set
