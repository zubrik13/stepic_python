"""
Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча
и выводит на стандартный вывод сводную таблицу результатов всех матчей.
За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число n — количество завершенных игр.
После этого идет строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Конкретный пример ввода-вывода приведён ниже.
3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15

Порядок вывода команд произвольный.
"""


class Team:
    def __init__(self, name):
        self.name = name
        self.total_games = 0
        self.wins = 0
        self.ties = 0
        self.loss = 0
        self.score = 0

    def as_list(self):
        return [
            self.total_games,
            self.wins,
            self.ties,
            self.loss,
            self.score
        ]

    def __str__(self):
        return f"{self.name}: {' '.join(map(str, self.as_list()))}"

    @staticmethod
    def update_results(team_a, team_b, score_a, score_b):
        team_a.total_games += 1
        team_b.total_games += 1
        if score_a > score_b:
            team_a.wins += 1
            team_b.loss += 1
            team_a.score += 3
        elif score_a == score_b:
            team_a.ties += 1
            team_b.ties += 1
            team_a.score += 1
            team_b.score += 1
        else:
            team_b.wins += 1
            team_a.loss += 1
            team_b.score += 3


# read input
games = int(input())
inp = []
for i in range(games):
    inp.append(input().split(";"))

# inp = [['Спартак', '9', 'Зенит', '10'], ['Локомотив', '12', 'Зенит', '3'], ['Спартак', '8', 'Локомотив', '15']]

teams = {}

for i in inp:
    teams[i[0]] = Team(i[0])
    teams[i[2]] = Team(i[2])


for i in inp:
    team1 = teams[i[0]]
    team2 = teams[i[2]]
    score1 = int(i[1])
    score2 = int(i[3])
    Team.update_results(team1, team2, score1, score2)

for t in teams.values():
    print(t)
