# coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�����Ȼ
���ڣ�2022/5/12
"""

import random


# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """

    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��
    if name == "ʯͷ":
        return 0
    elif name == "ʷ����":
        return 1
    elif name == "ֽ":
        return 2
    elif name == "����":
        return 3
    elif name == "����":
        return 4
    else:
        print("Error:No Correct Name")
        return 5


def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��
    if number == 0:
        return "ʯͷ"
    elif number == 1:
        return "ʷ����"
    elif number == 2:
        return "ֽ"
    elif number == 3:
        return "����"
    elif number == 4:
        return "����"


def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """

    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice
    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number
    player_choice_number = name_to_number(player_choice)
    # �ж��û������Ƿ������Ϸ���򣬲�������Ϸ�����ֱ���˳�
    if player_choice_number == 5:
        return
    print("����ѡ��Ϊ��{}".format(player_choice))
    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number
    comp_number = random.randrange(0, 5)
    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����
    comp_choice = number_to_name(comp_number)
    # ����Ļ����ʾ�����ѡ����������
    print("�������ѡ��Ϊ��{}".format(comp_choice))
    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��
    # win_flag���ڼ�¼�û��������ĶԾ��Ƿ�ʤ��
    win_flag = 0
    if comp_number == player_choice_number:
        print("���ͼ��������һ����")
        return
    # ��ÿһ�ֿ��ܵ��������ģ��
    else:
        if player_choice_number == 0:
            if (comp_number == 4) or (comp_number == 3):
                win_flag = 1
        if player_choice_number == 1:
            if (comp_number == 4) or (comp_number == 0):
                win_flag = 1
        if player_choice_number == 2:
            if (comp_number == 1) or (comp_number == 0):
                win_flag = 1
        if player_choice_number == 3:
            if (comp_number == 1) or (comp_number == 2):
                win_flag = 1
        if player_choice_number == 4:
            if (comp_number == 2) or (comp_number == 3):
                win_flag = 1
    if win_flag == 1:
        print("��Ӯ��")
    else:
        print("�����Ӯ��")

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name = input()
rpsls(choice_name)
