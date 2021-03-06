
# coding: utf-8

# In[2]:


with open('names.txt') as file:
    for element in file:
        elements = element.replace(',', ' ').replace('"', '').split()
        elements.sort()  # визуально определил что по умолчанию это как раз лексикографическая сортировка

alphabet = dict(A = 1, B = 2, C = 3, D = 4, 
                E = 5, F = 6, G = 7, H = 8, 
                I = 9, J = 10, K = 11, L = 12, 
                M = 13, N = 14, O = 15, P = 16, 
                Q = 17, R = 18, S = 19, T = 20, U = 21,
                V = 22, W = 23, X = 24, Y = 25, Z = 26)

result = 0
number = 0

for element in elements:
    number += 1
    summ = 0
    for letter in element:
        summ += alphabet[letter]
    
    result += number * summ
    
print(result)

