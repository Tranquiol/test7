#coding:gbk
"""
程序目标:RPSLS
作者:张珂怡
日期:04.08
"""
import random#调用random模块
def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if number==0:
	    return "石头"
    elif number==1:
	    return "史波克"
    elif number==2:
	    return "布"
    elif number==3:    
	    return "蜥蜴"
    elif number==4:
	    return "剪刀"
    else:
	    print("Error:No Correct Name.")

def name_to_number(name):
	if name=="石头":
		return 0
	elif name=="史波克":
		return 1
	elif name=="布":
		return 2
	elif name=="蜥蜴":
		return 3
	elif name=="剪刀":
		return 4
	else:
		print("Error:No Correct Name.")
		
def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
    """   

print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
import name_to_number#调用name_to_number函数
player_number=name_to_number.name_to_number(choice_name)
comp_number=random.randint(0,4)#计算机随机产生0-4的整数.
import number_to_name#调用number_to_name函数
comp_choice=number_to_name.number_to_name(comp_number)
print("计算机的选择是: ",comp_choice)
n=(player_number-comp_number)%5
if n==1 or n==2:
	print("您赢了")
elif n==3 or n==4:
	print("计算机赢了")
else:
	print("平局")


	
    
    
	
  
