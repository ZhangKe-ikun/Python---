# student.py

def add_student(student_data, student_id, name, score):
    """
    添加学生信息
    :param student_data: 学生数据列表
    :param student_id: 学生学号
    :param name: 学生姓名
    :param score: 学生成绩
    """
    if student_id in student_data:
        print(f"学号 {student_id} 已存在，无法添加！")
    else:
        student_data[student_id] = {'name': name, 'score': score}
        print(f"学生 {name} 信息已成功添加！")


def view_scores(student_data):
    """
    查看所有学生信息
    :param student_data: 学生数据列表
    """
    if not student_data:
        print("当前无学生信息！")
        return

    print("学生信息如下：")
    print(f"{'学号':<10}{'姓名':<10}{'成绩':<10}")
    for student_id, info in student_data.items():
        print(f"{student_id:<10}{info['name']:<10}{info['score']:<10}")


def update_score(student_data, student_id, new_score):
    """
    修改学生成绩
    :param student_data: 学生数据列表
    :param student_id: 学生学号
    :param new_score: 新的成绩
    """
    if student_id in student_data:
        student_data[student_id]['score'] = new_score
        print(f"学号 {student_id} 的成绩已更新为 {new_score}！")
    else:
        print(f"未找到学号 {student_id} 的学生信息，无法更新！")


def find_student(student_data, student_id):
    """
    根据学号查询学生信息
    :param student_data: 学生数据列表
    :param student_id: 学生学号
    """
    if student_id in student_data:
        info = student_data[student_id]
        print(f"学号: {student_id}, 姓名: {info['name']}, 成绩: {info['score']}")
    else:
        print(f"未找到学号 {student_id} 的学生信息！")


def delete_student(student_data, student_id):
    """
    删除学生信息
    :param student_data: 学生数据列表
    :param student_id: 学生学号
    """
    if student_id in student_data:
        del student_data[student_id]
        print(f"学号 {student_id} 的学生信息已删除！")
    else:
        print(f"未找到学号 {student_id} 的学生信息，无法删除！")