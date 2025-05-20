import math
import random
import unittest
from tester.task1 import Task1
from tester.task2 import Task2
from tester.task3 import Task3
from tester.task4 import Task4


class TestTasks(unittest.TestCase):
    def test_task1(self):
        """
        Method checks sum task generator
        registers are non-negative
        result is the sum of x1 and x2
        """
        random.seed(139)

        task1 = Task1('no_filename')
        for t in task1.tests:
            regsum = t['reginit']['x1'] + t['reginit']['x2']
            regres = t['expected_regs']['x3']

            assert t['reginit']['x1'] >= 0
            assert t['reginit']['x2'] >= 0

            assert regsum == regres
            assert regsum != -regres or regres == 0

    def test_task2(self):
        """
        Method checks gcd task generator
        registers are positive
        result is the gcd of x10 and x11
        """
        random.seed(139)

        task2 = Task2('no_filename')
        for t in task2.tests:
            reggcd = math.gcd(t['reginit']['x10'], t['reginit']['x11'])
            regres = t['expected_regs']['x10']

            assert t['reginit']['x10'] > 0
            assert t['reginit']['x11'] > 0
            assert regres > 0

            assert reggcd == regres
            assert reggcd != -regres

    def test_task3(self):
        """
        Method checks fibonacci task generator
        register is positive
        result is n-th position of fib sequence
        """
        random.seed(139)

        fib = [0, 1]
        for i in range(26): fib.append(fib[-1] + fib[-2])

        task3 = Task3('no_filename')
        for t in task3.tests:
            regpos = t['reginit']['x10']
            assert t['reginit']['x10'] > 0
            assert t['reginit']['x10'] < 25

            regres = t['expected_regs']['x10']
            assert fib[regpos] == regres

    def test_task4(self):
        """
        Method checks factorial task generator
        register is positive
        Result n!
        """
        random.seed(139)

        fact = [1, 1]
        for k in range(2, 26): fact.append(fact[-1] * k)

        task4 = Task4('no_filename')
        for t in task4.tests:
            regpos = t['reginit']['x10']
            assert t['reginit']['x10'] > 0
            assert t['reginit']['x10'] < 25

            regres = t['expected_regs']['x10']
            assert fact[regpos] == regres
