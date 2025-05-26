from tester.task import Task
from tester.ripes_tester import regs_dict
import random


class Task1(Task):
    def __init__(self, code_file, random_seed):
        super().__init__(code_file, random_seed, regs=True)
        regs = list(regs_dict.values())
        self.a_reg = random.choice(regs)
        self.b_reg = random.choice(regs)
        regs.remove('x17')
        self.res_reg = random.choice(regs)

        self.tests = self.__generate_tests()

    def __generate_tests(self) -> list[dict]:
        tests = []
        for i in range(5):
            a = random.randint(0, 10)
            b = random.randint(0, 10)
            test = {
                "input": None,
                "reginit": {self.a_reg: a, self.b_reg: b},
                "expected": "",
                "expected_regs": {self.res_reg: a + b}
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
        name: str = 'a + b'
        return name

    @property
    def description(self) -> str:
        description: str = (
            f'Сложите два числа a и b, которые лежат в регистрах {self.a_reg} и {self.b_reg} соответственно.'
            f'Результат записать в {self.res_reg}.'
        )
        return description
