import unittest
from api.Base.demo import RunMain


class TestMethod(unittest.TestCase):

    def setUp(self) -> None:
        self.run = RunMain()
        print("---每一条测试用例执行之前")

    def tearDown(self) -> None:
        print("---每一条测试用例执行之后")

    def test_01(self):
        url = "http://127.0.0.1:8000/login/"
        data = {
            "username": "12421",
            "password": "45678"
        }
        res = self.run.run_main(url, "POST", data)
        print(type(res))
        print("---用例一")

    def test_02(self):
        url = "https://m.jiuxiao2.cn/api/site/getSiteList"
        res = self.run.run_main(url, "GET")
        print(res["data"][0]["provinceName"])
        print("----用例二")


if __name__ == '__main__':
    unittest.main()