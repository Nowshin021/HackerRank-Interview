    # logic...only count the vally becaus when you go up and react sea level(0) it
    #means u have completed a vally
    
    
    sea = valley = 0

    for p in path:
        if p == 'U':
            sea += 1
        else:
            sea -= 1
        
        if p == 'U' and sea == 0:
            valley += 1
    
    return valley
