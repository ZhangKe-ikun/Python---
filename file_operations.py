# file_operations.py

def save_to_file(student_data, filename):
    """
    将学生信息保存到文件中
    :param student_data: 学生数据字典
    :param filename: 文件名
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for student_id, info in student_data.items():
                file.write(f"{student_id},{info['name']},{info['score']}\n")
        print(f"学生信息已成功保存到 {filename}！")
    except Exception as e:
        print(f"保存文件时发生错误：{e}")


def load_from_file(filename):
    """
    从文件中加载学生信息
    :param filename: 文件名
    :return: 学生数据字典
    """
    student_data = {}
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                student_id, name, score = line.strip().split(',')
                student_data[student_id] = {'name': name, 'score': float(score)}
        print(f"学生信息已成功从 {filename} 加载！")
    except FileNotFoundError:
        print(f"文件 {filename} 不存在，无法加载数据！")
    except Exception as e:
        print(f"加载文件时发生错误：{e}")
    return student_data


def format_student_data(student_data):
    """
    格式化学生信息为字符串列表
    :param student_data: 学生数据字典
    :return: 格式化的字符串列表
    """
    formatted_data = []
    for student_id, info in student_data.items():
        formatted_data.append(f"学号: {student_id}, 姓名: {info['name']}, 成绩: {info['score']:.2f}")
    return formatted_data