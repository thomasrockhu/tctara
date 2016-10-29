import math
import random


def tara():
    numbers = [random.randint(2, 20) for _ in range(random.randint(4, 8) * 2)]
    print 'X\tY'
    X = []
    Y = []
    for (index, number) in enumerate(numbers):
        if index % 2 == 0:
            X.append(number)
        else:
            Y.append(number)

    for index in range(len(X)):
        print '{}\t{}'.format(X[index], Y[index])
    print

    mean = 1.0 * sum(numbers) / len(numbers)
    print 'Mean of the entire set: {:.4f}'.format(mean)

    SD = sum([(i - mean) * (i - mean) for i in numbers]) / len(numbers)
    print 'Standard deviation of the entire set: {:.4f}'.format(SD)

    n = len(numbers) / 2
    sumxx = sum([X[i] * X[i] for i in range(len(X))])
    sumyy = sum([Y[i] * Y[i] for i in range(len(Y))])
    sumxy = sum([X[i] * Y[i] for i in range(len(X))])
    rxy = ((n * sumxy) - (sum(X) * sum(Y))) / (math.sqrt(((n * sumxx) - (sum(X) * sum(X))) * ((n * sumyy) - (sum(Y) * sum(Y)))))
    print 'Pearson correlation for X and Y: {:.4f}'.format(rxy)

    rxx = (2 * rxy) / (1 + rxy)
    print 'Spearman-Brown coefficient: {:.4f}'.format(rxx)

    sem = SD * (math.sqrt(1 - rxx))
    print 'Standard Error of Measurement: {:.4f}'.format(sem)
    return {
        'SD': SD,
        'X': X,
        'Y': Y,
        'mean': mean,
        'rxx': rxx,
        'rxy': rxy,
        'sem': sem,
    }
