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
            ID = False
            input_id = input("What is the id? ")
            for i in data["features"]:
                if i["properties"]["id"] == input_id:
                    print(json.dumps(i, indent=4))
                    ID = True
            if ID == False:
                print("None")

        elif option == 2:
            input_id = input("What is the id? ")
            for i in data["features"]:
                id = i["properties"]["id"]
                parents = i["properties"]["parent"]
                
                if id == input_id:
                    for r in data["features"]:
                        if r["properties"]["id"] == parents:
                            print(json.dumps(r, indent=4))
                            break
                        elif parents is None:
                            print("None")
                            break
        
        elif option == 3:
            input_id = input("What is the id? ")
            for i in data["features"]:
                id = i["properties"]["id"][0:2]
                parents = i["properties"]["parent"]
                list = []
                if id == input_id and parents != None:
                        list.append(i)
                        print(list)
            print(list)


class GeojsonShelf:
    pass

class GeojsonFacing:
    pass