USE March_Mad;

/* Get a look at the ordinal ranks for teams between 2005 & 2008 */
SELECT m.TeamID, t.TeamName, m.Season, m.OrdinalRank
FROM mmasseyordinals as m
INNER JOIN mteams as t ON m.TeamID = t.TeamID
WHERE m.Season >= 2005 AND m.Season <= 2008
ORDER BY m.OrdinalRank

/* Winner Games */
SELECT t.TeamName, m.Wscore, m.LScore
FROM mregularseasondetailedresults as m
INNER JOIN mteams as t ON m.WTeamID = t.TeamID
WHERE m.Season = 2022

/* Losser Games */
SELECT t.TeamName, m.Lscore, m.Wscore
FROM pleasework as m
INNER JOIN mteams as t ON m.LTeamID = t.TeamID
WHERE m.Season = 2022










