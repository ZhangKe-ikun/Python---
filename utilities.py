# utilities.py

def sort_students_by_score(student_data, reverse=False):
    """
    按成绩排序学生信息
    :param student_data: 学生数据字典
    :param reverse: 是否降序排序，默认升序
    :return: 排序后的学生数据列表
    """
    try:
        sorted_data = sorted(student_data.items(), key=lambda x: x[1]['score'], reverse=reverse)
        return sorted_data
    except KeyError as e:
        print(f"数据格式错误，无法排序：{e}")
        return []


def validate_input(input_value, input_type):
    """
    验证用户输入的有效性，确保符合指定的数据类型
    :param input_value: 用户输入值
    :param input_type: 数据类型（int、float、str）
    :return: 转换后的数据值或 None（无效输入）
    """
    try:
        if input_type == int:
            return int(input_value)
        elif input_type == float:
            return float(input_value)
        elif input_type == str:
            return str(input_value)
        else:
            print("不支持的输入类型！")
            return None
    except ValueError:
        print(f"输入无效，请输入一个有效的 {input_type.__name__} 类型值！")
        return None


def handle_exceptions(func):
    """
    装饰器函数，用于捕获和处理异常
    :param func: 被装饰的函数
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"执行函数 {func.__name__} 时发生错误：{e}")
            return None
    return wrapper