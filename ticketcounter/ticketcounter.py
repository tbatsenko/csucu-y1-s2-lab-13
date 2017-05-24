# Implementation of the main simulation class.
from arrays import Array
from arrayqueue import ArrayQueue
from people import TicketAgent, Passenger
import random

class TicketCounterSimulation(object):
    # Create a simulation object.
    def __init__( self, numAgents, numMinutes, betweenTime, serviceTime ):
        # Parameters supplied by the user.
        self._arriveProb = 1.0 / betweenTime
        self._serviceTime = serviceTime
        self._numMinutes = numMinutes

        # Simulation components.
        self._passengerQ = ArrayQueue()
        self._theAgents = Array( numAgents )
        for i in range( numAgents ) :
            self._theAgents[i] = TicketAgent(i+1)

        # Computed during the simulation.
        self._totalWaitTime = 0
        self._numPassengers = 0

    # Run the simulation using the parameters supplied earlier.
    def run( self ):
        for curTime in range(self._numMinutes + 1) :
            self._handleArrive(curTime)
            self._handleBeginService(curTime)
            self._handleEndService(curTime)

    # Print the simulation results.
    def printResults( self ):
        numServed = self._numPassengers - len(self._passengerQ)
        avgWait = float( self._totalWaitTime ) / numServed
        print( "" )
        print( "Number of passengers served = ", numServed )
        print( "Number of passengers remaining in line = %d" %
        len(self._passengerQ) )
        print( "The average wait time was %4.2f minutes." % avgWait )

    # Handles simulation rule #1.
    def _handleArrive(self, curTime):
        """
        Rule 1: If a customer arrives, he is added to the queue.
        At most, one customer can arrive during each time step.
        """
        if random.random() <= self._arriveProb:
            self._numPassengers += 1
            thePassenger = Passenger(self._numPassengers, curTime)
            print("Time {}: Passenger {} arrived.".format(curTime, self._numPassengers))
            self._passengerQ.add(thePassenger)
    # Handles simulation rule #2.
    def _handleBeginService(self, curTime):
        """
        Rule 2: If there are customers waiting, for each free server,
        the next customer in line begins her transaction.
        """
        for agent in self._theAgents:
            if agent.isFree():
                if not self._passengerQ.isEmpty():
                    thePassenger = self._passengerQ.pop()
                    agent.startService(thePassenger,
                     curTime + self._serviceTime)
                    print("Time {}: Agent {} started serving passenger {}.".format(curTime, agent._idNum, thePassenger._idNum))

    # Handles simulation rule #3.
    def _handleEndService( self, curTime ):
        """
        Rule 3: For each server handling a transaction, if the transaction is complete, the
        customer departs and the server becomes free.
        """
        for agent in self._theAgents:
            if agent.isFinished(curTime):
                thePassenger = agent.stopService()
                self._totalWaitTime += curTime - thePassenger._arrivalTime - self._serviceTime
                print("Time {}: Agent {} stopped serving passenger {}.".format(curTime, agent._idNum, thePassenger._idNum))
