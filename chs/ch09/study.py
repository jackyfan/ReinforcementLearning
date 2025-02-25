import gym

env = gym.make('CartPole-v1')

state = env.reset()
print(state)

print(env.action_space)
action = 0
next_state, reward, done, info, other = env.step(action=action)
print(next_state)
print(reward)
print(done)
print(info)
print(other)
