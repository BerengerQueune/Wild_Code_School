Return lastnames, firstnames, each player’s role and team, arranged in alphabetical order by team, then by role in the team, then by lastname, and finally by firstname.

SELECT lastname, firstname, player.role, team.name FROM wizard
JOIN player ON wizard.id = player.wizard_id
JOIN team ON player.team_id = team.id
ORDER BY team.name ASC, role ASC, lastname ASC, firstname ASC;

Return only the lastnames and firstnames of players who play the role of seeker, sorted by lastname and then firstname in alphabetical order.

SELECT lastname, firstname FROM wizard
JOIN player ON wizard.id = player.wizard_id WHERE player.role = 'seeker'
ORDER BY lastname ASC, firstname ASC;

Return a list of all of the wizards who do not play quidditch.

SELECT lastname, firstname FROM wizard
LEFT JOIN player ON wizard.id = player.wizard_id WHERE player.role IS NULL;



------------------ 

CREATE TABLE `wizard` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `firstname` VARCHAR(80) NOT NULL,
  `lastname` VARCHAR(80) NOT NULL,
  CONSTRAINT fk_wizard_player
FOREIGN KEY (id) REFERENCES player(id),
  PRIMARY KEY (`id`)
);

CREATE TABLE `player` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `wizard_id` INT NOT NULL,
  `team_id` INT NOT NULL,
  CONSTRAINT fk_player_team
	FOREIGN KEY (wizard_id) REFERENCES team(id),
    CONSTRAINT fk_wizard_noref
	FOREIGN KEY (team_id) REFERENCES team(id),
      `role` VARCHAR(50) NOT NULL,
  `enrollment_date` DATE NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `team` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`)
);
