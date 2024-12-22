# main.py

import student
import file_operations
import utilities

def display_menu():
    """
    显示主菜单
    """
    print("\n=== 学生成绩管理系统 ===")
    print("1. 添加学生信息")
    print("2. 查询学生成绩")
    print("3. 修改学生成绩")
    print("4. 查看所有学生信息")
    print("5. 导出学生信息到文件")
    print("6. 退出")
    print("========================")


def execute_choice(choice, student_data):
    """
    根据用户选择执行相应操作
    :param choice: 用户选择的操作编号
    :param student_data: 存储学生数据的字典
    """
    if choice == 1:
        student_id = input("请输入学生学号: ")
        name = input("请输入学生姓名: ")
        score = utilities.validate_input(input("请输入学生成绩: "), float)
        if score is not None:
            student.add_student(student_data, student_id, name, score)
            print("学生信息添加成功！")
    elif choice == 2:
        student_id = input("请输入要查询的学生学号: ")
        student.find_student(student_data, student_id)

    elif choice == 3:
        student_id = input("请输入要修改的学生学号: ")
        new_score = utilities.validate_input(input("请输入新的成绩: "), float)
        if new_score is not None:
            student.update_score(student_data, student_id, new_score)

    elif choice == 4:
        print("\n=== 所有学生信息 ===")
        for student_id, info in student_data.items():
            print(f"学号: {student_id}, 姓名: {info['name']}, 成绩: {info['score']:.2f}")
        sorted_students = utilities.sort_students_by_score(student_data, reverse=True)
        print("按成绩降序排序结果：")
        for student_id, info in sorted_students:
            print(f"学号: {student_id}, 姓名: {info['name']}, 成绩: {info['score']:.2f}")
    elif choice == 5:
        filename = input("请输入导出文件名（如 students.txt）: ")
        file_operations.save_to_file(student_data, filename)
    elif choice == 6:
        print("退出系统。再见！")
        return False
    else:
        print("无效选项，请重新输入！")
    return True


def main():
    """
    主程序入口
    """
    # 初始化学生数据
    student_data = {}

    # 尝试加载已有数据
    try:
        student_data = file_operations.load_from_file("students.txt")
        print("成功加载学生数据。")
    except FileNotFoundError:
        print("未找到学生数据文件，已创建新数据存储。")

    # 主循环
    while True:
        display_menu()
        choice = utilities.validate_input(input("请选择操作 (1-6): "), int)
        if choice is None:
            continue
        if not execute_choice(choice, student_data):
            break

    # 退出时保存数据
    file_operations.save_to_file(student_data, "students.txt")
    print("学生数据已保存，系统退出。")


if __name__ == "__main__":
    main()