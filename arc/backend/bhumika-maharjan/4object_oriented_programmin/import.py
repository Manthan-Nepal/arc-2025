import sys
import os

day3_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'day_3'))
sys.path.append(day3_path)

import mathoperation as mp

print(mp.add(5, 6))
