import numpy as np
import matplotlib.pyplot as plt
import random as rnd

COORDS = 15
N = int(input('N (count of points): '))
M = int(input('M (count of coords): '))
points = generation_points(N, M)
pareto_front = get_pareto_front(N, M, points)
show_points(M, points, pareto_front)
def p1_is_dominant(point1, point2):
    return (point1 - point2).min() >= 0
def generation_points(N, M):
    points = []
    for i in range(N):
        point = []
        for j in range(M):
            point.append(rnd.randint(-COORDS, COORDS))
        points.append(np.array(point))
    return points
def get_pareto_front(N, M, points):
    pareto_front = []
    mark_points = np.zeros(N)
    for i in range(N):
        if mark_points[i] != -1:
            is_optimal = True
            for k in range(N):
                if mark_points[k] not in [-1, 1] and i != k:
                    if p1_is_dominant(points[k], points[i]):
                        is_optimal = False
                        break
                    if p1_is_dominant(points[i], points[k]):
                        mark_points[k] = -1
            if is_optimal:
                pareto_front.append(points[i])
                mark_points[i] = 1
            else:
                mark_points[i] = -1
    return pareto_front
def show_points(M, points, pareto_front):
    plt.title("Отображение Парето фронт")
    plt.xlabel("Номер координаты точки")
    plt.ylabel("Значение координаты точки")
    plt.grid()
    coords = np.arange(M)
    for point in points:
        plt.plot(coords, point, 'D--')
    for pareto_point in pareto_front:
        plt.plot(coords, pareto_point, 'D-')
    plt.show()
