import gym


env = ''
env = gym.make(env)
env.reset()
for _ in range(100000):
    env.render()
    env.step(env.action_space.sample())  # take a random action
env.close()
