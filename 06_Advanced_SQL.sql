Return the team names and the number of players in each team, all sorted by the number of players in each team, from the highest to the lowest.

SELECT t.name, COUNT(*) as nb_players FROM wizard as w
JOIN player as p ON w.id = p.wizard_id
JOIN team as t ON p.team_id = t.id
GROUP BY t.id
ORDER BY nb_players DESC;

Return the names of complete teams only (14 players or more, that is to say a minimum of 7 players and 7 substitute players), sorted by alphabetical order.

SELECT t.name, COUNT(*) as nb_players FROM wizard as w
JOIN player as p ON w.id = p.wizard_id
JOIN team as t ON p.team_id = t.id
GROUP BY t.id
HAVING nb_players > 14
ORDER BY t.name ASC;

Gryffondor’s trainer is superstitious, his favorite day is Monday. Return a list of players in his team who were enrolled on a Monday (they want them to play first) and sort the results by enrollment date.

SELECT firstname, lastname, t.name, p.enrollment_date as enrolled_monday FROM wizard as w
JOIN player as p ON w.id = p.wizard_id
JOIN team as t ON p.team_id = t.id
WHERE t.name = 'Gryffindor'
HAVING WEEKDAY(enrolled_monday)=0
ORDER BY enrollment_date ASC;
