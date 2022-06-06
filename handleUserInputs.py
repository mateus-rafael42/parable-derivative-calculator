def userInputs():
    def handleUserInputs():
        while True:
            try:
                startPoint = float(input('Type a number equal or less than 0: ').replace(',','.'))
                if startPoint == 0:
                    endPoint = float(input('Type a number bigger than 0: ').replace(',','.'))
                    if endPoint <= 0:
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
        return startPoint, endPoint, givenDomainValue

    startPoint, endPoint, givenDomainValue = handleUserInputs()
    return startPoint, endPoint, givenDomainValue
    
if __name__ == '__main__':
    userInputs()