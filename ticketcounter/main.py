from ticketcounter import TicketCounterSimulation

print("Welcome to TicketCounterSimulation")
"""
: 25
Number of ticket agents: 2
Average service time per passenger: 3
Average time between passenger arrival: 2
"""
numMinutes = int(input("Number of minutes to simulate: "))
numAgents = int(input("Number of ticket agents: "))
serviceTime = int(input("Average service time per passenger: "))
betweenTime = float(input("Average time between passenger arrival: "))

# def __init__( self, numAgents, numMinutes, betweenTime, serviceTime ):
simulation = TicketCounterSimulation(numAgents, numMinutes, betweenTime, serviceTime)

simulation.run()
print(simulation)
