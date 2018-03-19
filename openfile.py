# Gary Morrissey
# Week 5 - Formatting Exercise

print("Petal Length", "Petal Width", "Sepal Length", "Sepal Width")  

with open ("Data/iris.csv") as f:
    for line in f:
        print('{:^12} {:^12} {:^12} {:^12}'.format(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3]))