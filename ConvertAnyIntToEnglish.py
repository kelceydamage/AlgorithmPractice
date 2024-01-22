import random
import queue

WordMap = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    0: 'zero',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirten',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eightteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'fourty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninty',
    100: 'hundred',
}


class Solution:
    languageSegments = 3
    segmentmap = {
        0: '',
        3: 'thousand',
        6: 'million',
        9: 'billion',
        12: 'trillion',
        15: 'quadrillion',
        18: 'quintillion',
        21: 'sextillion',
        24: 'septillion',
        27: 'octillion',
        30: 'nonillion',
        33: 'decillion',
    }
    stack = queue.LifoQueue()
    wordmap = WordMap
    resultStack = queue.LifoQueue()

    def Run(integertoSolve):
        print(f'Integer to convert: {integertoSolve}')
        Solution.OrderByLeastSignifiacantDigit(integertoSolve)
        Solution.RendderToText()
        Solution.PrintSolution()

    @staticmethod
    def OrderByLeastSignifiacantDigit(integertoSolve):
        [Solution.stack.put(i) for i in str(integertoSolve)]

    @staticmethod
    def PrintSolution():
        print('Conversion to string:')
        while Solution.resultStack.qsize() > 0:
            print(Solution.resultStack.get(), end=' ')
        print()

    @staticmethod
    def RendderToText():
        counter = 0
        while Solution.stack.qsize() > 0:
            for i in range(0, Solution.languageSegments - 1):
                if (Solution.stack.qsize() == 0): break
                if (i == 0):
                    nextSignificant = '0'
                    leastSignificant = Solution.stack.get()
                    if (Solution.stack.qsize() > 0): 
                        nextSignificant = Solution.stack.get()
                    if (nextSignificant == '1'):
                        key = int(nextSignificant + leastSignificant)
                        Solution.resultStack.put(Solution.wordmap[int(key)])
                    elif (leastSignificant != '0'):
                        Solution.resultStack.put(Solution.wordmap[int(leastSignificant)])
                        if (nextSignificant != '0'):
                            Solution.resultStack.put('-')
                            Solution.resultStack.put(f'{Solution.wordmap[int(nextSignificant) * 10]}')
                else:
                    mostSignificant = Solution.stack.get()
                    if (mostSignificant != '0'):
                        Solution.resultStack.put(Solution.wordmap[100])
                        Solution.resultStack.put(Solution.wordmap[int(mostSignificant)])
            counter += 3
            if (counter % Solution.languageSegments == 0 and Solution.stack.qsize() > 0):
                Solution.resultStack.put(Solution.segmentmap[counter])
                


            




if __name__ == "__main__":
    print('Running solution...')
    Solution.Run(random.randint(0, 999999999999999999999))
