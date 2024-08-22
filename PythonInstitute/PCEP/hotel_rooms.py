building = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

build_counter = 0
floor_counter = 0
room_counter = 0

building[1][9][13] = True
building[2][14][13] = True

for build in building:
    build_counter += 1
    print("building:", build_counter)
    for floor in build:
        floor_counter += 1
        print("floor:", floor_counter)
        for room in floor:
            room_counter += 1
            print("Room:", room_counter, room, end=" ")
        
        print()
        room_counter = 0
    print()
    floor_counter = 0
    
vacancy = 0

for room_number in range(20):
    if not building[2][14][room_number]:
        vacancy += 1
        
print("Number of vacancies on building 3 floor 15:", vacancy)
        
