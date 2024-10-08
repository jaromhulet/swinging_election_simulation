from simulate_election import state

party = 'rep'

# Dictionary with state instances and polling data for both Democrats and Republicans
states_dict = {
    'AL': state(state_abbrv='AL', elect_votes=9, reg_voters=2499000, voter_turn_out=0.454, vote_prob_dem=0.35, vote_prob_repub=0.63, party = party),
    'AK': state(state_abbrv='AK', elect_votes=3, reg_voters=597000, voter_turn_out=0.429, vote_prob_dem=0.40, vote_prob_repub=0.56, party = party),
    'AZ': state(state_abbrv='AZ', elect_votes=11, reg_voters=4543000, voter_turn_out=0.619, vote_prob_dem=0.49, vote_prob_repub=0.50, party = party),
    'AR': state(state_abbrv='AR', elect_votes=6, reg_voters=1631000, voter_turn_out=0.434, vote_prob_dem=0.32, vote_prob_repub=0.64, party = party),
    'CA': state(state_abbrv='CA', elect_votes=54, reg_voters=22100000, voter_turn_out=0.707, vote_prob_dem=0.65, vote_prob_repub=0.32, party = party),
    'CO': state(state_abbrv='CO', elect_votes=10, reg_voters=3888000, voter_turn_out=0.720, vote_prob_dem=0.54, vote_prob_repub=0.43, party = party),
    'CT': state(state_abbrv='CT', elect_votes=7, reg_voters=2265000, voter_turn_out=0.590, vote_prob_dem=0.60, vote_prob_repub=0.38, party = party),
    'DE': state(state_abbrv='DE', elect_votes=3, reg_voters=759000, voter_turn_out=0.631, vote_prob_dem=0.58, vote_prob_repub=0.38, party = party),
    'FL': state(state_abbrv='FL', elect_votes=30, reg_voters=14630000, voter_turn_out=0.625, vote_prob_dem=0.46, vote_prob_repub=0.49, party = party),
    'GA': state(state_abbrv='GA', elect_votes=16, reg_voters=7809000, voter_turn_out=0.620, vote_prob_dem=0.51, vote_prob_repub=0.48, party = party),
    'HI': state(state_abbrv='HI', elect_votes=4, reg_voters=832000, voter_turn_out=0.551, vote_prob_dem=0.62, vote_prob_repub=0.33, party = party),
    'ID': state(state_abbrv='ID', elect_votes=4, reg_voters=1042000, voter_turn_out=0.663, vote_prob_dem=0.32, vote_prob_repub=0.65, party = party),
    'IL': state(state_abbrv='IL', elect_votes=19, reg_voters=8625000, voter_turn_out=0.626, vote_prob_dem=0.58, vote_prob_repub=0.40, party = party),
    'IN': state(state_abbrv='IN', elect_votes=11, reg_voters=4825000, voter_turn_out=0.590, vote_prob_dem=0.44, vote_prob_repub=0.52, party = party),
    'IA': state(state_abbrv='IA', elect_votes=6, reg_voters=2135000, voter_turn_out=0.673, vote_prob_dem=0.47, vote_prob_repub=0.50, party = party),
    'KS': state(state_abbrv='KS', elect_votes=6, reg_voters=1861000, voter_turn_out=0.553, vote_prob_dem=0.40, vote_prob_repub=0.55, party = party),
    'KY': state(state_abbrv='KY', elect_votes=8, reg_voters=3430000, voter_turn_out=0.596, vote_prob_dem=0.36, vote_prob_repub=0.60, party = party),
    'LA': state(state_abbrv='LA', elect_votes=8, reg_voters=3030000, voter_turn_out=0.590, vote_prob_dem=0.40, vote_prob_repub=0.58, party = party),
    'ME': state(state_abbrv='ME', elect_votes=4, reg_voters=1074000, voter_turn_out=0.725, vote_prob_dem=0.51, vote_prob_repub=0.45, party = party),
    'MD': state(state_abbrv='MD', elect_votes=10, reg_voters=4182000, voter_turn_out=0.633, vote_prob_dem=0.62, vote_prob_repub=0.35, party = party),
    'MA': state(state_abbrv='MA', elect_votes=11, reg_voters=4674000, voter_turn_out=0.667, vote_prob_dem=0.65, vote_prob_repub=0.33, party = party),
    'MI': state(state_abbrv='MI', elect_votes=15, reg_voters=7728000, voter_turn_out=0.650, vote_prob_dem=0.50, vote_prob_repub=0.48, party = party),
    'MN': state(state_abbrv='MN', elect_votes=10, reg_voters=3912000, voter_turn_out=0.740, vote_prob_dem=0.53, vote_prob_repub=0.44, party = party),
    'MS': state(state_abbrv='MS', elect_votes=6, reg_voters=1755000, voter_turn_out=0.485, vote_prob_dem=0.37, vote_prob_repub=0.59, party = party),
    'MO': state(state_abbrv='MO', elect_votes=10, reg_voters=4420000, voter_turn_out=0.630, vote_prob_dem=0.45, vote_prob_repub=0.51, party = party),
    'MT': state(state_abbrv='MT', elect_votes=4, reg_voters=726000, voter_turn_out=0.674, vote_prob_dem=0.42, vote_prob_repub=0.55, party = party),
    'NE': state(state_abbrv='NE', elect_votes=5, reg_voters=1421000, voter_turn_out=0.616, vote_prob_dem=0.40, vote_prob_repub=0.58, party = party),
    'NV': state(state_abbrv='NV', elect_votes=6, reg_voters=1907000, voter_turn_out=0.580, vote_prob_dem=0.48, vote_prob_repub=0.49, party = party),
    'NH': state(state_abbrv='NH', elect_votes=4, reg_voters=980000, voter_turn_out=0.710, vote_prob_dem=0.50, vote_prob_repub=0.47, party = party),
    'NJ': state(state_abbrv='NJ', elect_votes=14, reg_voters=6273000, voter_turn_out=0.630, vote_prob_dem=0.56, vote_prob_repub=0.39, party = party),
    'NM': state(state_abbrv='NM', elect_votes=5, reg_voters=1475000, voter_turn_out=0.646, vote_prob_dem=0.54, vote_prob_repub=0.43, party = party),
    'NY': state(state_abbrv='NY', elect_votes=28, reg_voters=13250000, voter_turn_out=0.625, vote_prob_dem=0.60, vote_prob_repub=0.36, party = party),
    'NC': state(state_abbrv='NC', elect_votes=16, reg_voters=7590000, voter_turn_out=0.630, vote_prob_dem=0.48, vote_prob_repub=0.50, party = party),
    'ND': state(state_abbrv='ND', elect_votes=3, reg_voters=581000, voter_turn_out=0.623, vote_prob_dem=0.34, vote_prob_repub=0.62, party = party),
    'OH': state(state_abbrv='OH', elect_votes=17, reg_voters=7950000, voter_turn_out=0.590, vote_prob_dem=0.44, vote_prob_repub=0.52, party = party),
    'OK': state(state_abbrv='OK', elect_votes=7, reg_voters=2224000, voter_turn_out=0.523, vote_prob_dem=0.36, vote_prob_repub=0.61, party = party),
    'OR': state(state_abbrv='OR', elect_votes=8, reg_voters=2913000, voter_turn_out=0.727, vote_prob_dem=0.58, vote_prob_repub=0.37, party = party),
    'PA': state(state_abbrv='PA', elect_votes=19, reg_voters=8897000, voter_turn_out=0.620, vote_prob_dem=0.49, vote_prob_repub=0.47, party = party),
    'RI': state(state_abbrv='RI', elect_votes=4, reg_voters=807000, voter_turn_out=0.545, vote_prob_dem=0.60, vote_prob_repub=0.36, party = party),
    'SC': state(state_abbrv='SC', elect_votes=9, reg_voters=3686000, voter_turn_out=0.612, vote_prob_dem=0.43, vote_prob_repub=0.55, party = party),
    'SD': state(state_abbrv='SD', elect_votes=3, reg_voters=615000, voter_turn_out=0.645, vote_prob_dem=0.34, vote_prob_repub=0.63, party = party),
    'TN': state(state_abbrv='TN', elect_votes=11, reg_voters=5094000, voter_turn_out=0.558, vote_prob_dem=0.40, vote_prob_repub=0.57, party = party),
    'TX': state(state_abbrv='TX', elect_votes=40, reg_voters=17200000, voter_turn_out=0.580, vote_prob_dem=0.46, vote_prob_repub=0.50, party = party),
    'UT': state(state_abbrv='UT', elect_votes=6, reg_voters=1780000, voter_turn_out=0.647, vote_prob_dem=0.33, vote_prob_repub=0.60, party = party),
    'VT': state(state_abbrv='VT', elect_votes=3, reg_voters=514000, voter_turn_out=0.724, vote_prob_dem=0.60, vote_prob_repub=0.33, party = party),
    'VA': state(state_abbrv='VA', elect_votes=13, reg_voters=5935000, voter_turn_out=0.610, vote_prob_dem=0.51, vote_prob_repub=0.46, party = party),
    'WA': state(state_abbrv='WA', elect_votes=12, reg_voters=5016000, voter_turn_out=0.738, vote_prob_dem=0.58, vote_prob_repub=0.37, party = party),
    'WV': state(state_abbrv='WV', elect_votes=4, reg_voters=1255000, voter_turn_out=0.550, vote_prob_dem=0.31, vote_prob_repub=0.65, party = party),
    'WI': state(state_abbrv='WI', elect_votes=10, reg_voters=3650000, voter_turn_out=0.735, vote_prob_dem=0.49, vote_prob_repub=0.47, party = party),
    'WY': state(state_abbrv='WY', elect_votes=3, reg_voters=289000, voter_turn_out=0.579, vote_prob_dem=0.25, vote_prob_repub=0.69, party = party),
}
