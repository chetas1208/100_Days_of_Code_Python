import random

states_of_usa = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
print(states_of_usa)
print(states_of_usa[random.randint(0, 49)]) # random.randint(0, 49) is the same as random.randint(0, len(states_of_usa)-1)

#append() adds an item to the end of the list
states_of_usa.append("Puerto Rico")
print(states_of_usa)

#extend() adds multiple items to the end of the list
states_of_usa.extend(["Guam", "U.S. Virgin Islands"])
print(states_of_usa)