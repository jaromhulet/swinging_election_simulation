from states import state

class simulate_elections():

    def __init__(self,
                 state_dict,
                 resid_state,
                 elect_votes_to_win = 270):
        
        '''
            state_dict (dictionary) : list of instances of state class
            resid_state (str)       : state abbreviation for the single 
                                       potential swing vote
            elect_votes_to_win (int) : number of electoral votes to win
                                       default to 270

        '''
        
        self.state_dict = state_dict
        self.resid_state = resid_state
        self.elect_votes_to_win = elect_votes_to_win

        return
    
    def simulate_national_election(self):

        '''
            Simulates a popular election for each state and adds up
            electoral votes for candidate. Determines if the candidate
            loses without resident's state and wins with it. This is 
            a pre-requisite to the resident swinging the overall
            election

            input:
                no explicit input, but uses state_dict, resid_state
                elect_votes_to_win attributes

            output:
                swing_election (bool) : True if resident's state would
                                        swing election

        '''

        won_elect_votes = 0

        # simulate election for each state
        
        for state in self.state_dict.values():

            # skip simulation for resident's state
            if state != self.resid_state:
                state_elect_votes = state.simulate_election()
                won_elect_votes += state_elect_votes

        
        # determine of candidate loses with resident's state's electoral votes and winds with it
        # print(f'elect votes b4 state = {won_elect_votes}')
        # print(f'elect votes with state = {won_elect_votes + self.state_dict[self.resid_state].elect_votes }')
        # print(f'needed votes = {self.elect_votes_to_win}')
        loss_without_resid_state = won_elect_votes <= self.elect_votes_to_win
        win_with_resid_state = won_elect_votes + self.state_dict[self.resid_state].elect_votes >= self.elect_votes_to_win

        if  loss_without_resid_state and win_with_resid_state:
            swing_election = True
        else:
            swing_election = False

        return swing_election
    
    def simulate_state_election(self):

        '''
            Simulates the resident's state election and 
            determines if the resident's vote could swing
            the election.

            inputs
                no direct inputs, uses multiple class attributes

            output:
                swing_state (bool) : True if resident's vote
                                     could swing election False
                                     if not
        
        '''
        resident_state = self.state_dict[self.resid_state]

        swing_state = resident_state.simulate_votes()

        return swing_state
    
    def simulate_overall_election(self):

        '''
            Runs the state election and then the national election
            identifies if a single vote swung the entire election

            inputs
                no direct inputs, uses multiple attributes

            output
                swing_overall_election (bool) : True means a single vote 
                                                swung the election, false
                                                means that it did not
        '''
        state_swing_election = self.simulate_national_election()

        vote_swing_state = self.simulate_state_election()

        if state_swing_election and vote_swing_state:
            swing_overall_election = True
        else:
            swing_overall_election = False

        return swing_overall_election
    
    def simulate_multiple_times(self,
                                iters,
                                sim_type):
        

        '''
            Runs individual simulations multiple times.

            inputs
                iters (int) : number of simulations to run
                sim_type (str) : indicates what kind of simulation
                                 should be run - acceptable values are
                                 'state', 'national' and 'both'

        '''

        if sim_type == 'state':
            sim_func = self.simulate_state_election

        elif sim_type == 'national':
            sim_func = self.simulate_national_election

        elif sim_type == 'both':
            sim_func = self.simulate_overall_election

        election_results = []
        for _ in range(iters + 1):
            iter_result = sim_func()
            election_results.append(iter_result)

        swing_pct = (sum(election_results) / len(election_results))*100
        # print(f'The election was swung {swing_pct}% of the simulations')

        return election_results
