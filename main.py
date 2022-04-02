import json

with open("geojson.json", "r") as geojson:
    data = json.load(geojson)

class GeojsonFeatureCollection:
    def get_feature():
        input_id = input("What is the id? ")
        ID = False
        for i in data["features"]:
            if i["properties"]["id"] == input_id:
                print(json.dumps(i, indent=4))
                ID = True
        if ID == False:
            print("None")

    def get_parent_feature():
        input_id = input("What is the id? ")
        for i in data["features"]:
            id = i["properties"]["id"]
            parents = i["properties"]["parent"]
            
            if input_id[0:2] == id and len(input_id) == 4 and parents == None:
                print(json.dumps(i, indent=4))
        if len(input_id) != 4:
            print("None")

    def get_children_feature():
        input_id = input("What is the id? ")
        empty_list = True
        for i in data["features"]:
            id = i["properties"]["id"][0:2]
            parents = i["properties"]["parent"]
            list = ""
            
            if id == input_id and parents != None:
                    empty_list = False
                    list = i
                    print(list)
        if empty_list == True:
            print(list)
    
    def get_all_shelves():
        list = ""


#         elif option == 6:
#             input_id = input("What is the id? ")
#             for i in data["features"]:
#                 id = i["properties"]["id"]
#                 type = i["properties"]["type"]
#                 for r in data["features"]:
#                     if r["properties"]["type"] == "facing" and r["properties"]["id"] == input_id:
#                         facing_label = r["properties"]["label"]
                        
#                         if input_id[0:2] == id and len(input_id) == 4:
#                             print(f"{type}_{id}_{facing_label}")


# class GeojsonShelf:
#     pass

# class GeojsonFacing:
#     pass

if __name__ == "__main__":
    print(f"\n1. Retrieve Feature Object.")
    print(f"2. Retrieve Parent Feature Object.")
    print(f"3. Retrieve Children Feature Object(s).")
    print(f"4. Return All Shelf Ojbects As A list.")
    print(f"5. Return All Facing Objects As A List.")
    print(f"6. Return a formatted string label of its parent Shelf's label + given Facing's label \n")
    option = int(input(f"Enter your option (1, 2, 3, 4, 5, or 6): "))
    if option == 1:
        GeojsonFeatureCollection.get_feature()
    elif option == 2:
        GeojsonFeatureCollection.get_parent_feature()
    elif option == 3:
        GeojsonFeatureCollection.get_children_feature()