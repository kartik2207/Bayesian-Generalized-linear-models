import pandas as pd

name = ['Sam', 'Bill', 'Bob', 'Ian', 'Jo', 'Anne', 'Carl', 'Toni']
age = [22, 34, 18, 34, 76, 54, 21, 8]
gender = ['f', 'm', 'm', 'm', 'f', 'f', 'm', 'f']
height = [1.64, 1.85, 1.70, 1.75, 1.63, 1.79, 1.70, 1.68]

passed_physical = [0, 1, 1, 1, 0, 1, 1, 0]

people = pd.DataFrame()
people_label =pd.DataFrame()
people['name'] = name
people['age'] = age
people['gender'] = gender
people['height'] = height

people_label['passed'] = passed_physical

people_copy = people.copy()
people_label_copy=people_label.copy()
train_set = people_copy.sample(frac=0.75, random_state=1)
train_label=people_label_copy.sample(frac=0.75, random_state=1)

test_set = people_copy.drop(train_set.index)
test_label=people_label_copy.drop(train_label.index)

print(people.shape)
print ('Training set')
print (train_set)
print ('\nTest set')
print (test_set)
print('\n Train label')
print(train_label)
print('\Test label')
print(test_label)

print ('\nOriginal DataFrame')
print (people)

