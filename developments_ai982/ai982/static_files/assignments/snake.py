import numpy as np
from ple import PLE
from ple.games.snake import Snake


agent = Snake(width=256, height=256)


env = PLE(agent, fps=15, force_fps=False, display_screen=True)

env.init()
actions = env.getActionSet()
for i in range(1000):
    if env.game_over():
        env.reset_game()

    action = actions[np.random.randint(0, len(actions))]
    env.act(action)
