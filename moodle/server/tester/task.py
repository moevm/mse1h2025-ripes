from tester.ripes_tester import Tester
from random import seed


class Task:
    def __init__(self, code_file, random_seed, **kwargs) -> None:
        self.tester = Tester(code_file=code_file, **kwargs)
        seed(random_seed)

    def __generate_tests(self) -> list[dict]:
        tests = [
            {
                "input": None,
                "reginit": None,
                "expected": "",
                "expected_regs": None
            }
        ]
        return tests

    def __check_test(self, test: dict) -> bool:
        res = self.tester.run(test["input"], test["reginit"])
        if res["output"] == test["expected"]:
            return True
        return False

    def run(self) -> float:
        passed = 0
        for test in self.tests:
            if self.__check_test(test):
                passed += 1

        return passed / len(self.tests)

    @property
    def name(self) -> str:
        name: str = 'Тестовая задача'
        return name

    @property
    def description(self) -> str:
        description: str = 'Чтобы получить полный балл в этой задаче программа должна успешно завершиться.'
        return description
