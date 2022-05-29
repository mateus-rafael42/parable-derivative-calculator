import matplotlib.pyplot as plt
from sympy import *

def getDerivative():
    print('This is a simple quadratic function derivative calculator, enjoy!')
    variation = Symbol('x')
    while true:
        try:
            startPoint = float(input('Type a number equal or less than 0: ').replace(',','.'))
            if startPoint == 0:
                endPoint = float(input('Type a number bigger than 0: ').replace(',','.'))
                if endPoint == 0:
                    print('{:.0f} is not bigger than 0, please try again.'.format(endPoint))
                    continue
            else:
                endPoint = float(input('Type a number equal or bigger than 0: ').replace(',','.'))
                if endPoint < 0:
                    print('{:.0f} is not equal or bigger than 0, please try again.'.format(endPoint))
                    continue
            userInput = float(input('Type a integer between the start and end points: ').replace(',','.'))
            if startPoint < userInput < endPoint:
                break
            print('{:.0f} is not between the start and end points, please try again.'.format(userInput))
            continue
        except:
            print('You typed a value that is not acceptable, please try again.')
            continue
    givenDomainValue = userInput

    expression = ((-1)*((variation+givenDomainValue)**2) - (-1)*(givenDomainValue**2))/(variation)
    derivative = limit(expression, variation, 0)

    linearCoefficient = (-1)*(givenDomainValue**2) - derivative*givenDomainValue

    i = startPoint
    parableXValues = []
    parableYValues = []
    tangentXValues = []
    tangentYValues = []
    while i >= startPoint and i <= endPoint:
        parableYValues.append((-1)*(i**2)) # the quadratic function that generates the parable
        parableXValues.append(i)
        tangentYValues.append((derivative*i) + (linearCoefficient)) # equation of a line y = ax + b
        tangentXValues.append(i)
        i = i + 0.1

    print('The derivative of a quadratic function at x = {} is {:.2f}'.format(givenDomainValue, derivative))
        

    plt.plot(parableXValues, parableYValues, label = 'Parable')

    plt.plot(tangentXValues, tangentYValues, label = 'Tangent')

    plt.xlabel('x - axis')

    plt.ylabel('y - axis')

    plt.title('The instanteneous velocity of a projectile at a given time t')

    plt.show()

getDerivative()
