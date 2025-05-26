import math
import random
import unittest
from tester.task1 import Task1
from tester.task2 import Task2
from tester.task3 import Task3
from tester.task4 import Task4


class TestTasks(unittest.TestCase):

    SEED = 139

    def test_task1(self):
        """
        Method checks sum task generator
        registers are non-negative
        result is the sum of two registers
        """
        task1 = Task1('no_filename', self.SEED)
        for t in task1.tests:
            regsum = t['reginit'][task1.a_reg] + t['reginit'][task1.b_reg]
            regres = t['expected_regs'][task1.res_reg]

            assert t['reginit'][task1.a_reg] >= 0
            assert t['reginit'][task1.b_reg] >= 0

            assert regsum == regres
            assert regsum != -regres or regres == 0

    def test_task2(self):
        """
        Method checks gcd task generator
        registers are positive
        result is the gcd of two registers
        """

        task2 = Task2('no_filename', self.SEED)
        for t in task2.tests:
            reggcd = math.gcd(t['reginit'][task2.a_reg], t['reginit'][task2.b_reg])
            regres = t['expected_regs'][task2.res_reg]

            assert t['reginit'][task2.a_reg] > 0
            assert t['reginit'][task2.b_reg] > 0
            assert regres > 0

            assert reggcd == regres
            assert reggcd != -regres

    def test_task3(self):
        """
        Method checks fibonacci task generator
        register is positive
        result is n-th position of fib sequence
        """
        fib = [0, 1]
        for i in range(26): fib.append(fib[-1] + fib[-2])

        task3 = Task3('no_filename', self.SEED)
        for t in task3.tests:
            regpos = t['reginit'][task3.n_reg]
            assert t['reginit'][task3.n_reg] > 0
            assert t['reginit'][task3.n_reg] < 25

            regres = t['expected_regs'][task3.res_reg]
            assert fib[regpos] == regres

    def test_task4(self):
        """
        Method checks factorial task generator
        register is positive
        Result n!
        """
        fact = [1, 1]
        for k in range(2, 26): fact.append(fact[-1] * k)

        task4 = Task4('no_filename', self.SEED)
        for t in task4.tests:
            regpos = t['reginit'][task4.n_reg]
            assert t['reginit'][task4.n_reg] > 0
            assert t['reginit'][task4.n_reg] < 25

            regres = t['expected_regs'][task4.res_reg]
            assert fact[regpos] == regres
