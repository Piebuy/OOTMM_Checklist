from globals import TRACKER_ITEMS
from inventory_service import process_item_string

def update_inventory(data):
    all_items = load_inventory(data)
    new_inventory = []

    for i in range(all_items.count("Empty Bottle (OoT)")):
        new_inventory.append("empty bottle (oot)")
    for i in range(all_items.count("Empty Bottle (MM)")):
            new_inventory.append("empty bottle (mm)")
    for i in range(all_items.count("Progressive Ocarina")):
        new_inventory.append("progressive ocarina")
    for i in range(all_items.count("Progressive Wallet")):
        new_inventory.append("progressive wallet")
    if "Bottle of Milk (OoT)" in all_items:
        new_inventory.append("empty bottle (oot)") 
    if "Bottle of Red Potion (MM)" in all_items:
        new_inventory.append("empty bottle (mm)")
    if "Bottle of Chateau Romani" in all_items:
        new_inventory.append("empty bottle (mm)")
    if "Bottle of Milk (MM)" in all_items:
        new_inventory.append("empty bottle (mm)")
    if "Platinum Token (OoT)" in all_items:
        new_inventory.append("platinum token (oot)")
    if "Platinum Token (MM)" in all_items:
        new_inventory.append("platinum token (mm)")
    if "Transcendent Fairy" in all_items:
        new_inventory.append("transcendent fairy")
    if "Keaton Mask" in all_items:
        new_inventory.append("keaton mask (mm)")
    if "Bunny Hood" in all_items:
        new_inventory.append("bunny hood")
    new_inventory.append("zelda's letter")

    new_inventory = process_item_string(all_items,new_inventory,TRACKER_ITEMS)
    

    inventory = {
        "deku stick upgrade (oot)": 10 + 10 * new_inventory.count("deku stick upgrade (oot)"),
        "deku nut upgrade (oot)": 20 + 10 * new_inventory.count("deku nut upgrade (oot)"),

        "bomb bag (oot)": (
            10 + 10 * new_inventory.count("bomb bag (oot)")
            if new_inventory.count("bomb bag (oot)") > 0 else 0
        ),

        "fairy bow (oot)": (
            20 + 10 * new_inventory.count("fairy bow (oot)")
            if new_inventory.count("fairy bow (oot)") > 0 else 0
        ),

        "fire arrows (oot)": "fire arrows (oot)" in new_inventory,
        "din's fire (oot)": "din's fire (oot)" in new_inventory,
        "kokiri sword (oot)": "kokiri sword (oot)" in new_inventory,
        "deku shield (oot)": "deku shield (oot)" in new_inventory,
        "fairy slingshot (oot)": (
            20 + 10 * new_inventory.count("fairy slingshot (oot)")
            if new_inventory.count("fairy slingshot (oot)") > 0 else 0
        ),

        # 0 = no ocarina, 1 = Fairy Ocarina, 2 = Ocarina of Time
        "ocarina (oot)": new_inventory.count("progressive ocarina"),

        "bombchu bag (oot)": (
            10 + 10 * new_inventory.count("bombchu bag (oot)")
            if new_inventory.count("bombchu bag (oot)") > 0 else 0
        ),

        # 0 = none, 1 = Hookshot, 2 = Longshot
        "hookshot (oot)": new_inventory.count("progressive hookshot (oot)"),

        "ice arrows (oot)": "ice arrows (oot)" in new_inventory,
        "farore's wind (oot)": "farore's wind" in new_inventory, #TODO: Need mapping in tracker.py
        "master sword (oot)": "master sword" in new_inventory,
        "hylian shield (oot)": "hylian shield" in new_inventory,
        "boomerang (oot)": "boomerang (oot)" in new_inventory,
        "lens of truth (oot)": "lens of truth (oot)" in new_inventory,
        "magic beans (oot)": "magic beans (oot)" in new_inventory,
        "megaton hammer (oot)": "megaton hammer (oot)" in new_inventory,
        "light arrows (oot)": "light arrows (oot)" in new_inventory,
        "nayru's love (oot)": "nayru's love (oot)" in new_inventory,
        "biggoron's sword (oot)": "biggoron's sword" in new_inventory,
        "mirror shield (oot)": "mirror shield (oot)" in new_inventory,

        # Songs
        "zelda's lullaby (oot)": "zelda's lullaby (oot)" in new_inventory,
        "epona's song (oot)": "epona's song" in new_inventory,
        "saria's song (oot)": "saria's song (oot)" in new_inventory,
        "sun's song (oot)": "sun's song (oot)" in new_inventory,
        "song of time (oot)": "song of time (oot)" in new_inventory,
        "song of storms (oot)": "song of storms (oot)" in new_inventory,

        # Boots / tunics
        "iron boots (oot)": "iron boots (oot)" in new_inventory,
        "hover boots (oot)": "hover boots (oot)" in new_inventory,
        "goron tunic (oot)": "goron tunic (oot)" in new_inventory,
        "zora tunic (oot)": "zora tunic (oot)" in new_inventory,

        # Adult warp songs
        "minuet of forest (oot)": "minuet of forest (oot)" in new_inventory,
        "bolero of fire (oot)": "bolero of fire (oot)" in new_inventory,
        "serenade of water (oot)": "serenade of water (oot)" in new_inventory,
        "requiem of spirit (oot)": "requiem of spirit (oot)" in new_inventory,
        "nocturne of shadow (oot)": "nocturne of shadow (oot)" in new_inventory,
        "prelude of light (oot)": "prelude of light (oot)" in new_inventory,

        # Bottles / equipment upgrades
        "ruto's letter (oot)": "ruto's letter" in new_inventory,
        "empty bottle (oot) 2": new_inventory.count("empty bottle (oot)") > 0, 
        "empty bottle (oot) 3": new_inventory.count("empty bottle (oot)") > 1,
        "empty bottle (oot) 4": new_inventory.count("empty bottle (oot)") > 2,
        "progressive scale (oot)": new_inventory.count("progressive scale (oot)"),
        "magic upgrade (oot)": new_inventory.count("magic upgrade (oot)"),
        "progressive strength (oot)": new_inventory.count("progressive strength (oot)"),
        "progressive wallet (oot)": new_inventory.count("progressive wallet"),

        "gold skulltula tokens (oot)": new_inventory.count("gold skulltula token") if "platinum token (oot)" not in new_inventory else 100,
        "stone of agony (oot)": "stone of agony" in new_inventory,
        "gerudo's membership card (oot)": "gerudo's membership card" in new_inventory,
        # Egg / mask trading sequence
        "keaton mask (oot)": "keaton mask (oot)" in new_inventory,
        "skull mask (oot)": "skull mask (oot)" in new_inventory,
        "spooky mask (oot)": "spooky mask (oot)" in new_inventory,
        "bunny hood (oot)": "bunny hood" in new_inventory,
        "mask of truth (oot)": "mask of truth (oot)" in new_inventory,

        "pocket egg (oot)": "pocket egg" in new_inventory,
        "zelda's letter (oot)": "zelda's letter" in new_inventory,
        "pocket cucco (oot)": "pocket cucco" in new_inventory,
        "cojiro (oot)": "cojiro" in new_inventory,
        "odd mushroom (oot)": "odd mushroom" in new_inventory,
        "odd potion (oot)": "odd potion" in new_inventory,
        "poacher's saw (oot)": "poacher's saw" in new_inventory,
        "broken goron's sword (oot)": "broken goron's sword" in new_inventory,
        "prescription (oot)": "prescription" in new_inventory,
        "eyeball frog (oot)": "eyeball frog" in new_inventory,
        "eye drops (oot)": "eye drops" in new_inventory,
        "claim check (oot)": "claim check" in new_inventory,

        # Medallions
        "kokiri's emerald (oot)": "kokiri's emerald" in new_inventory,
        "goron's ruby (oot)": "goron's ruby" in new_inventory,
        "zora's sapphire (oot)": "zora's sapphire" in new_inventory,
        "forest medallion (oot)": "forest medallion" in new_inventory,
        "fire medallion (oot)": "fire medallion" in new_inventory,
        "water medallion (oot)": "water medallion" in new_inventory,
        "spirit medallion (oot)": "spirit medallion" in new_inventory,
        "shadow medallion (oot)": "shadow medallion" in new_inventory,
        "light medallion (oot)": "light medallion" in new_inventory,

        

        # Dungeon keys
        "small key (forest temple) (oot)": new_inventory.count("small key (forest temple)"),
        "boss key (forest temple) (oot)": "boss key (forest temple)" in new_inventory,

        "small key (fire temple) (oot)": new_inventory.count("small key (fire temple)"),
        "boss key (fire temple) (oot)": "boss key (fire temple)" in new_inventory,

        "small key (water temple) (oot)": new_inventory.count("small key (water temple)"),
        "boss key (water temple) (oot)": "boss key (water temple)" in new_inventory,

        "small key (spirit temple) (oot)": new_inventory.count("small key (spirit temple)"),
        "boss key (spirit temple) (oot)": "boss key (spirit temple)" in new_inventory,

        "small key (shadow temple) (oot)": new_inventory.count("small key (shadow temple)"),
        "boss key (shadow temple) (oot)": "boss key (shadow temple)" in new_inventory,

        "small key (ganon's castle) (oot)": new_inventory.count("small key (ganon's castle)"),

        "small key (gerudo's training ground) (oot)": new_inventory.count(
            "small key (gerudo's training ground)"
        ),

        "key ring (hideout) (oot)": "key ring (hideout)" in new_inventory,

        "small key (bottom of the well) (oot)": new_inventory.count(
            "small key (bottom of the well)"
        ),
        # ============================================================
        # Majoras Mask inventory
        # ============================================================

        # 0 = no ocarina, 1 = Fairy Ocarina, 2 = Ocarina of Time
        "ocarina (mm)": new_inventory.count("progressive ocarina"),

        "hero's bow (mm)": (
            20 + 10 * new_inventory.count("hero's bow (mm)")
            if new_inventory.count("hero's bow (mm)") > 0 else 0
        ),

        "fire arrows (mm)": "fire arrows (mm)" in new_inventory,
        "ice arrows (mm)": "ice arrows (mm)" in new_inventory,
        "light arrows (mm)": "light arrows (mm)" in new_inventory,

        # 0 = Kokiri Sword, 1 = Razor Sword, 2 = Gilded Sword
        "progressive sword (mm)": new_inventory.count("progressive sword (mm)"),

        "hero's shield (mm)": "hero's shield" in new_inventory,
        "mirror shield (mm)": "mirror shield (mm)" in new_inventory,

        # ============================================================
        # CONSUMABLES / UPGRADES
        # ============================================================

        "bomb bag (mm)": (
            10 + 10 * new_inventory.count("bomb bag (mm)")
            if new_inventory.count("bomb bag (mm)") > 0 else 0
        ),

        "bombchu bag (mm)": (
            10 + 10 * new_inventory.count("bombchu bag (mm)")
            if new_inventory.count("bombchu bag (mm)") > 0 else 0
        ),

        "deku stick upgrade (mm)": (
            10 + 10 * new_inventory.count("deku stick upgrade (mm)")
        ),

        "deku nut upgrade (mm)": (
            20 + 10 * new_inventory.count("deku nut upgrade (mm)")
        ),

        "magic bean (mm)": "magic bean (mm)" in new_inventory,

        "bottle of gold dust (mm)": "bottle of gold dust" in new_inventory,

        "empty bottle (mm) 2": new_inventory.count("empty bottle (mm)") > 0, 
        "empty bottle (mm) 3": new_inventory.count("empty bottle (mm)") > 1,
        "empty bottle (mm) 4": new_inventory.count("empty bottle (mm)") > 2,
        "empty bottle (mm) 5": new_inventory.count("empty bottle (mm)") > 3,
        "empty bottle (mm) 6": new_inventory.count("empty bottle (mm)") > 4,

        "powder keg (mm)": "powder keg (mm)" in new_inventory,

        "pictograph box (mm)": "pictograph box" in new_inventory,

        "lens of truth (mm)": "lens of truth (mm)" in new_inventory,

        # 0 = none, 1 = Hookshot
        "hookshot (mm)": new_inventory.count("hookshot (mm)"),

        "great fairy's sword (mm)": "great fairy's sword (mm)" in new_inventory,

        # ============================================================
        # MAGIC / SHARED UPGRADES
        # ============================================================

        "din's fire (mm)": "din's fire (mm)" in new_inventory,

        # Same shared wallet progression as OoT
        "progressive wallet (mm)": new_inventory.count("progressive wallet"),

        "magic upgrade (mm)": new_inventory.count("magic upgrade (mm)"),

        # ============================================================
        # SONGS
        # ============================================================

        "song of time (mm)": "song of time (mm)" in new_inventory,
        "song of healing (mm)": "song of healing (mm)" in new_inventory,
        "epona's song (mm)": "epona's song" in new_inventory,
        "song of soaring (mm)": "song of soaring (mm)" in new_inventory,
        "song of storms (mm)": "song of storms (mm)" in new_inventory,

        "sonata of awakening (mm)": "sonata of awakening (mm)" in new_inventory,
        "progressive goron lullaby (mm)": new_inventory.count("progressive goron lullaby (mm)"),
        "new wave bossa nova (mm)": "new wave bossa nova (mm)" in new_inventory,
        "elegy of emptiness (mm)": "elegy of emptiness (mm)" in new_inventory,
        "oath to order (mm)": "oath to order (mm)" in new_inventory,

        # ============================================================
        # STRAY FAIRIES
        # ============================================================

        "stray fairy (clock town) (mm)": new_inventory.count(
            "stray fairy (clock town)"
        ), # Not sure if transcendet affect town fairy

        "stray fairy (woodfall temple) (mm)": new_inventory.count(
            "stray fairy (woodfall temple)"
        ) if "transcendent fairy" not in new_inventory else 15,

        "stray fairy (snowhead temple) (mm)": new_inventory.count(
            "stray fairy (snowhead temple)"
        ) if "transcendent fairy" not in new_inventory else 15,

        "stray fairy (great bay temple) (mm)": new_inventory.count(
            "stray fairy (great bay temple)"
        ) if "transcendent fairy" not in new_inventory else 15,

        "stray fairy (stone tower temple) (mm)": new_inventory.count(
            "stray fairy (stone tower temple)"
        ) if "transcendent fairy" not in new_inventory else 15,

        # ============================================================
        # SKULLTULA TOKENS
        # ============================================================

        "swamp skulltula token (mm)": new_inventory.count(
            "swamp skulltula token"
        ) if "platinum token (mm)" not in new_inventory else 30,

        "ocean skulltula token (mm)": new_inventory.count(
            "ocean skulltula token"
        ) if "platinum token (mm)" not in new_inventory else 30,

        # ============================================================
        # DUNGEON SMALL KEYS
        # ============================================================

        "small key (woodfall temple) (mm)": new_inventory.count(
            "small key (woodfall temple)"
        ),

        "small key (snowhead temple) (mm)": new_inventory.count(
            "small key (snowhead temple)"
        ),

        "small key (great bay temple) (mm)": new_inventory.count(
            "small key (great bay temple)"
        ),

        "small key (stone tower temple) (mm)": new_inventory.count(
            "small key (stone tower temple)"
        ),

        # ============================================================
        # DUNGEON BOSS KEYS
        # ============================================================

        "boss key (woodfall temple) (mm)": (
            "boss key (woodfall temple)" in new_inventory
        ),

        "boss key (snowhead temple) (mm)": (
            "boss key (snowhead temple)" in new_inventory
        ),

        "boss key (great bay temple) (mm)": (
            "boss key (great bay temple)" in new_inventory
        ),

        "boss key (stone tower temple) (mm)": (
            "boss key (stone tower temple)" in new_inventory
        ),

        # ============================================================
        # DUNGEON REMAINS
        # ============================================================

        "odolwa's remains (mm)": "odolwa's remains" in new_inventory,
        "goht's remains (mm)": "goht's remains" in new_inventory,
        "gyorg's remains (mm)": "gyorg's remains" in new_inventory,
        "twinmold's remains (mm)": "twinmold's remains" in new_inventory,

        # ============================================================
        # STORY / TRADING ITEMS
        # ============================================================

        "moon's tear (mm)": "moon's tear" in new_inventory,

        "pendant of memories (mm)": (
            "pendant of memories" in new_inventory
        ),

        "letter to kafei (mm)": (
            "letter to kafei" in new_inventory
        ),

        "letter to mama (mm)": (
            "letter to mama" in new_inventory
        ),

        "land title deed (mm)": (
            "land title deed" in new_inventory
        ),

        "swamp title deed (mm)": (
            "swamp title deed" in new_inventory
        ),

        "mountain title deed (mm)": (
            "mountain title deed" in new_inventory
        ),

        "ocean title deed (mm)": (
            "ocean title deed" in new_inventory
        ),

        "room key (mm)": "room key" in new_inventory,
        # ============================================================
        # Clock pieces
        # ============================================================

        "clock (day 1)": "clock (day 1)" in new_inventory,
        "clock (day 2)": "clock (day 2)" in new_inventory,
        "clock (day 3)": "clock (day 3)" in new_inventory,
        "clock (night 1)": "clock (night 1)" in new_inventory,
        "clock (night 2)": "clock (night 2)" in new_inventory,
        "clock (night 3)": "clock (night 3)" in new_inventory,



        # ============================================================
        # MASKS — EXACTLY 24 MM MASKS
        # ============================================================

        # Transformation masks
        "deku mask (mm)": "deku mask" in new_inventory,
        "goron mask (mm)": "goron mask" in new_inventory,
        "zora mask (mm)": "zora mask" in new_inventory,
        "fierce deity's mask (mm)": "fierce deity's mask" in new_inventory,

        # Fairy / basic masks
        "great fairy's mask (mm)": (
            "great fairy's mask" in new_inventory
        ),

        "bunny hood (mm)": "bunny hood" in new_inventory,
        "blast mask (mm)": "blast mask (mm)" in new_inventory,
        "stone mask (mm)": "stone mask (mm)" in new_inventory,

        # Animal / character masks
        "keaton mask (mm)": "keaton mask (mm)" in new_inventory,
        "bremen mask (mm)": "bremen mask" in new_inventory,
        "don gero's mask (mm)": "don gero's mask" in new_inventory,
        "mask of scents (mm)": "mask of scents" in new_inventory,

        "captain's hat (mm)": "captain's hat" in new_inventory,
        "garo's mask (mm)": "garo's mask" in new_inventory,
        "gibdo mask (mm)": "gibdo mask" in new_inventory,

        "romani's mask (mm)": "romani's mask" in new_inventory,
        "couple's mask (mm)": "couple's mask" in new_inventory,
        "kamaro's mask (mm)": "kamaro's mask (mm)" in new_inventory,

        "postman's hat (mm)": "postman's hat" in new_inventory,
        "all-night mask (mm)": "all-night mask" in new_inventory,

        "circus leader's mask (mm)": (
            "circus leader's mask" in new_inventory
        ),

        "kafei's mask (mm)": "kafei's mask" in new_inventory,

        "mask of truth (mm)": "mask of truth (mm)" in new_inventory,

        "giant's mask (mm)": "giant's mask" in new_inventory,
        "empty":"",
    }

    return inventory

def load_inventory(data):
    if not data:
        return []

    return [
        location.get("item", "")
        for scene_data in data.values()
        if isinstance(scene_data, dict)
        for location in scene_data.get("locations", [])
        if location.get("checked") is True
    ]

def print_inventory(inventory):

    char = 0

    for item in inventory:
        if len(item) > char:
            char = len(item)

    for item, value in inventory.items():
        if not value:
            continue
        print(f"{item:>{char}}: {value}")


