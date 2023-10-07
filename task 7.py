my_dict = {"name":"Ahmed", "age":20, "job":"Engineer"}
print(my_dict.values())
print(my_dict.keys())
print(my_dict["name"])
my_dict["age"]=32
my_dict.update({"workplace":"GSG"})
print(my_dict)
print("*"*50)

my_dict["job"]="Doctor"
key = tuple(my_dict.keys())
value = tuple(my_dict.values())
print("My-tuple = (" ,end=" ")
for i in range(len(key)):
    print(f"( {key[i]} , {value[i]} )",end=" " )
    if i != len(key) - 1:
        print("," , end=" ")

dic1 = {'name':'Dema', "age":20}
dic2 = {'job':'Engineer', "ID": 456367}
dic3 = {'year': 2003}
new_dic = dic1 | dic2 | dic3
print(new_dic)
print("*"*50)

my_dict = {'num1': 648, 'num2':4194, 'num3': 60}
num = list(my_dict.values())
# print(type(num))
num.sort()
print("Maximum Value "+ str(num[-1]))
print("Minimum Value "+ str(num[0]))
print("*"*50)

my_dict = {'name':'Abed', 'age': 31, 'job':'Teacher'}
print('ID' in my_dict)
print('ID' in my_dict.values())
print("*"*50)

Language2023 = {'programming Language':['python','Java', 'JavaScript', 'C#'] ,
                'Market share %':[27.99, 15.9, 9.36, 6.67]}
result = [{key : value[i]
           for key, value in Language2023.items()}
          for i in range(4)]
print(result)