import matplotlib.pyplot as plt
from getDerivative import useDerivative

def useGraph():
    def getGraph():
        startPoint, endPoint, givenDomainValue, parableXValues, parableYValues, tangentXValues, tangentYValues, derivative = useDerivative()
        print('The derivative of a quadratic function at x = {} is {:.2f}'.format(givenDomainValue, derivative))
                
        plt.plot(parableXValues, parableYValues, label = 'Parable')

        plt.plot(tangentXValues, tangentYValues, label = 'Tangent')

        plt.xlabel('x - axis')

        plt.ylabel('y - axis')

        plt.title('The parable of domain ({}, {}) and the tangent line at x = {}'.format(startPoint, endPoint, givenDomainValue))

        plt.show()

    getGraph()

if __name__ == '__main__':
    useGraph()
