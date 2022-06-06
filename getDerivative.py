from sympy import *
from handleUserInputs import userInputs

def useDerivative():
    def getDerivative():
        variation = Symbol('x')

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

        return parableXValues, parableYValues, tangentXValues, tangentYValues, derivative

    startPoint, endPoint, givenDomainValue = userInputs()
    parableXValues, parableYValues, tangentXValues, tangentYValues, derivative = getDerivative()
    return startPoint, endPoint, givenDomainValue, parableXValues, parableYValues, tangentXValues, tangentYValues, derivative

if __name__ == '__main__':
    useDerivative()