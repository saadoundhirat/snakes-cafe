dic1 = {"dic":1}
dic2 = {"dic":2}
dic3 = {"dic":3}
dictionaries = [dic1,dic2,dic3]
for i in range(len(dictionaries)):
  my_var_name = [ k for k,v in locals().items() if v == dictionaries[i]][0]
  print(my_var_name)

