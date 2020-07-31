import norminput
import numpy as np
import math

print("\n========================================")
print("  obst_judge Ver. 0.1 (20200601)")
print("========================================\n")

#dp = [[[[1] for i in range(1000)] for j in range(1000)] for k in range(100)]  # [通行不可=0, 通行可=1]
dp = np.ones((norminput.count_x, norminput.count_y, 150, 1), dtype=int)

for i in range(norminput.count_x):
    print("\r", i, "/", norminput.count_x, end="")
    for j in range(norminput.count_y):
        for k in range(math.ceil(norminput.data[i][j][0])):
            dp[i][j][k][0] = 0
print("\n通行可能性判定完了")