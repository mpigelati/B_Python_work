'''
student = ["bhagavan", "Bhagavan Prasad", "1000", "1001", "99020 96750", " ", "Bommanahalli", "  ", "enabled", ""]


for details in student:
        print details

'''

temp_list = []

students = [
    ["bhagavan", "Bhagavan Prasad", "1000", "1001", "99020 96750", "", "Bommanahalli", "", "enabled"],
    ["sai", "Sai Kumar", "1000", "1001", "99457 08707", "", "Bangalore", " ", "enabled"],
    ["pavan", "Pavan Kumar", "1500", "1001", "98863 04081", "", "Bommanahalli", "", "enabled"],
    ["test users", "Harsha Vardhan", "1501", "1001", "9902369277", "", "Bommanahalli", "", "enabled"],
    ["harsha", "Harsha Vardhan", "1501", "1001", "9902369277", "", "Bommanahalli", "", "enabled"],
    ["mohansai", "Mohan Sai", "1503", "1001", "9379741678", "", "Bommanahalli", "", "enabled"],
]

for student in students:
    for details in student[4:5]:
        print details, 
        temp_list.append(details)
    print ""

print "==============="
print temp_list
print "==============="

