class Stat:
    def __init__(self):
        self._placement = None
        self._scores = {}

    def updateScores(self, task, points):
        if task not in self._scores:
            self._scores[task] = 0
        self._scores[task] = max(self._scores[task], points)

    def getTotalScore(self):
        return sum(self._scores.values())


class Contest:
    def __init__(self, names, task_count):
        self.place = 0
        self.stats = {}
        for name in names:
            self.stats[name] = [None, Stat(), 0]


    def add_submission(self, name, task, score):
        self.stats[name][1].updateScores(task, score)
        if self.stats[name][1].getTotalScore() > self.stats[name][2]:
            self.stats[name][0] = self.place
            self.place += 1
            self.stats[name][2] = self.stats[name][1].getTotalScore()

    def create_scoreboard(self):

        has_points = []
        no_points = []
        for name in self.stats:
            player = (self.stats[name][0], name, self.stats[name][1].getTotalScore())
            if player[2] > 0:
                has_points.append(player)
            else:
                no_points.append(player)

        has_points.sort(key=lambda x: (-x[2], x[0]))
        no_points.sort(key=lambda x: x[1])
        return [x[1:] for x in has_points + no_points]

