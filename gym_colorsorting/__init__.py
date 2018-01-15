from gym.envs.registration import register

register(
    id='colorsorting-v0',
    entry_point='gym_colorsorting.envs:ColorSortingEnv',
)
