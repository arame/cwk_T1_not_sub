
import random


class Policy():
        
    def get(self):
        # Sample an action from the policy, given a state
        # The action returned here is the numerical representation
        action = random.randint(0, 3)
        return action

    # This method is the same as the above get method EXCEPT
    # one of the available actions might be ghost replacing one of (up, down, left, right)
    def get_with_available_actions(self, available_actions):
        action = random.choice(available_actions)
        return action
        