def bouncing_ball(h, bounce, window):
    if h > 0 and bounce < 1 and bounce > 0 and window < h:
        count = 1
        while h * bounce > window:
            h *= bounce
            if h > window: count += 1
            count += 1
        return count
    else: return -1

bouncing_ball(2, 0.5, 1)