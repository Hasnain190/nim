from nim import NimAI  
    
    # Tests that the method returns 0 when self.q is empty
def test_empty_q():
        ai = NimAI()
        state = [1, 1, 4, 4]
        action = (2, 3)
        q_value = ai.get_q_value(state, action)
        assert q_value == 0
        
    # Tests that the method returns the correct Q-value for a state and action that exists in self.q
def test_q_value_exists():
        ai = NimAI()
        ai.q = {((1, 1, 4, 4), (1, 2)): 10, ((2, 2, 3, 3), (2, 3)): 5}
        state = [1, 1, 4, 4]
       
        action = (1, 2)
        assert ai.get_q_value(state, action) == 10
        
    # Tests that the Q-value is updated correctly with positive values for old_q, reward, and future_rewards
# def test_update_q_value_positive_values():
#         ai = NimAI()
#         state = [1, 2, 3]
#         action = (0, 1)
#         old_q = 0.5
#         reward = 1.0
#         future_rewards = 0.8

#         ai.update_q_value(state, action, old_q, reward, future_rewards)
#         print((0.5 + (0.5 * (1.0 + 0.8))))

#         assert ai.q[(tuple(state), action)] == 0.5 +( 0.5 * (1.0 + 0.8))
        
        

def test_best_future_reward( ):
        """
        Given a state `state`, consider all possible `(state, action)`
        pairs available in that state and return the maximum of all
        of their Q-values.

        Use 0 as the Q-value if a `(state, action)` pair has no
        Q-value in `self.q`. If there are no available actions in
        `state`, return 0.
        """
        # first we will find all the available actions in a given state
        # find the q-values for these action,state pairs
        # choose the max
        ai = NimAI()
        state  = [0,0,2]
        # print(list( enumerate(state)) )
        state_action_pairs = set()
        for i, remaining in enumerate(state):
            for j in range(1, remaining +1):
                state_action_pairs.add((i, j))
        # print(state_action_pairs)
        # assert list(state_action_pairs) ==  [(2,1),(2,2)]
        
        q_values = []
        for pair in list(state_action_pairs):
            q_values.append(ai.q.get(pair,0) )
        # print(q_values)
        # assert q_values  == [0,0]
        
        # q_values = []
        max_q = max(q_values)
        
        best_action_index = list(state_action_pairs).index(max_q)
        
        best_action =  list(state_action_pairs)[best_action_index]
        
        return best_action
            
            
        
        