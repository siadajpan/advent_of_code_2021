import copy
import time
from dataclasses import dataclass
from typing import Tuple, List

import numpy as np

import utils.file_io



def part_1(data):
    def _move(pos, dice, score):
        pos = (pos + sum(dice) - 1) % 10 + 1
        score += pos
        return pos, score
    print(data)
    pos_1, pos_2 = data
    score_1, score_2 = 0, 0
    dice = np.array([1, 2, 3])
    throws = 3
    while True:
        pos_1, score_1 = _move(pos_1, dice, score_1)
        if score_1 >= 1000:
            break
        dice = np.mod(dice + 3, 100)
        throws += 3
        print(pos_1, score_1, dice)
        pos_2, score_2 = _move(pos_2, dice, score_2)
        if score_2 >= 1000:
            break
        dice = np.mod(dice + 3, 100)
        throws += 3
        print(pos_2, score_2, dice)
        # if throws > 10:
        #     break

    print(min(score_1, score_2)* throws)


def part_2(data):
    pos_1, pos_2 = data

    @dataclass
    class State:
        score: List[int]
        positions: List[int]
        turn: int
        routes: int = 1
        won: bool = False

        def __eq__(self, other):
            same_score = self.score[0] == other.score[0] and self.score[1] == other.score[1]
            same_positions = self.positions[0] == other.positions[0] and self.positions[1] == other.positions[1]
            same_turn = self.turn == other.turn
            return same_score and same_positions and same_turn

        @property
        def id(self):
            return f'{self.score[0]}_{self.score[1]}_{self.positions[0]}_{self.positions[1]}_{self.turn}'

    new_state = State(score=[0, 0], positions=[pos_1, pos_2], turn=0)
    states = {new_state.id: new_state}

    while True:
        not_won_states = [s for s in states.values() if not s.won]
        print(len(not_won_states))
        if len(not_won_states) == 0:
            break

        for state in not_won_states:
            for throw in range(3, 10):
                if throw in [3, 9]:
                    universes = 1
                elif throw in [4, 8]:
                    universes = 3
                elif throw in [5, 7]:
                    universes = 6
                elif throw == 6:
                    universes = 7

                new_state = copy.deepcopy(state)
                new_state.routes *= universes
                new_state.positions[state.turn] = (state.positions[state.turn] + throw - 1) % 10 + 1
                new_state.score[state.turn] += new_state.positions[state.turn]
                new_state.turn = 1 - state.turn

                if new_state.score[state.turn] >= 21:
                    new_state.won = True

                state_id = new_state.id
                state_search = states.get(state_id)
                if state_search is not None:
                    state_search.routes += new_state.routes
                else:
                    states[state_id] = new_state
            states.pop(state.id)

    # for state in states:
    #     print(state)

    print(sum([s.routes for s in states.values() if s.score[0] > s.score[1]]))
    print(sum([s.routes for s in states.values() if s.score[1] > s.score[0]]))



if __name__ == '__main__':
    DATA = utils.file_io.read_file('input.txt')
    data = [int(d.split(': ')[1]) for d in DATA]
    part_1(data)
    part_2(data)
