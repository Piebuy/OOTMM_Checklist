from globals import SCENE_DIC_OOT, SCENE_DIC_MM, CURRENT_SCENE_FILE, LOCATIONS_FILE,BACKUP_LOCATIONS_FILE
import re
import json
import os

def get_scene_change(values,data,matching_scene):
    """Reads data sent from emulator compares the data to the game dictionaries and returns a string of the current location
    
    Arguments:
        values: Data sent from the emulator. Contains game, scene value, previous scene value
        data: A dictionary containing the all the locations and checked value. Basicly the savefile.
        matching_scene: Previous matching scene. Used to prevent duplicate updates when someone enters back from sublocations in a location

    return:
        matching_scene: Current Location
    """

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

    scene = process_location_strings(scene)

    # If scene from emulator == a location in the spoiler data and player is not in the same area (including subareas). set the current scene
    if scene in data and matching_scene != scene:
        checked = sum(
                1
                for check in data[scene]["locations"]
                if check["checked"] is True
            )
        
        print(f"Location: {scene}")
        print(f"n checks: {checked}/{data[scene]["checks"]}")
        for check in data[scene]["locations"]:
            print("    " + check["location"])

        matching_scene = scene
        save_matching_scene(matching_scene)
    return matching_scene



def text_to_dict(text):
    """Takes a processed spoiler file and formats it to a dictionary"""
    data = {}

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
                        "checked": False,
                        "item": location.split(":", 1)[1].strip() if ":" in location else ""
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
                "item": location.split(":", 1)[1].strip() if ":" in location else ""
            }
            
            for location in current_locations
            ]
        }

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

    # Save as JSON
    save_data(data, init = True)

    print("Created locations.json")

    # The data variable is also a normal Python dictionary
    return data

def load_data():
    """Load locations.json."""

    if not os.path.exists(LOCATIONS_FILE):
        return None

    with open(LOCATIONS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_data(data, init = False):
    """Save locations.json."""

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
    b = False
    with open(text_file,"r", encoding="utf-8") as file:
        text = file.readlines()

    for line in text:
        if "location list (" in line.lower():
            b = True
            continue
        elif b == False:
            continue
        if line.strip() == "":
            continue
        if line.endswith(":\n"):
            line = line.strip().replace(":","")

        # Remove if you want boss spoiler
        if "Boss:" in line:
            line = line[line.index("Boss:"):]
        if "Boss HC:" in line:
            line = line[line.index("Boss HC:"):]

        new_spoiler_log.append(line.strip())

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

    return scene


