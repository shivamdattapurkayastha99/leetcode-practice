def minDistance(word1:str,word2:str):
    dp=[[0]*(len(word2)+1)for _ in range(len(word1)+1)]
    for i in range(len(word1)+1):
        for j in range(len(word2)+1):
            if i==0:
                dp[i][j]=j
            elif j==0:
                dp[i][j]=i
            elif word1[i-1]==word2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
    return dp[len(word1)][len(word2)]
word1="horse"
word2="ros"
print(minDistance(word1,word2))
