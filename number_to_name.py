#coding:gbk




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
