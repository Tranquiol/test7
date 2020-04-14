#coding:gbk




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
