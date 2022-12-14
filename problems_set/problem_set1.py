def problem_set1():
    problem_set = {
        "PROPOSAL": [
            {"cost":52, "quality":58},
            {"cost":56, "quality":57},
            {"cost":70, "quality":70},
            {"cost":56, "quality":54},
            {"cost":60, "quality":63},
            {"cost":17, "quality":17},
            {"cost":3, "quality":16},
            {"cost":2, "quality":10},
            {"cost":10, "quality":8},
            {"cost":1, "quality":14}
        ],
        "AVAILABLE_MONEY" : 100,
        "OPTIMAL_QUALITY" : 128
    }
    
    problem_set.update(SET_SIZE = len(problem_set.get("PROPOSAL"))) 
    return problem_set