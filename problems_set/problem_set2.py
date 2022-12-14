def problem_set2():
    problem_set = {
        "PROPOSAL": [
            {"cost":110, "quality":107},
            {"cost":111, "quality":106},
            {"cost":106, "quality":104},
            {"cost":122, "quality":116},
            {"cost":117, "quality":116},
            {"cost":112, "quality":113},
            {"cost":115, "quality":122},
            {"cost":112, "quality":116},
            {"cost":104, "quality":108},
            {"cost":110, "quality":117},
            {"cost":110, "quality":103},
            {"cost":120, "quality":118},
            {"cost":106, "quality":121},
            {"cost":8, "quality":4},
            {"cost":3, "quality":19},
            {"cost":14, "quality":6},
            {"cost":20, "quality":15},
            {"cost":5, "quality":1},
            {"cost":5, "quality":3},
            {"cost":18, "quality":14},
            {"cost":17, "quality":20},
            {"cost":8, "quality":1},
            {"cost":6, "quality":3},
            {"cost":14, "quality":6},
            {"cost":3, "quality":11}
        ],
        "AVAILABLE_MONEY" : 200,
        "OPTIMAL_QUALITY" : 216
    }
    
    problem_set.update(SET_SIZE = len(problem_set.get("PROPOSAL"))) 
    return problem_set