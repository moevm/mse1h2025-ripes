from tester.task import Task
from tester.ripes_tester import regs_dict
import math
import random


class Task4(Task):
    def __init__(self, code_file, random_seed):
        super().__init__(code_file, random_seed, regs=True)
        regs = list(regs_dict.values())
        self.n_reg = random.choice(regs)
        regs.remove('x17')
        self.res_reg = random.choice(regs)
        self.tests = self.__generate_tests()

    def __generate_tests(self) -> list[dict]:
        tests = []
        for i in range(10):
            n = random.randint(1, 11)
            test = {
                "input": None,
                "reginit": {self.n_reg: n},
                "expected": "",
                "expected_regs": {self.res_reg: math.factorial(n)}
            }
            tests.append(test)
        return tests

    def __check_test(self, test: dict) -> bool:
        res = self.tester.run(test["input"], test["reginit"])
        return int(res['report']['registers'][self.res_reg]) == test["expected_regs"][self.res_reg]
    
    def run(self) -> float:
        passed = 0
        for test in self.tests:
            if self.__check_test(test):
                passed += 1

        return passed / len(self.tests)

    @property
    def name(self) -> str:
        name: str = 'Факториал числа'
        return name

    @property
    def description(self) -> str:
        description: str = (
            f'Напишите алгоритм, вычисляющий факториал числа n. '
            f'n записано в {self.n_reg}, результат записать в {self.res_reg}.'
        )
        return description

