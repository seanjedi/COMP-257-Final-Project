def problem_set20():
    problem_set = {
        "PROPOSAL": [
            {"cost":107, "quality":103},
            {"cost":122, "quality":116},
            {"cost":109, "quality":119},
            {"cost":110, "quality":118},
            {"cost":103, "quality":117},
            {"cost":105, "quality":104},
            {"cost":106, "quality":118},
            {"cost":113, "quality":110},
            {"cost":117, "quality":109},
            {"cost":105, "quality":104},
            {"cost":5, "quality":20},
            {"cost":17, "quality":3},
            {"cost":16, "quality":12},
            {"cost":7, "quality":14},
            {"cost":12, "quality":20},
            {"cost":10, "quality":19},
            {"cost":4, "quality":9},
            {"cost":7, "quality":2},
            {"cost":11, "quality":16},
            {"cost":2, "quality":12}
        ],
        "AVAILABLE_MONEY" : 200,
        "OPTIMAL_QUALITY" : 246
    }
    
    problem_set.update(SET_SIZE = len(problem_set.get("PROPOSAL"))) 
    return problem_set