def process_item_string(all_items,new_inventory,tracker_items):
    for item in tracker_items:
        if item == "empty":
            continue
        if "farore's wind" in item:
            item = "farore's wind"
        if "master sword" in item:
            item = "master sword"
        if "hylian shield" in item:
            item = "hylian shield"
        if "biggoron's sword" in item:
            item = "biggoron's sword"
        if "epona's song" in item:
            item = "epona's song"
        if "ruto's letter" in item:
            item = "ruto's letter"
        if "gold skulltula token" in item:
            item = "gold skulltula token"
        if "stone of agony" in item:
            item = "stone of agony"
        if "gerudo's membership" in item:
            item = "gerudo's membership card"
        if "pocket egg" in item:
            item = "pocket egg"
        if "pocket cucco" in item:
            item = "pocket cucco"
        if "cojiro" in item:
            item = "cojiro"
        if "odd mushroom" in item:
            item = "odd mushroom"
        if "odd potion" in item:
            item = "odd potion"
        if "poacher's saw" in item:
            item = "poacher's saw"
        if "broken goron's sword" in item:
            item = "broken goron's sword"
        if "prescription" in item:
            item = "prescription"
        if "eyeball frog" in item:
            item = "eyeball frog"
        if "eye drops" in item:
            item = "eye drops"
        if "claim check" in item:
            item = "claim check"
        if "kokiri's emerald" in item:
            item = "kokiri's emerald"
        if "goron's ruby" in item:
            item = "goron's ruby"
        if "zora's sapphire" in item:
            item = "zora's sapphire"
        if "forest medallion" in item:
            item = "forest medallion"
        if "fire medallion" in item:
            item = "fire medallion"
        if "water medallion" in item:
            item = "water medallion"
        if "spirit medallion" in item:
            item = "spirit medallion"
        if "shadow medallion" in item:
            item = "shadow medallion"
        if "light medallion" in item:
            item = "light medallion"
        if "boss key (forest temple)" in item:
            item = "boss key (forest temple)"
        if "boss key (fire temple)" in item:
            item = "boss key (fire temple)"
        if "boss key (water temple)" in item:
            item = "boss key (water temple)"
        if "boss key (spirit temple)" in item:
            item = "boss key (spirit temple)"
        if "boss key (shadow temple)" in item:
            item = "boss key (shadow temple)"
        if "small key (forest temple)" in item:
            item = "small key (forest temple)"
        if "small key (fire temple)" in item:
            item = "small key (fire temple)"
        if "small key (water temple)" in item:
            item = "small key (water temple)"
        if "small key (spirit temple)" in item:
            item = "small key (spirit temple)"
        if "small key (shadow temple)" in item:
            item = "small key (shadow temple)"
        if "small key (bottom of the well)" in item:
            item = "small key (bottom of the well)"
        if "small key (gerudo's training ground)" in item:
            item = "small key (gerudo's training ground)"
        if "key ring (hideout)" in item:
            item = "key ring (hideout)"
        if "key ring (chest game)" in item:
            item = "key ring (chest game)"
        if "small key (ganon's castle)" in item:
            item = "small key (ganon's castle)"
        if "hero's shield" in item:
            item = "hero's shield"
        if "bottle of gold dust" in item:
            item = "bottle of gold dust"
        if "pictograph box" in item:
            item = "pictograph box"
        if "moon's tear" in item:
            item = "moon's tear"
        if "stray fairy (clock town)" in item:
            item = "stray fairy (clock town)"
        if "room key" in item:
            item = "room key"
        if "land title deed" in item:
            item = "land title deed"
        if "postman's hat" in item:
            item = "postman's hat"
        if "all-night mask" in item:
            item = "all-night mask"
        if "great fairy's mask" in item:
            item = "great fairy's mask"
        if "deku mask" in item:
            item = "deku mask"
        if "pendant of memories" in item:
            item = "pendant of memories"
        if "swamp title deed" in item:
            item = "swamp title deed"
        if "bremen mask" in item:
            item = "bremen mask"
        if "don gero's mask" in item:
            item = "don gero's mask"
        if "mask of scents" in item:
            item = "mask of scents"
        if "goron mask" in item:
            item = "goron mask"
        if "letter to kafei" in item:
            item = "letter to kafei"
        if "mountain title deed" in item:
            item = "mountain title deed"
        if "romani's mask" in item:
            item = "romani's mask"
        if "circus leader's mask" in item:
            item = "circus leader's mask"
        if "kafei's mask" in item:
            item = "kafei's mask"
        if "couple's mask" in item:
            item = "couple's mask"
        if "zora mask" in item:
            item = "zora mask"
        if "letter to mama" in item:
            item = "letter to mama"
        if "ocean title deed" in item:
            item = "ocean title deed"
        if "gibdo mask" in item:
            item = "gibdo mask"
        if "garo's mask" in item:
            item = "garo's mask"
        if "captain's hat" in item:
            item = "captain's hat"
        if "giant's mask" in item:
            item = "giant's mask"
        if "fierce deity's mask" in item:
            item = "fierce deity's mask"
        if "swamp skulltula token" in item:
            item = "swamp skulltula token"
        if "ocean skulltula token" in item:
            item = "ocean skulltula token"
        if "odolwa's remains" in item:
            item = "odolwa's remains"
        if "stray fairy (woodfall temple)" in item:
            item = "stray fairy (woodfall temple)"
        if "stray fairy (snowhead temple)" in item:
            item = "stray fairy (snowhead temple)"
        if "stray fairy (great bay temple)" in item:
            item = "stray fairy (great bay temple)"
        if "stray fairy (stone tower temple)" in item:
            item = "stray fairy (stone tower temple)"
        if "goht's remains" in item:
            item = "goht's remains"
        if "gyorg's remains" in item:
            item ="gyorg's remains"
        if "twinmold's remains" in item:
            item = "twinmold's remains"
        if "small key (woodfall temple)" in item:
            item = "small key (woodfall temple)"
        if "small key (snowhead temple)" in item:
            item = "small key (snowhead temple)"
        if "small key (great bay temple)" in item:
            item = "small key (great bay temple)"
        if "small key (stone tower temple)" in item:
            item = "small key (stone tower temple)"
        if "boss key (woodfall temple)" in item:
            item = "boss key (woodfall temple)"
        if "boss key (snowhead temple)" in item:
            item = "boss key (snowhead temple)"
        if "boss key (great bay temple)" in item:
            item = "boss key (great bay temple)"
        if "boss key (stone tower temple)" in item:
            item = "boss key (stone tower temple)"
        
        for inventory_item in all_items:
            if item.lower() in inventory_item.lower(): # type: ignore
                new_inventory.append(inventory_item.lower())
    return new_inventory