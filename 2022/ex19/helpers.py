import dataclasses

from ortools.sat.python import cp_model

from utils.readlines import LineInterface

ress = ['geode', 'obsidian', 'clay', 'ore']


@dataclasses.dataclass
class Blueprint2:
    bid: int
    ore_ore: int
    clay_ore: int
    obsidian_ore: int
    obsidian_clay: int
    geode_ore: int
    geode_obsidian: int

    def add_resource(self, typ, count, ore, clay, obsidian, geode):
        if typ == 'ore':
            return ore + count, clay, obsidian, geode
        if typ == 'clay':
            return ore, clay + count, obsidian, geode
        if typ == 'obsidian':
            return ore, clay, obsidian + count, geode
        if typ == 'geode':
            return ore, clay, obsidian, geode + count

    def get_config_value(self, robots, ore, clay, obsidian, geode, cc):
        cc = 1
        ore_val = 1000
        clay_val = self.clay_ore
        obsidian_val = self.obsidian_ore + self.obsidian_clay * clay_val
        geode_val = self.geode_obsidian * obsidian_val + self.geode_ore
        ss = robots['ore'] * cc + ore + (robots['clay'] * cc + clay) * clay_val + (
            robots['obsidian'] * cc + obsidian) * obsidian_val + (robots['geode'] * cc + geode) * geode_val
        # ss = robots['ore'] + ore + clay + obsidian + geode + (robots['clay']) * clay_val + (
        #         robots['obsidian']) * obsidian_val + (robots['geode']) * geode_val

        # ss = ore + clay * clay_val + obsidian * obsidian_val + geode * geode_val
        return ss

    def robots_to_config(self, robots, ore, clay, obsidian, geode):
        # return tuple([robots[r] for r in ress] + [ore, clay, obsidian, geode])
        return tuple([robots[r] for r in ress])

    def get_most_geodes(self, minutes=24):
        vv = {k: 0 for k in ress}
        vv['ore'] = 1
        q = [(1, vv, 0, 0, 0, 0)]
        bests = {}
        tt = 0
        while True:
            turn, robots, ore, clay, obsidian, geode = q.pop(0)

            if tt < turn:
                tt += 1
                q = sorted(q, key=lambda x: self.get_config_value(x[1], x[2], x[3], x[4], x[5], minutes - x[0]), reverse=True)[:5000]

            # print(turn, robots, ore, clay, obsidian, geode)
            if turn > minutes:
                break

            left = minutes - turn

            new_ore, new_clay, new_obsidian, new_geode = ore, clay, obsidian, geode

            for robot in robots:
                new_ore, new_clay, new_obsidian, new_geode = self.add_resource(robot, robots[robot], new_ore, new_clay,
                                                                               new_obsidian, new_geode)

            val = self.get_config_value(robots, new_ore, new_clay, new_obsidian, new_geode, left)
            k = self.robots_to_config(robots, new_ore, new_clay, new_obsidian, new_geode)
            # if val >= bests.get(k, 0):
            #     q.append((turn + 1, robots, new_ore, new_clay, new_obsidian, new_geode))
            q.append((turn + 1, robots, new_ore, new_clay, new_obsidian, new_geode))

            if ore >= self.geode_ore and obsidian >= self.geode_obsidian:
                new_robots = robots.copy()
                new_robots['geode'] += 1
                val = self.get_config_value(new_robots, new_ore - self.geode_ore, new_clay,
                                            new_obsidian - self.geode_obsidian, new_geode, left)
                k = self.robots_to_config(new_robots, new_ore - self.geode_ore, new_clay,
                                          new_obsidian - self.geode_obsidian, new_geode)
                # if val >= bests.get(k, 0):
                #     bests[k] = val
                #     q.append((turn + 1, new_robots, new_ore - self.geode_ore, new_clay,
                #               new_obsidian - self.geode_obsidian, new_geode))
                q.append((turn + 1, new_robots, new_ore - self.geode_ore, new_clay,
                          new_obsidian - self.geode_obsidian, new_geode))

            if ore >= self.obsidian_ore and clay >= self.obsidian_clay:
                new_robots = robots.copy()
                new_robots['obsidian'] += 1
                val = self.get_config_value(new_robots, new_ore - self.obsidian_ore, new_clay - self.obsidian_clay,
                                            new_obsidian,
                                            new_geode, left)
                k = self.robots_to_config(new_robots, new_ore - self.obsidian_ore, new_clay - self.obsidian_clay,
                                          new_obsidian,
                                          new_geode)
                # if val >= bests.get(k, 0):
                #     bests[k] = val
                #     q.append((
                #         turn + 1, new_robots, new_ore - self.obsidian_ore, new_clay - self.obsidian_clay, new_obsidian,
                #         new_geode))

                q.append((
                    turn + 1, new_robots, new_ore - self.obsidian_ore, new_clay - self.obsidian_clay, new_obsidian,
                    new_geode))
            if ore >= self.clay_ore:
                new_robots = robots.copy()
                new_robots['clay'] += 1
                val = self.get_config_value(new_robots, new_ore - self.clay_ore, new_clay, new_obsidian, new_geode,
                                            left)
                k = self.robots_to_config(new_robots, new_ore - self.clay_ore, new_clay, new_obsidian, new_geode)
                # if val >= bests.get(k, 0):
                #     bests[k] = val
                #     q.append((turn + 1, new_robots, new_ore - self.clay_ore, new_clay, new_obsidian, new_geode))
                q.append((turn + 1, new_robots, new_ore - self.clay_ore, new_clay, new_obsidian, new_geode))

            if ore >= self.ore_ore:
                new_robots = robots.copy()
                new_robots['ore'] += 1
                val = self.get_config_value(new_robots, new_ore - self.ore_ore, new_clay, new_obsidian, new_geode, left)
                k = self.robots_to_config(new_robots, new_ore - self.ore_ore, new_clay, new_obsidian, new_geode)
                # if val >= bests.get(k, 0):
                #     bests[k] = val
                #     q.append((turn + 1, new_robots, new_ore - self.ore_ore, new_clay, new_obsidian, new_geode))
                q.append((turn + 1, new_robots, new_ore - self.ore_ore, new_clay, new_obsidian, new_geode))

        # print(q)
        els = sorted(q, key=lambda x: x[5], reverse=True)
        # print(els[:5])
        return els[0][5]

    def get_value(self, minutes=24):
        v = self.get_most_geodes(minutes)
        print(self.bid, v)
        return v * self.bid


def summ(x, y):
    return tuple(sum(x) for x in zip(x, y))


@dataclasses.dataclass
class Blueprint:
    bid: int
    ore_ore: int
    clay_ore: int
    obsidian_ore: int
    obsidian_clay: int
    geode_ore: int
    geode_obsidian: int

    def get_config_value(self, vals):
        # ore_val = 1
        # clay_val = self.clay_ore
        # obsidian_val = self.obsidian_ore + self.obsidian_clay * clay_val
        # geode_val = self.geode_obsidian * obsidian_val + self.geode_ore

        # ore_val = self.geode_ore +
        # clay_val = self.clay_ore
        # obsidian_val = self.geode_obsidian
        # geode_val = ore_val + clay_val + obsidian_val

        # ore_val = 1 / self.geode_ore
        # clay_val = 1 / self.obsidian_clay
        # obsidian_val = 1 / self.geode_obsidian
        # geode_val = 1
        # ss = sum([vals[i] * uu for i, uu in enumerate([ore_val, clay_val, obsidian_val, geode_val])])

        # ss = vals[-1] + vals[0] / self.geode_ore + vals[2] / self.geode_obsidian
        ss = vals[-1], vals[0], vals[2], vals[1]

        # ss = vals[-1] + max(vals[0] / self.geode_ore, vals[2] / self.geode_obsidian) + vals[1] / self.obsidian_clay / self.geode_obsidian

        return ss

    # def get_config_value(self, vals):
    #     return tuple(reversed(vals))

    def lowere(self, e1, e2):
        for i, x in enumerate(e1):
            if x > e2[i]:
                return False
        return True

    def substr(self, e1, e2):
        return tuple(e1[i] - e2[i] for i in range(len(e1)))

    def get_most_geodes(self, minutes=24):
        costs = {
            (1, 0, 0, 0): (self.ore_ore, 0, 0, 0),
            (0, 1, 0, 0): (self.clay_ore, 0, 0, 0),
            (0, 0, 1, 0): (self.obsidian_ore, self.obsidian_clay, 0, 0),
            (0, 0, 0, 1): (self.geode_ore, 0, self.geode_obsidian, 0),
            (0, 0, 0, 0): (0, 0, 0, 0),
        }
        dyna = {
            0: {
                (1, 0, 0, 0): [(0, 0, 0, 0)]
            }
        }
        for i in range(1, minutes + 1):
            dyna[i] = {}
            for current_robots in dyna[i - 1]:
                for configuration in dyna[i - 1][current_robots]:
                    monies = configuration
                    for robot_tuple in costs:
                        cost = costs[robot_tuple]
                        if self.lowere(cost, monies):
                            new_robots = summ(current_robots, robot_tuple)
                            monies_after_buying_robot = summ(self.substr(monies, cost), current_robots)
                            val = self.get_config_value(monies_after_buying_robot)
                            curr_val = self.get_config_value(dyna[i].get(new_robots, [(0, 0, 0, 0)])[0])
                            if curr_val == val:
                                if new_robots not in dyna[i]:
                                    dyna[i][new_robots] = []
                                dyna[i][new_robots].append(monies_after_buying_robot)
                            elif curr_val < val:
                                dyna[i][new_robots] = [monies_after_buying_robot]
            # print(i, dyna[i])
        kk = max(dyna[minutes], key=lambda x: dyna[minutes][x][-1])
        # print(kk, dyna[minutes][kk])
        a = sorted([sorted(dyna[24][x], key=lambda y: y[-1])[-1][-1] for x in dyna[24]], reverse=True)
        return a[0]

    def get_value(self, minutes=24):
        v = self.get_most_geodes(minutes)
        print(self.bid, v)
        return v * self.bid


@dataclasses.dataclass
class Blueprint3:
    bid: int
    ore_ore: int
    clay_ore: int
    obsidian_ore: int
    obsidian_clay: int
    geode_ore: int
    geode_obsidian: int

    def add_resource(self, typ, count, ore, clay, obsidian, geode):
        if typ == 'ore':
            return ore + count, clay, obsidian, geode
        if typ == 'clay':
            return ore, clay + count, obsidian, geode
        if typ == 'obsidian':
            return ore, clay, obsidian + count, geode
        if typ == 'geode':
            return ore, clay, obsidian, geode + count

    def get_most_geodes(self, minutes=24):
        model = cp_model.CpModel()
        inf = 2137213721
        u = {}
        resources = {}
        robots = {}

        for r in ress:
            k = f'{r}_1'
            # resources[k] = model.NewIntVar(0, 1000, 'res_' + k)
            resources[k] = 0
            if r != 'ore':
                # robots[k] = model.NewIntVar(0, 1000, 'robot_' + k)
                robots[k] = 0

        k = 'ore_1'
        # robots[k] = model.NewIntVar(0, 1000, 'robot_' + k)
        robots[k] = 1

        for i in range(2, minutes + 2):
            for r in ress:
                k = f'{r}_{i}'
                pk = f'{r}_{i - 1}'
                resources[k] = model.NewIntVar(0, 1000, 'res_' + k)
                robots[k] = model.NewIntVar(0, 1000, 'robot_' + k)

            k = f'ore_{i}'
            pk = f'ore_{i - 1}'
            model.Add(robots[pk] <= robots[k])
            model.Add(1000 * robots[k] <= 1000 * robots[pk] + (1000 + (resources[k] - self.ore_ore)))

            k = f'clay_{i}'
            pk = f'clay_{i - 1}'
            model.Add(robots[pk] <= robots[k])
            model.Add(1000 * robots[k] <= 1000 * robots[pk] + (1000 + (resources[f'ore_{i}'] - self.clay_ore)))

            k = f'obsidian_{i}'
            pk = f'obsidian_{i - 1}'
            model.Add(robots[pk] <= robots[k])
            model.Add(1000 * robots[k] <= 1000 * robots[pk] + (1000 + (resources[f'ore_{i}'] - self.obsidian_ore)))
            model.Add(1000 * robots[k] <= 1000 * robots[pk] + (1000 + (resources[f'clay_{i}'] - self.obsidian_clay)))

            k = f'geode_{i}'
            pk = f'geode_{i - 1}'
            model.Add(robots[pk] <= robots[k])
            model.Add(1000 * robots[k] <= 1000 * robots[pk] + (1000 + (resources[f'ore_{i}'] - self.geode_ore)))
            model.Add(
                1000 * robots[k] <= 1000 * robots[pk] + (1000 + (resources[f'obsidian_{i}'] - self.geode_obsidian)))

        model.Maximize(resources[f'geode_24'])

        solver = cp_model.CpSolver()
        status = solver.Solve(model)

        print(f'status is {"optimal" if status == cp_model.OPTIMAL else "feasible or not"}')
        print(f'number of nanobots in range: {solver.ObjectiveValue()}')

        return 0

    def get_value(self, minutes=24):
        return self.get_most_geodes(minutes) * self.bid


class Line(LineInterface):
    def __init__(self, line: str):
        super().__init__(line)
