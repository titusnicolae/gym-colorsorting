import gym
from gym import error, spaces, utils
from gym.utils import seeding
from gym import spaces
import numpy as np

class ColorSortingEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
	self.action_space = spaces.Discrete(4)
	self.state = None
	self.width = 8
	self.height = 8
	print("init")

  def _step(self, action):
	print("step")
	self.state = {
		0: ((self.state[0]+1)%self.width, self.state[1]),
		1: ((self.state[0]-1)%self.width, self.state[1]),
		2: (self.state[0], (self.state[1]+1)%self.height),
		3: (self.state[0], (self.state[1]-1)%self.height),
	}[action]
	print(self.state)

  def _reset(self):
	self.state = (4, 4)
	print("reset")

  def _render(self, mode='human', close=False):
	print("render")
   	scene = np.zeros((self.height, self.width), dtype=np.uint8)
	scene[self.state[0], self.state[1]] = 255
	return resize(scene, 32)

def resize(mat, scale):
	ret = np.zeros((mat.shape[0]*scale, mat.shape[1]*scale), dtype=np.uint8)
	for i in range(mat.shape[0]):
		for j in range(mat.shape[1]):	
			ret[i*scale:(i+1)*scale, j*scale:(j+1)*scale] = mat[i, j]
	return ret
