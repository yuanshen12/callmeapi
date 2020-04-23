from api.Base.runmethod import RunMethod
from api.Base.get_data import GetData
from api.Base.common_util import CommonUtil


class RunTest:
    def __init__(self, file_name=None, sheet_id=None):
        self.run_method = RunMethod()
        self.data = GetData(file_name, sheet_id)
        self.com_util = CommonUtil()

    # 程序执行
    def go_on_run(self):
        rows_count = self.data.get_case_lines()
        for i in range(1, rows_count):
            url = self.data.get_url(i)
            method = self.data.get_request_method(i)
            is_run = self.data.get_is_rum(i)
            data = self.data.get_data_for_json(i)
            expect = self.data.get_expcet_data(i)
            header = self.data.is_header(i)
            if is_run:
                res = self.run_method.run_main(method, url, data, header)
                if self.com_util.is_contain(expect, res) is True:
                    self.data.write_result(i, "pass")
                else:
                    self.data.write_result(i, "fail")


if __name__ == '__main__':
    run = RunTest()
    res = run.go_on_run()

