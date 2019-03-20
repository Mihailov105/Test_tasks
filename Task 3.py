
# coding: utf-8

# In[3]:


def get_zeros(n):
    factorial = 1
    for i in range(n - 1):
        factorial *= i+2

    factorial = str(factorial)[::-1]
    rez = 0
    for index in range(len(str(factorial))):
        if int(factorial[index]) != 0:
            break
        else:
            rez += 1
            
    return rez


print(get_zeros(15))

