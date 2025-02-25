import numpy as np


class GridWorld:
    def __init__(self):
        # 操作集合
        self.action_space = [0, 1, 2, 3]
        # 操作编码
        self.action_meaning = {
            '0': 'UP',
            '1': 'DOWN',
            '2': 'LEFT',
            '3': 'RIGHT'
        }
        # 奖励
        self.reward_map = np.array([[0, 0, 0, 1], [0, 0, None, -1], [0, 0, 0, 0]])
        # 各种状态坐标
        self.reward_state = (0, 3)
        self.wall_state = (1, 1)
        self.start_state = (2, 0)
        self.agent_state = self.start_state

    @property
    def height(self):
        return len(self.reward_map)

    @property
    def width(self):
        return len(self.reward_map[0])

    @property
    def shape(self):
        return self.reward_map.shape

    def actions(self):
        return self.action_space

    def states(self):
        for h in range(self.height):
            for w in range(self.width):
                yield h, w

    def next_state(self,state,action):
        action_move_map = [(-1,0),(1,0),(0,-1),(0,1)]
        move = action_move_map[action]
        next_state = (state[0]+move[0],state[1]+move[1])
        ny,nx=next_state

        if 0<nx or nx>self.width or 0<ny or ny>self.height:
            next_state=state
        elif next_state ==self.wall_state:
            next_state = state

        return next_state

    def reward(self,state,action,next_state):
        return self.reward_map[next_state]