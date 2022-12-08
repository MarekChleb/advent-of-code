import sys
from glob import glob
from typing import List

import parse

from helpers import Line
from utils.readlines import read_lines

print(sys.setrecursionlimit(20000))


def get_solution(lines: List[Line]) -> str:
    dir_hist = []
    dirs = {}
    lss = False
    lsed = set()
    sums = {}

    # def get_sum(i):
    #     if i in sums:
    #         return sums[i]
    #     summ = 0
    #     for p in dirs.get(i, []):
    #         if p[0] == 'dir':
    #             summ += get_sum(p[1])
    #             continue
    #         summ += p[2]
    #     sums[i] = summ
    #     return summ

    def get_sum(i):
        q = [('dir', i)]
        prev = i
        curr_dir = i
        visited = set()
        while len(q) > 0:
            curr = q.pop()
            if curr[0] == 'dir':
                curr_dir = curr[1]
                if curr_dir in visited:
                    continue
                print(curr_dir)

                if curr_dir not in sums:
                    sums[curr_dir] = 0
                    q += dirs[curr_dir]

                # visited.add(curr_dir)
            else:
                val = curr[2]
                sums[curr_dir] += val



    blank_sums = {}

    solution = 0
    cded = set()
    for line in lines:
        raw = line.raw_line
        if line.raw_line.startswith('$ cd'):
            lss = False
            dirr = parse.parse('$ cd {}', raw)
            dirr = dirr[0]
            if dirr not in cded:
                cded.add(dirr)
            elif dirr != '..':
                print('already been here', dirr)
            if dirr == '..':
                dir_hist.pop()
            else:
                dir_hist.append(dirr)
                blank_sums[dirr] = 0
            continue
        if raw.startswith('$ ls'):
            # dirr = dir_hist[-1]
            # if dirr in lsed:
            #     lss = False
            #     continue
            # lsed.add(dirr)
            # lss = True
            # blank_sums[dirr] = 0
            continue

        # if not lss:
        #     continue
        current_dir = dir_hist[-1]
        if current_dir not in dirs:
            dirs[current_dir] = []
        if raw.startswith('dir'):
            dirr = parse.parse('dir {}', raw)
            dirr = dirr[0]
            dirs[current_dir].append(('dir', dirr))
            continue

        size, dirr = parse.parse('{} {}', raw)
        size = int(size)
        dirs[current_dir].append(('file', dirr, size))
        for i, d in enumerate(dir_hist):
            k = '-'.join(dir_hist[:i+1])
            if k not  in blank_sums:
                blank_sums[k] = 0
            blank_sums['-'.join(dir_hist[:i+1])] += size
        print(dir_hist, size)
        # blank_sums[current_dir] += size

    print(dirs)
    # get_sum('/')
    print(blank_sums)
    solution = sum([blank_sums[ss] for ss in blank_sums if blank_sums[ss] <= 100000])
    return str(solution)


for filename in glob('input/*.in'):


    input_lines = read_lines(Line, filename)
    print(filename, get_solution(input_lines))
