from ast import Pass
import json

print(f"\n1. Retrieve Feature Object.")
print(f"2. Retrieve Parent Feature Object.")
print(f"3. Retrieve Children Feature Object(s).")
print(f"4. Return All Shelf Ojbects As A list.")
print(f"5. Return All Facing Objects As A List.\n")
option = int(input(f"Enter your option (1, 2, 3, 4, or 5): "))

class GeojsonFeatureCollection:
    with open("geojson.json", "r") as geojson:
        data = json.load(geojson)

        if option == 1:
            # print(json.dumps(data, indent=4)) # works
            ID = False
            input_id = input("What is the id? ")
            for i in data["features"]:
                if i["properties"]["id"] == input_id:
                    print(json.dumps(i, indent=4))
                    ID = True
            if ID == False:
                print("None")

        elif option == 2:
        # if parent id is 01
        # then go look for object where id is 01
        # then print object where id is 01
            input_id = input("What is the id? ")
            for i in data["features"]:
                id = i["properties"]["id"]
                # print(f"id: {id}") #works
                parents = i["properties"]["parent"]
                # print(f"parents: {parents}") # works
                
                if id == input_id:
                    # print(id) #works
                    for r in data["features"]:
                        if r["properties"]["id"] == parents:
                            print(json.dumps(r, indent=4))
                        elif parents is None:
                            print("None")
                            break
        
        elif option == 3:
            # if id is 01 && parent is Null (None)
            # loop through and return all IDs with 01
            # append to list and return list
            # else return empty list
            input_id = input("What is the id? ")
            list = []
            # print(f"list (should be empty): {list}") # works
            for i in data["features"]:
                id = i["properties"]["id"]
                parents = i["properties"]["parent"]
                if id == input_id:
                    if id == input_id and parents is None:
                        for r in data["features"]:
                            list.append(r)
                            print(list)
                            # print(f"list (should not be empty): {list}") # works
                    else:
                        print(list)


class GeojsonShelf:
    pass

class GeojsonFacing:
    pass