from api.Base.operation_excel import OperationExcel
import data_config
from api.Base.operation_json import OperationJson

# 拿excel数据
class GetData:

    def __init__(self, file_name=None, sheet_id=None):
        self.operation_excel = OperationExcel(file_name, sheet_id)

    # 去获取excel行数，就是我的case个数
    def get_case_lines(self):
        return self.operation_excel.get_lines()

    # 获取是否执行
    def get_is_rum(self, row):
        flag = None
        col = data_config.get_run()
        run_model = self.operation_excel.get_cell_value(row, col)
        if run_model == "yes":
            flag = True
        else:
            flag = False
        return flag

    # 是否携带header
    def is_header(self, row):
        col = data_config.get_header()
        header = self.operation_excel.get_cell_value(row, col)
        if header == "yes":
            return data_config.get_header()
        else:
            return None

    # 获取请求方式
    def get_request_method(self, row):
        col = data_config.get_request_way()
        request_method = self.operation_excel.get_cell_value(row, col)
        return request_method

    # 获取url
    def get_url(self, row):
        col = data_config.get_url()
        url = self.operation_excel.get_cell_value(row, col)
        return url

    # 获取请求数据
    def get_request_data(self, row):
        col = data_config.get_data()
        data = self.operation_excel.get_cell_value(row, col)
        if data == "":
            return None
        return data

    # 通过获取关键字拿到data
    def get_data_for_json(self, row):
        opera_json = OperationJson()
        request_data = opera_json.get_data(self.get_request_data(row))
        return request_data

    # 获取预期结果
    def get_expcet_data(self, row):
        col = data_config.get_expect()
        expect = self.operation_excel.get_cell_value(row, col)
        if expect == "":
            return None
        return expect

    def write_result(self, row, value):
        col = int(data_config.get_result())
        self.operation_excel.write_value(row, col, value)

    # 获取依赖数据的key
    def get_depend_key(self, row):
        col = int(data_config.get_data_depend())
        dependent_key = self.operation_excel.get_cell_value(row, col)
        if dependent_key == "":
            return None
        else:
            return dependent_key

    # 判断是否有case依赖
    def is_depend(self, row):
        col = int(data_config.get_case_depend())
        depend_case_id = self.operation_excel.get_cell_value(row, col)
        if depend_case_id == "":
            return None
        else:
            return depend_case_id

    # 获取数据依赖字段
    def get_depend_field(self, row):
        col = int(data_config.get_field_depend())
        data = self.operation_excel.get_cell_value(row, col)
        if data == "":
            return None
        else:
            return data





