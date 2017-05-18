
class Carrier(object):
    #### Variables ####
    NUM_OF_RATS #Number of rats in this carrier
    INFECTED #Bool
    MOBILITY #Ability to travel
    LIFESPAN_COUNTER #Counts the lifespan of the rats.  Becoming infected will cut the lifespan.
    POP_GROWTH_RATE #Growth rate of this agent. The agent will eventually split.
    