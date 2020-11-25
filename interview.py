# ride-- diffrent szes ,,capacity vary,, don
# 5,4,3,2 --group

# 10 people how many group?
# list of group
# car size
# return num of people can fit in the car

# def function name_(list ofgroups, car capasity)
# count=0
#     for loop through list of ofgroups
#          if number of people on the group can fit in the car capasity.
# return num of groups
# groups=[5,4,3]
# car_size=6
def num_groups(groups,car_size):
    count = 0
    for group in groups:
        if group<= car_size:
            car_size=car_size - group
            count=count+1
            # 1 person left
    return count 

print(num_groups([1,3,5,6],5))