from api.Base.runmethod import RunMethod
from api.Base.get_data import GetData


class RunTest:
    def __init__(self, file_name=None, sheet_id=None):
        self.run_method = RunMethod()
        self.data = GetData(file_name, sheet_id)

    # 程序执行
    def go_on_run(self):
        rows_count = self.data.get_case_lines()
        for i in range(1, rows_count):
            url = self.data.get_url(i)
            method = self.data.get_request_method(i)
            is_run = self.data.get_is_rum(i)
            data = self.data.get_data_for_json(i)
            header = self.data.is_header(i)
            if is_run:
                res = self.run_method.run_main(method, url,data,header)
            return res


if __name__ == '__main__':
    run = RunTest()
    res = run.go_on_run()
    print(res)

