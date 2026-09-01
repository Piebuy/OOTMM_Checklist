from globals import SCENE_DIC_OOT, SCENE_DIC_MM, CURRENT_SCENE_FILE, LOCATIONS_FILE,BACKUP_LOCATIONS_FILE, DUNGEON_ENTRANCES,BOSS_ENTRANCES
from inventory import print_inventory, update_inventory
from filelock import FileLock
import re
import json
import os
import subprocess

def get_scene_change(values,matching_scene):
    """Reads data sent from emulator compares the data to the game dictionaries and returns a string of the current location
    
    Arguments:
        values: Data sent from the emulator. Contains game, scene value, previous scene value
        matching_scene: Previous matching scene. Used to prevent duplicate updates when someone enters back from sublocations in a location

    return:
        matching_scene: Current Location
    """

    data = load_data()
    if not data:
        raise ValueError("There is no data to load")

    if "game" in values:
        if values["game"] == "mm":
            scene_dict = SCENE_DIC_MM
        else:
            scene_dict = SCENE_DIC_OOT
    if "scene" in values:
        scene = values["scene"]
    else:
        scene = "No Scene"
    if "previousScene" in values:
        pscene = values["previousScene"]

    if scene in scene_dict:
        scene = scene_dict[scene]
    if pscene in scene_dict:
        pscene = scene_dict[pscene]
    else:
        pscene = None

    clear_terminal()
    print(pscene, " -> ",scene)
    print()
    print_dungeons(data)
    print_indexwarp()

    raw_scene = scene
    scene = process_location_strings(scene,)

    # If scene from emulator == a location in the spoiler data and player is not in the same area (including subareas). set the current scene
    if scene in data and matching_scene != scene or raw_scene in BOSS_ENTRANCES:
 
        #print(f"Location: {scene}")
        #print(f"n checks: {checked}/{data[scene]["checks"]}")
        #for check in data[scene]["locations"]:
            #print("    " + check["location"])

        if raw_scene in BOSS_ENTRANCES:
            check_boss_entrance(matching_scene,raw_scene,data)
        else:
            check_dungeon_entrance(matching_scene,scene,data)
            matching_scene = scene
            save_matching_scene(matching_scene)
        clear_terminal()
        print(pscene, " -> ",scene)
        print()
        print_dungeons(data)
        print_indexwarp()
        
    return matching_scene
def print_indexwarp():
    print()
    print(f"""{"--Index Warp--":>40} 

{"Great Bay":>30} -> Great Bay 
{"Zora Hall":>30} -> Zora Cape 
{"Romani Ranch":>30} -> Snowhead 
{"Deku Palace":>30} -> Mountain Village 
{"Woodfall":>30} -> Clock Town 
{"Clock Town":>30} -> Milk Road 
{"Snowhead":>30} -> Woodfall                               
{"Ikana Graveyard":>30} -> Southern Swamp                               
{"Ikana Canyon":>30} -> Ikana Canyon                               
{"Goron Village":>30} -> Stone Tower                               
{"Stone Tower":>30} -> Dungeon Entrance (softlock)          

{"--Tingle Map Location--":>45}

{"North Clock Town":>30}: Clock Town, Woodfall
{"Road to Souther Swamp":>30}: Woodfall, Snowhead
{"Twin Islands":>30}: Snowhead, Romani Ranch
{"Milk Road":>30}: Romani Ranch, Great Bay
{"Great Bay Coast":>30}: Great Bay, Stone Tower
{"Ikana Canyon":>30}: Stone Tower , Clock Town
""")
    


def check_dungeon_entrance(previous, current, data):
    
    
    dungeon = ""
    if (
        current in DUNGEON_ENTRANCES
        and not any(
            dungeon_data["dungeon"] == current
            for dungeon_data in data["dungeons"].values()
        )
    ) or (
        current == DUNGEON_ENTRANCES[-1]
        and sum(
            dungeon_data["dungeon"] == DUNGEON_ENTRANCES[-1]
            for dungeon_data in data["dungeons"].values()
        ) < 2
    ):
        
        match previous:

            case "Kokiri Forest":
                dungeon = DUNGEON_ENTRANCES[0]

            case "Death Mountain Trail":
                dungeon = DUNGEON_ENTRANCES[1]

            case "Zora's Fountain":
                c = input(
                    "Enter (1) for Jabu\n"
                    "Enter (2) for Ice Cavern\n"
                    "Enter (q) to quit: "
                )

                if c == "1":
                    dungeon = DUNGEON_ENTRANCES[2]

                elif c == "2":
                    dungeon = DUNGEON_ENTRANCES[9]

                else:
                    print("Location was not saved")

            case "Sacred Forest Meadow":
                dungeon = DUNGEON_ENTRANCES[3]

            case "Death Mountain Crater":
                dungeon = DUNGEON_ENTRANCES[4]

            case "Lake Hylia":
                dungeon = DUNGEON_ENTRANCES[5]

            case "Graveyard":
                dungeon = DUNGEON_ENTRANCES[6]

            case "Desert Colossus":
                dungeon = DUNGEON_ENTRANCES[7]

            case "Kakariko":
                dungeon = DUNGEON_ENTRANCES[8]

            case "Gerudo's Fortress":
                dungeon = DUNGEON_ENTRANCES[10]

            case "Woodfall":
                dungeon = DUNGEON_ENTRANCES[11]

            case "Great Bay Coast":
                c = input(
                    "Enter (1) for Ocean Spider House\n"
                    "Enter (2) for Pirates' Fortress Exterior\n"
                    "Enter (q) to quit: "
                )

                if c == "1":
                    dungeon = DUNGEON_ENTRANCES[22]
                elif c == "2":
                    dungeon = DUNGEON_ENTRANCES[18]

                else:
                    print("Location was not saved")
            case "Zora Cape":
                dungeon = DUNGEON_ENTRANCES[12]

            case "Snowhead":
                dungeon = DUNGEON_ENTRANCES[13]

            case "Stone Tower":
                c = input(
                    "Enter (1) for Stone Tower Temple\n"
                    "Enter (2) for Inverted Stone Tower Temple\n"
                    "Enter (q) to quit: "
                )

                if c == "1":
                    dungeon = DUNGEON_ENTRANCES[14]

                elif c == "2":
                    dungeon = DUNGEON_ENTRANCES[15]

                else:
                    print("Location was not saved")

            case "Ikana Canyon":
                c = input(
                    "Enter (1) for Beneath The Well Canyon\n"
                    "Enter (2) for Secret Shrine\n"
                    "Enter (q) to quit: "
                )

                if c == "1":
                    dungeon = DUNGEON_ENTRANCES[16]

                elif c == "2":
                    dungeon = DUNGEON_ENTRANCES[19]

                else:
                    print("Location was not saved")

            case "Ikana Castle":
                c = input(
                    "Enter (1) for Beneath The Well Exit\n"
                    "Enter (2) for Ikana Castle\n"
                    "Enter (q) to quit: "
                )

                if c == "1":
                    dungeon = DUNGEON_ENTRANCES[17]

                elif c == "2":
                    dungeon = DUNGEON_ENTRANCES[20]

                else:
                    print("Location was not saved")

            case "Southern Swamp":
                dungeon = DUNGEON_ENTRANCES[21]

            case "South Clock Town":
                dungeon = DUNGEON_ENTRANCES[23]
            case "Outside Ganon's Castle":
                dungeon = DUNGEON_ENTRANCES[24]

    if dungeon != "":
        data["dungeons"][dungeon]["dungeon"] = current
        print("Dungeon: ", dungeon, " -> ", current)
        save_data(data)

def check_boss_entrance(dungeon,boss_room,data):

    if boss_room in BOSS_ENTRANCES and not any(
            dungeon_data["boss"] == boss_room
            for dungeon_data in data["dungeons"].values()
        ):
            
        dungeon_key = next(
        key
        for key, dungeon_data in data["dungeons"].items()
        if dungeon_data["dungeon"] == dungeon
    )

        data["dungeons"][dungeon_key]["boss"] = boss_room
        save_data(data)



    
def print_dungeons(data):
    print(f"{"--Dungeons--":>40}")
    print()
    dungeon_space_index = [7,10,15,20,22]
    for i,dungeon in enumerate(data["dungeons"]):
        print(f"{dungeon:>30} -> {data["dungeons"][dungeon]["dungeon"]} {f"-> {data["dungeons"][dungeon]["boss"]}" if data["dungeons"][dungeon]["boss"] != "" else "" }")
        if i in dungeon_space_index:
            print()

def delete_dungeon_entrance(entrance,data):
    data["dungeons"][entrance] = ""

def text_to_dict(text):
    """Takes a processed spoiler file and formats it to a dictionary"""
    data = {"dungeons": {}}

    for entrance in DUNGEON_ENTRANCES[:-1]:
        data["dungeons"][entrance] = {"dungeon": "","boss": ""}

    current_key = None
    current_checks = 0
    current_locations = []

    for line in text.splitlines():
        line = line.strip()

        # Ignore empty lines
        if not line:
            continue

        # Check for a section header such as:
        # South Clock Town (10)
        match = re.match(r"^(.*?)\s*\((\d+)\)\s*$", line)

        if match:
            # Save the previous section
            if current_key is not None:
                data[current_key] = {
                    "checks": current_checks,
                    "checked_locations": 0,
                    "locations": [
                    {
                        "location": location.split(":", 1)[0].strip(),
                        "checked": True if " SR " in location.split(":", 1)[0].strip() and "Silver Rupee (" in location.split(":", 1)[1].strip() else False,
                        "junk": False,
                        "item": location.split(":", 1)[1].strip() if ":" in location else "",
                        "description": ""
                    }
                    
                    for location in current_locations
                    ]
                }

            # Start a new section
            current_key = match.group(1).strip()
            current_checks = int(match.group(2))
            current_locations = []

        else:
            # This is a location belonging to the current section
            if current_key is not None:
                current_locations.append(line)

    # Save the final section
    if current_key is not None:
        data[current_key] = {
            "checks": current_checks,
            "checked_locations": 0,
            "locations": [
            {
                "location": location.split(":", 1)[0].strip(),
                "checked": False,
                "junk": False,
                "item": location.split(":", 1)[1].strip() if ":" in location else "",
                "description": ""
            }
            
            for location in current_locations
            ]
        }

    return data

def set_starting_items(data):

    for scene in data:
        if "starting items" in scene.lower():
            for item in data[scene].get("locations", []):
                item["checked"] = True
        if "pocket" in scene.lower():
            for item in data[scene].get("locations", []):
                item["checked"] = True
    return data

def set_junk_locations(data):
    junk_locations = {
        junk["location"]
        for scene in data
        if "junk locations" in scene.lower()
        for junk in data[scene].get("locations", [])
    }

    for scene in data.values():
        for location in scene.get("locations", []):
            if location["location"] in junk_locations:
                location["junk"] = True
    return data

def create_check_dict():
    """Takes a raw spoiler file, processes the data, formats it to a dictionary, saves it to a json and returns the dictionary
        This is creating a new savefile
    """
    process_spoiler_file("spoiler_file.txt")
    # Put your input text in input.txt
    with open("new_spoiler_file.txt", "r", encoding="utf-8") as file:
        text = file.read()

    # Convert text to dictionary
    data = text_to_dict(text)
    data = set_starting_items(data)
    data = set_junk_locations(data)

    # Save as JSON
    save_data(data, init = True)

    print("Created locations.json")

    # The data variable is also a normal Python dictionary
    return data

def load_data():
    """Load locations.json."""

    filelock = f"{LOCATIONS_FILE}.lock"
    with FileLock(filelock):

        if not os.path.exists(LOCATIONS_FILE):
            return None

        with open(LOCATIONS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)


def save_data(data, init = False):
    """Save locations.json."""

    filelock = f"{LOCATIONS_FILE}.lock"
    with FileLock(filelock):
        with open(LOCATIONS_FILE, "w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

        if not init: # not used when creating new file, only when you start checking off checks 
            with open(BACKUP_LOCATIONS_FILE, "w", encoding="utf-8") as file:
                json.dump(
                    data,
                    file,
                    indent=4,
                    ensure_ascii=False
                )



def save_matching_scene(matching_scene):
    """Save the current matching scene for the flask app to use."""

    data = {
        "matching_scene": matching_scene
    }

    with open(
        CURRENT_SCENE_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )
    


def load_matching_scene():
    """Load the current matching scene for the flask app to use"""

    if not os.path.exists(CURRENT_SCENE_FILE):
        return ""

    try:

        with open(
            CURRENT_SCENE_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

            return data.get(
                "matching_scene",
                ""
            )

    except (
        json.JSONDecodeError,
        OSError
    ):

        return ""

def process_spoiler_file(text_file):
    """Extracting the data from the raw spoiler file and turns it into a simple checklist with
        Also removes Boss spoiler from the location name.
    """

    new_spoiler_log = []
    junk_locations = []
    starting_items = []
    a = False
    b = False
    c = False
    with open(text_file,"r", encoding="utf-8") as file:
        text = file.readlines()

    for line in text:
        if "starting items" in line.lower():
            a = True
            continue
        if line.strip() != "" and a == True:
            line = line[:line.find(":")] 
            starting_items.append(f"{line.strip()}:{line.strip()}")
            continue
        if a == True:
            a = False
            starting_items.insert(0,f"Starting Items ({len(starting_items)})")


        if "junk locations" in line.lower():
            b = True
            continue
        if line.strip() != "" and b == True:
            junk_locations.append(line.strip())
            continue
        if b == True:
            b = False
            junk_locations.insert(0,f"Junk Locations ({len(junk_locations)})")

        if "location list (" in line.lower():
            c = True
            continue
        elif c == False:
            continue
        if line.strip() == "":
            continue
        if line.endswith(":\n"):
            line = line.strip().replace(":","")

        # Remove if you want boss spoiler
        if "Boss Container:" in line:
            line = line.replace("Boss Container","Boss HC")
        if "Boss:" in line and not "Near Boss" in line:
            line = line[line.index("Boss:"):]
        if "Boss HC:" in line:
            line = line[line.index("Boss HC:"):]
        if "Boss Chest:" in line:
            line = line[line.index("Boss Chest:"):]

        new_spoiler_log.append(line.strip())

    new_spoiler_log += starting_items
    new_spoiler_log += junk_locations

    with open("new_spoiler_file.txt","w",encoding="utf-8") as file:
        file.write("\n".join(new_spoiler_log))


def process_location_strings(scene: str) -> str:
    """Converts a location string to the correct string
        Used when spoiler_log location and scene tables don't match
    """
    if "market" in scene.lower():
        scene = "Market"
    if "inside ganon's castle" in scene.lower():
        scene = "Ganon's Castle"
    if "kakariko village" in scene.lower():
        scene = "Kakariko"
    if "stone tower temple (inverted)" in scene.lower():
        scene = "Inverted Stone Tower Temple"
    if "ganon's castle exterior" in scene.lower():
        scene = "Outside Ganon's Castle"
    if "ganon's tower" in scene.lower():
        scene = "Ganon's Castle Tower"
    if "southern swamp (" in scene.lower():
        scene = "Southern Swamp"
    if "inside the deku tree" in scene.lower():
        scene = "Deku Tree"
    if "(winter)" in scene.lower() or "(spring)" in scene.lower():
        scene = scene.replace(" (Winter)","")
        scene = scene.replace(" (Spring)","")
    if "path to goron village" in scene.lower():
        scene = "Twin Islands"
    if "path to snowhead" in scene.lower():
        scene = "Road to Snowhead"
    if "inside jabu-jabu's belly" in scene.lower():
        scene = "Jabu-Jabu's Belly"
    if "oceanside spider house" in scene.lower():
        scene = "Ocean Spider House"
    if "ancient castle of ikana" in scene.lower():
        scene = "Ikana Castle"
    if "beneath the well" in scene.lower():
        scene = "Beneath The Well"
    if "clock tower rooftop" in scene.lower():
        scene = "Clock Tower Roof"
    if "gerudo training ground" in scene.lower():
        scene = "Gerudo's Training Ground"



    return scene


def clear_terminal():
    command = "cls" if os.name == "nt" else "clear"
    subprocess.run([command], shell=os.name == "nt")