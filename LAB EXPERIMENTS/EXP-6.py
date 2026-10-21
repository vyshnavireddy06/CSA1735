rooms = {'A': 'Dirty', 'B': 'Dirty'}
position = 'A'

while 'Dirty' in rooms.values():
    if rooms[position] == 'Dirty':
        print("Clean", position)
        rooms[position] = 'Clean'
    else:
        position = 'B' if position == 'A' else 'A'
        print("Move to", position)

print("Both rooms are clean")
