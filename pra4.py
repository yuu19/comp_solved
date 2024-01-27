X = int(input())
ans = 0
now = 1
while X > 0:
  if now > X:
    break
  tmp, _ = divmod(X, now)
  ans += tmp
  now *= 10

print(ans)