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
        # print((data)) #works
        # print(type(data)) # works -> dictionary

        if option == 1:
            print(json.dumps(data, indent=4)) # works

        elif option == 2:
            input_id = input("What is the id field? ")

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
                            # break
                        else:
                            pass
                    
                elif (id != input_id):
                    print("None")
                    # break
                
                else:
                    pass
                    
                # for p in data["features"]:
                #     if i["properties"]["id"] == "01":
                # if parents == input_id:
                #     print(i)
                #     break

                # else:
                #     print("None")
                #     break

        # for i in data["features"]:
        #     if i["properties"]["id"] == "01":
        #         print(i)
        #         break
                        
                # if i["properties"]["id"] == id:
                #     print(i)

                    # for i in data["features"]:
                    #     parent = i["properties"]["parent"]
                    #     print(f"line 27: {parent}") # works
                    #     if parent == id:
                    #         print(i)
                    #         break

                # else:
                #     print("None")
                #     break
        else:
            pass
# if parent id is 01
# then go look for object where id is 01
# then print object where id is 01

class GeojsonShelf:
    pass

class GeojsonFacing:
    Pass


# g = GeojsonFeatureCollection("FeatureCollection")
# s = GeojsonShelf("Johnny", "black", "30")
# f = GeojsonFacing("Brian", "brown", "60")

# g.goutput()
# s.soutput()
# f.foutput()