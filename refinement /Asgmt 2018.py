# bags_rice = 15
# upper_bound = 5.1
# lower_bound = 4.9
# for count in range(bags_rice):
#     bag_weight = float(input("Enter the weight of the bag of rice "))
#     if bag_weight > upper_bound:
#         print("The bag of rice is overweight")
#     if bag_weight < lower_bound:
#         print("The bag of rice is underweight")

bags_rice = 10
upper_bound = 5.1
lower_bound = 4.9
overweight_count = 0
underweight_count = 0
for i in range(bags_rice):
    bag_weight = float(input("Enter the weight of the bag of rice: "))
    if bag_weight < upper_bound and bag_weight > lower_bound:
        print("The bag of rice is the correct weight\n")
    if bag_weight > upper_bound:
        print("The bag of rice is overweight\n")
        overweight_count += 1
    if bag_weight < lower_bound:
        print("The bag of rice is underweight\n")
        underweight_count += 1
    print("The number of bags of rice that were overweight: ",overweight_count)
    print("The number of bags of rice that were underweight: ",underweight_count,"\n")
