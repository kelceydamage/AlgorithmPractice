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
    englishLanguageSegments = 3
    englishSegmentmap = {
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
    englishWordmap = WordMap
    resultStack = queue.LifoQueue()

    def Run(integertoSolve):
        print(f'Integer to convert: {integertoSolve}')
        Solution.OrderByLeastSignificantDigit(integertoSolve)
        Solution.RendderToText()
        Solution.PrintSolution()

    @staticmethod
    def OrderByLeastSignificantDigit(integertoSolve):
        """Build a stack of the digits from left to right in order to use them 
        right to left."""
        [Solution.stack.put(i) for i in str(integertoSolve)]

    @staticmethod
    def PrintSolution():
        """Print the result stack to get the solution in correct order."""
        print('Conversion to string:')
        while Solution.resultStack.qsize() > 0:
            print(Solution.resultStack.get(), end=' ')
        print()

    @staticmethod
    def RendderToText():
        """Drain the stack while running a segment solver on each iteration.
        Inject inter-segmental words into the result stack."""
        counter = 0
        while Solution.stack.qsize() > 0:
            solvedSegmentLength = Solution.EnglishSolverForSegments()
            counter += solvedSegmentLength
            if (counter % Solution.englishLanguageSegments == 0 and Solution.stack.qsize() > 0):
                Solution.resultStack.put(Solution.englishSegmentmap[counter])

    @staticmethod
    def EnglishSolverForSegments():
        """Take up to 3 digits off the stack and contextually convert them to
        English words. Push them onto the result stack in reverese order."""
        solvedSegmentLength = 1
        for i in range(0, 2):
            if (Solution.stack.qsize() == 0): break
            if (i == 0):
                leastSignificant = Solution.stack.get()
                nextSignificant = '0'
                if (Solution.stack.qsize() > 0): 
                    nextSignificant = Solution.stack.get()
                if (nextSignificant == '1'):
                    key = int(nextSignificant + leastSignificant)
                    Solution.resultStack.put(Solution.englishWordmap[int(key)])
                    continue
                if (leastSignificant != '0'):
                    Solution.resultStack.put(Solution.englishWordmap[int(leastSignificant)])
                if (int(nextSignificant) > 1):
                    if (leastSignificant != '0'):
                        Solution.resultStack.put('-')
                    Solution.resultStack.put(f'{Solution.englishWordmap[int(nextSignificant) * 10]}')
            else:
                mostSignificant = Solution.stack.get()
                if (mostSignificant != '0'):
                    Solution.resultStack.put(Solution.englishWordmap[100])
                    Solution.resultStack.put(Solution.englishWordmap[int(mostSignificant)])
                solvedSegmentLength = 3
        return solvedSegmentLength


if __name__ == "__main__":
    print('Running solution...')
    Solution.Run(random.randint(0, 999999999999999999999))
    #Solution.Run(70316726957092492757)
