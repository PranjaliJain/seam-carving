import numpy as np
import cv2

#horizontal changes 
# DP is used to generate path with minimal cost
def horizontal(mat):
    n,m = mat.shape
    dp = [[0 for i in range(m)] for i in range(n)]
    dp[0] = mat[0]
    
    for i in range(1, n):
        for j in range(m):
            if (j != 0) and (j != m-1):
                dp[i][j] = mat[i][j] + min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])
            elif j == 0:
                dp[i][j] = mat[i][j] + min(dp[i-1][j], dp[i-1][j+1])
            else:
                dp[i][j] = mat[i][j] + min(dp[i-1][j-1], dp[i-1][j])
                
    return dp[n-1].index(min(dp[n-1]))

#vertical changes
# DP is used to generate path with minimal cost
def vertical(mat):
    n,m = mat.shape
    dp = np.array([[0 for i in range(m)] for i in range(n)], dtype=float)
    dp[:,0] = mat[:,0]
    
    for j in range(1, m):
        for i in range(n):
            if (i != 0) and (i != n-1):
                dp[i][j] = mat[i][j] + min(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])
            elif i == 0:
                dp[i][j] = mat[i][j] + min(dp[i][j-1], dp[i+1][j-1])
            else:
                dp[i][j] = mat[i][j] + min(dp[i][j-1], dp[i-1][j-1])
                
    return np.where(dp[:,m-1] == min(dp[:, m-1]))[0][0]