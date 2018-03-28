# Gary Morrissey, 
# Week 5 - Formatting Exercise
# Adapted from http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data

print("Petal Length", "Petal Width", "Sepal Length", "Sepal Width")  # Column headings

with open ("Data/iris.csv") as f: # Link the csv file
    for line in f:
        print('{:^12} {:^12} {:^12} {:^12}'.format(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3]))
