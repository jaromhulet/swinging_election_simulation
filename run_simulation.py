from state_info import states_dict
import pandas as pd
import election_simulations as sim

state_abbreviations = [
    'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
    'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
    'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
    'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
    'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
]

swinging_states_df = pd.DataFrame()

for abbrv in state_abbreviations:

    test_sim = sim.simulate_elections(states_dict,
                                     abbrv)

    swing = test_sim.simulate_multiple_times(100000, 'national')
    # swing = test_sim.simulate_multiple_times(5000000, 'state')

    temp_swing_prob = round(sum(swing) / len(swing), 10)*100

    temp_df = pd.DataFrame({'state' : [abbrv],
                            'probability' : [temp_swing_prob]})
    
    swinging_states_df = pd.concat([swinging_states_df, temp_df])

    print(f'{abbrv} : {temp_swing_prob}%')

swinging_states_df.to_csv('prob_of_swining_state.csv')

print(swinging_states_df)
