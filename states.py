import numpy as np
from scipy.stats import binom
import time

def calc_time(start_time, end_time, string = ''):

    execution_time = end_time - start_time
    print(f"Execution time for {string}: {execution_time} seconds")

    return

class state():

    def __init__(self,
                 state_abbrv,
                 elect_votes,
                 reg_voters,
                 voter_turn_out,
                 vote_prob_dem,
                 vote_prob_repub,
                 party,
                 exclude_odd_vote_results = False):
        
        '''
            state_abbrv (str)      : state abbreviation
            elect_votes (int)      : number of electoral votes that state has
            reg_voters (int)       : number of registered voters in state
            voter_turn_out (float) : percent of registered voters that vote
            vote_prob_dem (float)  : probability that a single voter
                                     votes for the democrate candidate
            vote_prob_rep (float)  : probability that a single voter
                                     votes for the republican candidate
            party (str)            : the party of the potential swing voter
                                     'rep' or 'dem'                                
        '''

        self.state_abbrv = state_abbrv
        self.elect_votes = elect_votes
        self.reg_voters = reg_voters
        self.voter_turn_out = voter_turn_out
        self.vote_prob_dem = vote_prob_dem
        self.vote_prob_repub = vote_prob_repub
        self.party = party
        self.exclude_odd_vote_results = exclude_odd_vote_results

        # scale poll numbers for two-party assumption
        sum_dem_rep = self.vote_prob_dem + self.vote_prob_repub

        if self.party == 'dem':
            self.vote_prob = self.vote_prob_dem / sum_dem_rep
        else:
            self.vote_prob = self.vote_prob_repub / sum_dem_rep

        # simulate the number of voters that turn out
        self.actual_voters = np.random.binomial(n = self.reg_voters,
                                                p = self.vote_prob)            

        return
    
    def simulate_election(self):
        
        '''
            Simulates an election by simulating the vote of each 
            voting registered voter in the state.  Assumes popular 
            vote winner takes all electoral points

            output
                elect_points_won (int) : if the candidate wins the state, this is 
                                         the self.elect_votes else, it is 0        
        '''

        votes_for_candidate = np.random.binomial(1, self.vote_prob, self.actual_voters)

        # see if votes for candidate is greater than 50% of actual voters
        if np.sum(votes_for_candidate) > 0.5*self.actual_voters:
            return self.elect_votes
        else:
            return 0
        
    def simulate_votes(self):

        '''
            Simulates the votes from a state election. If state would
            be lost without resident's vote and won with it, then
            the resident will swing the state's vote.

            input:
                no explicit inputs - uses multiple class attributes

            output:
                swing_vote (bool) : True if resident's vote would swing the
                                    election, False otherwise
        
        '''
        # if actual_voters is odd, there is no chance of swinging the election
        if (self.actual_voters % 2 != 0) and (self.exclude_odd_vote_results):
            swing_vote = False
            return swing_vote

        # calculate probability of a tie using binomial distribution
        prob_of_tie = binom.pmf(int(self.actual_voters*0.5), self.actual_voters, self.vote_prob)
        rand_num = np.random.rand()

        if rand_num <= prob_of_tie:
            swing_vote = True
        else:
            swing_vote = False

        return swing_vote
