
# coding: utf-8

# In[2]:


def search_pairs(array, k):
    rez = []
    for i in array:
        for j in array:
            if i + j == k:
                if rez.count(str(i) + ', ' + str(j)) == 1 or rez.count(str(j) + ', ' + str(i)) == 1:
                    pass
                else:
                    rez.append(str(i) + ', ' + str(j))
                    
    return(rez)


print(search_pairs([1, 2, 6, 5, 3, 4, 7, 8, 3, 2], 7)) 

