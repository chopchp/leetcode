class Solution:
  def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
    S = sum(x for x in A if x % 2 == 0)
    ans = []
    for val, index in queries:
      if A[index] % 2 == 0: S -= A[index]
      A[index] += val
      if A[index] % 2 == 0: S += A[index]
      ans.append(S)
    return ans
