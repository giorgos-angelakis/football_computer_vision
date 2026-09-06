import sys
sys.path.append('.../')
from utils import get_center_of_bbox, measure_disctance

class PlayerBallAssigner():
    def __init__(self):
        self.max_player_ball_distance = 70

    def assigne_ball_to_player(self, players, ball_bbox):

        minimum_distance = 9999
        assigned_player = -1

        ball_pos = get_center_of_bbox(ball_bbox)
        for player_id, player in players.items():
            player_bbox = player['bbox']
            distance_left = measure_disctance((player_bbox[0], player_bbox[-1]), ball_pos)
            distance_right = measure_disctance((player_bbox[2], player_bbox[-1]), ball_pos)
            distance = min(distance_right, distance_left)
            
            if (distance < self.max_player_ball_distance) and (distance < minimum_distance):
                minimum_distance = distance
                assigned_player = player_id

        return assigned_player




