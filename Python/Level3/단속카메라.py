def solution(routes):
    answer = 1
    routes = sorted(routes, key=lambda x: (x[1], x[0]))
    cam = routes[0][1]

    for route in routes:
        if cam < route[0]:
            cam = route[1]
            answer += 1

    return answer