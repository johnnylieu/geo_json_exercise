import json

with open("geojson.json", "r") as geojson:
    data = json.load(geojson)

class GeojsonFeatureCollection(geojson):
    def get_feature() -> object:
        input_id = input("What is the id? ")
        ID = False
        for i in data["features"]:
            if i["properties"]["id"] == input_id:
                print(json.dumps(i, indent=4))
                ID = True
                return i
        if ID == False:
            return None

    def get_parent_feature() -> object:
        input_id = input("What is the id? ")
        for i in data["features"]:
            id = i["properties"]["id"]
            parents = i["properties"]["parent"]
            
            if input_id[0:2] == id and len(input_id) == 4 and parents == None:
                print(json.dumps(i, indent=4))
                return i
        if len(input_id) != 4:
            return None

    def get_children_feature() -> list:
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
                    return(list)
        if empty_list == True:
            print(f"empty list: {list}")

    def get_facing_compound_label() -> str:
        input_id = input("What is the id? ")
        for i in data["features"]:
            id = i["properties"]["id"]
            type = i["properties"]["type"]
            for r in data["features"]:
                if r["properties"]["type"] == "facing" and r["properties"]["id"] == input_id:
                    facing_label = r["properties"]["label"]
                    
                    if input_id[0:2] == id and len(input_id) == 4:
                        return(f"{type}_{id}_{facing_label}")

class GeojsonShelf:
    def get_all_shelves() -> list:
        list = ""
        empty_list = True
        for i in data["features"]:
            type = i["properties"]["type"]
            # print(f"type: {type}")
            list = ""
            if type == "facing":
                empty_list = False
                list = i
                print(list)
                return(list)
        if empty_list == True:
            print(f"empty list: {list}")

class GeojsonFacing:
    def get_all_facings() -> list:
        list = ""
        empty_list = True
        for i in data["features"]:
            type = i["properties"]["type"]
            # print(f"type: {type}")
            list = ""
            if type == "shelf":
                empty_list = False
                list = i
                print(list)
                return(list)
        if empty_list == True:
            print(f"empty list: {list}")

if __name__ == "__main__":
    print(f"\n1. Retrieve Feature Object.")
    print(f"2. Retrieve Parent Feature Object.")
    print(f"3. Retrieve Children Feature Object(s).")
    print(f"4. Return All Facing Ojbects As A list.")
    print(f"5. Return All Shelf Objects As A List.")
    print(f"6. Return a formatted string label of its parent Shelf's label + given Facing's label \n")
    
    option = int(input(f"Enter your option (1, 2, 3, 4, 5, or 6): "))
    
    if option == 1:
        GeojsonFeatureCollection.get_feature()
    elif option == 2:
        GeojsonFeatureCollection.get_parent_feature()
    elif option == 3:
        GeojsonFeatureCollection.get_children_feature()
    elif option == 4:
        GeojsonShelf.get_all_shelves()
    elif option == 5:
        GeojsonFacing.get_all_facings()
    elif option == 6:
        GeojsonFeatureCollection.get_facing_compound_label()