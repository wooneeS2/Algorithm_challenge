def solution(N):
    # write your code in Python 3.6
    number =list(str(format(N, 'b')))
    number_list = list(map(int,number))
    one_list=[]
    for i in range(len(number_list)):
        if number_list[i]==1:
            one_list.append(i)
    max = 0
    for i in range(len(one_list)):
        if i == (len(one_list)-1):
            if one_list[-1]-one_list[i] > max:
                max = one_list[-1]-one_list[i]
            else :
                if max>0:
                    return max-1
                else:
                    return max
           
        if one_list[i+1]-one_list[i] > max:
            max=one_list[i+1]-one_list[i]

    return max