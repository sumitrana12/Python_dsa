A, B, C = map(int, input().split())
if C > B > A:
    print("Increasing")
elif A < B < C:
    print("Decreasing")
else:
    print("Neither")