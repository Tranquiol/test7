#coding:gbk
"""
����Ŀ��:RPSLS
����:������
����:04.08
"""
import random#����randomģ��
def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==0:
	    return "ʯͷ"
    elif number==1:
	    return "ʷ����"
    elif number==2:
	    return "��"
    elif number==3:    
	    return "����"
    elif number==4:
	    return "����"
    else:
	    print("Error:No Correct Name.")

def name_to_number(name):
	if name=="ʯͷ":
		return 0
	elif name=="ʷ����":
		return 1
	elif name=="��":
		return 2
	elif name=="����":
		return 3
	elif name=="����":
		return 4
	else:
		print("Error:No Correct Name.")
		
def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
    """   

print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
import name_to_number#����name_to_number����
player_number=name_to_number.name_to_number(choice_name)
comp_number=random.randint(0,4)#������������0-4������.
import number_to_name#����number_to_name����
comp_choice=number_to_name.number_to_name(comp_number)
print("�������ѡ����: ",comp_choice)
n=(player_number-comp_number)%5
if n==1 or n==2:
	print("��Ӯ��")
elif n==3 or n==4:
	print("�����Ӯ��")
else:
	print("ƽ��")


	
    
    
	
  
