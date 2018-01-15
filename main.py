#!/usr/bin/python

import gym
import gym_colorsorting
import imageio
import numpy as np

env = gym.make('colorsorting-v0')
env.reset()

images = []
for _ in range(30):
	images.append(env.render())
	env.step(env.action_space.sample())

imageio.mimsave("output.gif", images)
