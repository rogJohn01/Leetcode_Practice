# Write your MySQL query statement below


SELECT player_id, event_date , sum(games_played) over( partition by player_id order by event_date) games_played_so_far from Activity;
