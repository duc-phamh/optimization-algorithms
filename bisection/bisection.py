last_left = a
last_right = b
while True:
    mid_point = (last_left + last_right)/2
    f_midpoint = f(mid_point)
    f_lastleft = f(last_left)
    
    if abs(f_midpoint) < tol:
        print(mid_point)
        break
    elif f_midpoint > 0:
        if f_lastleft > 0:
            last_left = mid_point
        else:
            last_right = mid_point
    else:
        if f_lastleft > 0:
            last_right = mid_point
        else:
            last_left = mid_point
