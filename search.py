# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def expand(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (child,
        action, stepCost), where 'child' is a child to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that child.
        """
        util.raiseNotDefined()

    def getActions(self, state):
        """
          state: Search state

        For a given state, this should return a list of possible actions.
        """
        util.raiseNotDefined()

    def getActionCost(self, state, action, next_state):
        """
          state: Search state
          action: action taken at state.
          next_state: next Search state after taking action.

        For a given state, this should return the cost of the (s, a, s') transition.
        """
        util.raiseNotDefined()

    def getNextState(self, state, action):
        """
          state: Search state
          action: action taken at state

        For a given state, this should return the next state after taking action from state.
        """
        util.raiseNotDefined()

    def getCostOfActionSequence(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

# DFS algorithm
def depthFirstSearch(problem):
    # Create a stack to store the state and the actions taken to reach that state
    stack = util.Stack()
    # Push the start state and an empty list of actions to the stack
    stack.push((problem.getStartState(), []))
    
    # Create a set to store the visited states
    visited = set()
    
    # While the stack is not empty, pop the state and actions from the stack
    while not stack.isEmpty():
        state, actions = stack.pop()

        # If the state is the goal state, return the actions taken to reach that state
        if problem.isGoalState(state):
            return actions

        # If the state has not been visited, add it to the visited set
        if state not in visited:
            visited.add(state)

            # For each child of the state, push the child and the actions taken to reach that child to the stack
            for child, action, _ in problem.expand(state):
                if child not in visited:
                    stack.push((child, actions + [action]))
    
    # If no solution is found, return an empty list
    return []

# BFS algorithm
def breadthFirstSearch(problem):
    # Crete a queue to store the state and the actions taken to reach that state, made so the algorithm searches the shallowest nodes first
    queue = util.Queue()
    queue.push((problem.getStartState(),[]))
    
    # Set to store the visited states
    visited = set()
    
    while not queue.isEmpty():
        # Pop the state and actions from the queue
        state,actions = queue.pop()

        # Verify if the state is the goal state
        if problem.isGoalState(state):
            return actions  

        # Add the state to the visited set
        if state not in visited:
            visited.add(state) 

            # For each child of the state, push the child and the actions taken to reach that child to the queue
            for child, action, _ in problem.expand(state):
                if child not in visited:
                    newActions = actions+ [action]
                    queue.push((child,newActions))

    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
