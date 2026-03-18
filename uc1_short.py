def avg_age(users):
    tot = 0
    cnt = 0
    for u in users:
        if u.get('act'):
            age = u.get('age', 0)
            if age > 0:
                tot += age
                cnt += 1
    return tot / cnt if cnt else 0.0
