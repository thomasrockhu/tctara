import math
import random


def tara():
    numbers = [random.randint(2, 20) for _ in range(random.randint(4, 8) * 2)]
    X = []
    Y = []
    for (index, number) in enumerate(numbers):
        if index % 2 == 0:
            X.append(number)
        else:
            Y.append(number)

    number_display = []
    for index in range(len(X)):
        number_display.append({'0': X[index], '1': Y[index]})

    mean = 1.0 * sum(numbers) / len(numbers)

    SD = math.sqrt(sum([(i - mean) * (i - mean) for i in numbers]) / (len(numbers) - 1))

    n = len(numbers) / 2
    sumxx = sum([X[i] * X[i] for i in range(len(X))])
    sumyy = sum([Y[i] * Y[i] for i in range(len(Y))])
    sumxy = sum([X[i] * Y[i] for i in range(len(X))])
    rxy = ((n * sumxy) - (sum(X) * sum(Y))) / (math.sqrt(((n * sumxx) - (sum(X) * sum(X))) * ((n * sumyy) - (sum(Y) * sum(Y)))))

    rxx = (2 * rxy) / (1 + rxy)

    sem = SD * (math.sqrt(1 - rxx))
    return {
        'SD': '{:.4f}'.format(SD),
        'mean': '{:.4f}'.format(mean),
        'number_display': number_display,
        'rxx': '{:.4f}'.format(rxx),
        'rxy': '{:.4f}'.format(rxy),
        'sem': '{:.4f}'.format(sem),
    }
