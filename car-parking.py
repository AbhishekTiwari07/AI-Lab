import gym
env = gym.make("Taxi-v3").env
env.reset()
env.render()

print("Action Space {}".format(env.action_space))
print("State Space {}".format(env.observation_space))

env.close()