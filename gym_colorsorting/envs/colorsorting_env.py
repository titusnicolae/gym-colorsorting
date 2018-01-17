import gym
from gym import error, spaces, utils
from gym.utils import seeding
from gym import spaces
from random import randint
import numpy as np

class ColorSortingEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    self.action_space = spaces.Discrete(4)
    self.width = 14
    self.height = 14
    self.state = (self.height/2, self.width/2)
    self.ll = []
    self.count = 0
    self._reset()

  def _step(self, action):
    self.count +=1
    """
    self.state = {
        0: ((self.state[0]+1)%self.width, self.state[1]),
        1: ((self.state[0]-1)%self.width, self.state[1]),
        2: (self.state[0], (self.state[1]+1)%self.height),
        3: (self.state[0], (self.state[1]-1)%self.height),
    }[action]
    """
    self.state = {
        0: (self.state[0]+1, self.state[1]),
        1: (self.state[0]-1, self.state[1]),
        2: (self.state[0], self.state[1]+1),
        3: (self.state[0], self.state[1]-1),
    }[action]

    done = self.state[0]<0 or self.state[1]<0 or self.state[0]>=self.height or self.state[1]>=self.width

    return (self._render, 1 if not done else -3, done, {"lengths": self.ll})

  def _reset(self):
    if len(self.ll)<1000: 
      self.ll.append(self.count)
    else: 
      self.ll=self.ll[1:]+[self.count]
    self.count=0
    self.state = (randint(1, self.height-2), randint(1, self.width-2))

  def _render(self, mode='human', close=False):
    scene = np.zeros((self.height, self.width), dtype=np.uint8)

    if 0<=self.state[0] and 0<=self.state[1] and self.state[0]<self.height and self.state[1]<self.width:
        scene[self.state[0], self.state[1]] = 255
      

    return resize(scene, 6)

def resize(mat, scale):
    ret = np.zeros((mat.shape[0]*scale, mat.shape[1]*scale), dtype=np.uint8)
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):    
            ret[i*scale:(i+1)*scale, j*scale:(j+1)*scale] = mat[i, j]
    return ret
