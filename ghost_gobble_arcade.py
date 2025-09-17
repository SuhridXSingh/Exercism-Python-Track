def eat_ghost(power_pellet_active, touching_ghost):
  
    total= power_pellet_active and touching_ghost
    return total
  
def score(touching_power_pellet, touching_dot):

    total= touching_power_pellet or touching_dot
    return total
  
def lose(power_pellet_active, touching_ghost):
   
    total= not power_pellet_active 
    return total
  
def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
  
    total= (touching_ghost and power_pellet_active and has_eaten_all_dots) or (not touching_ghost and has_eaten_all_dots)
    return total
