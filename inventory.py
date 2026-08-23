from globals import TRACKER_ITEMS

def update_inventory(data):
    all_items = load_inventory(data)
    new_inventory = []

    for item in TRACKER_ITEMS:
        for inventory_item in all_items:
            if item in inventory_item.lower():
                new_inventory.append(inventory_item.lower())

    inventory = {
        "deku sticks (oot)": 10 + 10 * new_inventory.count("deku stick upgrade (oot)"),
        "deku nuts (oot)": 20 + 10 * new_inventory.count("deku nut upgrade (oot)"),

        "bombs (oot)": (
            10 + 10 * new_inventory.count("bomb bag (oot)")
            if new_inventory.count("bomb bag (oot)") > 0 else 0
        ),

        "fairy bow (oot)": (
            20 + 10 * new_inventory.count("fairy bow (oot)")
            if new_inventory.count("fairy bow (oot)") > 0 else 0
        ),

        "fire arrows (oot)": "fire arrows(oot)" in new_inventory,
        "din's fire (oot)": "din's fire (oot)" in new_inventory,
        "kokiri sword (oot)": "kokiri sword (oot)" in new_inventory,
        "deku shield (oot)": "deku shield (oot)" in new_inventory,
        "fairy slingshot (oot)": "fairy slingshot" in new_inventory,

        # 0 = no ocarina, 1 = Fairy Ocarina, 2 = Ocarina of Time
        "ocarina": new_inventory.count("progressive ocarina"),

        "bombchu (oot)": (
            10 + 10 * new_inventory.count("bombchu bag (oot)")
            if new_inventory.count("bombchu bag (oot)") > 0 else 0
        ),

        # 0 = none, 1 = Hookshot, 2 = Longshot
        "hookshot (oot)": new_inventory.count("progressive hookshot (oot)"),

        "ice arrows (oot)": "ice arrows (oot)" in new_inventory,
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
        "zeldas lullaby (oot)": "zeldas lullaby" in new_inventory,
        "eponas song (oot)": "eponas song" in new_inventory,
        "sarias song (oot)": "sarias song" in new_inventory,
        "sunsong (oot)": "sunsong" in new_inventory,
        "song of time (oot)": "song of time" in new_inventory,
        "song of storm (oot)": "song of storm" in new_inventory,

        # Boots / tunics
        "iron boots (oot)": "iron boots" in new_inventory,
        "hoover boots (oot)": "hoover boots" in new_inventory,
        "goron tunic (oot)": "goron tunic" in new_inventory,
        "zora tunic (oot)": "zora tunic" in new_inventory,

        # Adult warp songs
        "minuet of forest (oot)": "minuet of forest" in new_inventory,
        "bolero of fire (oot)": "bolero of fire" in new_inventory,
        "serenade of water (oot)": "serenade of water" in new_inventory,
        "requiem of spirit (oot)": "requiem of spirit" in new_inventory,
        "nocturne of shadow (oot)": "nocturne of shadow" in new_inventory,
        "prelude of light (oot)": "prelude of light" in new_inventory,

        # Bottles / equipment upgrades
        "letter in a bottle (oot)": "letter in a bottle" in new_inventory,
        "empty bottles (oot)": new_inventory.count("empty bottle (oot)"),
        "progressive scale (oot)": new_inventory.count("progressive scale (oot)"),
        "progressive magic (oot)": new_inventory.count("progressive magic (oot)"),
        "progressive strength (oot)": new_inventory.count("progressive strength (oot)"),
        "progressive wallet (oot)": new_inventory.count("progressive wallet"),

        "golden skulltula tokens (oot)": new_inventory.count("gold skulltula token") if "platinum token (oot)" not in new_inventory else 100,
        "stone of agony (oot)": "stone of agony (oot)" in new_inventory,
        "gerudo's membership card (oot)": "gerudo's membership card" in new_inventory,

        # Egg / mask trading sequence
        "weird egg (oot)": "weird egg" in new_inventory,
        "zelda's letter (oot)": "zelda's letter" in new_inventory,
        "keaton mask (oot)": "keaton mask" in new_inventory,
        "skull mask (oot)": "skull mask" in new_inventory,
        "spooky mask (oot)": "spooky mask" in new_inventory,
        "bunny mask (oot)": "bunny mask" in new_inventory,
        "mask of truth (oot)": "mask of truth" in new_inventory,

        "pocket cucco (oot)": "pocket cucco" in new_inventory,
        "cojiro (oot)": "cojiro" in new_inventory,
        "odd mushroom (oot)": "odd mushroom" in new_inventory,
        "odd potion (oot)": "odd potion" in new_inventory,
        "poachers saw (oot)": "poachers saw" in new_inventory,
        "broken goron's sword (oot)": "broken goron's sword" in new_inventory,
        "prescription (oot)": "prescription" in new_inventory,
        "eyeball frog (oot)": "eyeball frog" in new_inventory,
        "eye drops (oot)": "eye drops" in new_inventory,
        "claim check (oot)": "claim check" in new_inventory,

        # Medallions
        "forest medallion (oot)": "forest medallion" in new_inventory,
        "fire medallion (oot)": "fire medallion" in new_inventory,
        "water medallion (oot)": "water medallion" in new_inventory,
        "spirit medallion (oot)": "spirit medallion" in new_inventory,
        "shadow medallion (oot)": "shadow medallion" in new_inventory,
        "light medallion (oot)": "light medallion" in new_inventory,

        # Dungeon keys
        "forest temple small key (oot)": new_inventory.count("small key (forest temple)"),
        "forest temple boss key (oot)": "boss key (forest temple)" in new_inventory,

        "fire temple small key (oot)": new_inventory.count("small key (fire temple)"),
        "fire temple boss key (oot)": "boss key (fire temple)" in new_inventory,

        "water temple small key (oot)": new_inventory.count("small key (water temple)"),
        "water temple boss key (oot)": "boss key (water temple)" in new_inventory,

        "spirit temple small key (oot)": new_inventory.count("small key (spirit temple)"),
        "spirit temple boss key (oot)": "boss key (spirit temple)" in new_inventory,

        "shadow temple small key (oot)": new_inventory.count("small key (shadow temple)"),
        "shadow temple boss key (oot)": "boss key (shadow temple)" in new_inventory,

        "ganons castle small key (oot)": new_inventory.count("small key (ganon's castle)"),

        "gerudo training ground small key (oot)": new_inventory.count(
            "small key (gerudo's training ground)"
        ),

        "thieves hideout key ring (oot)": "small key ring (hideout)" in new_inventory,

        "bottom of the well small key (oot)": new_inventory.count(
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
        "progressive swords (mm)": new_inventory.count("progressive sword (mm)"),

        "hero's shield (mm)": "hero's shield (mm)" in new_inventory,
        "mirror shield (mm)": "mirror shield (mm)" in new_inventory,

        # ============================================================
        # CONSUMABLES / UPGRADES
        # ============================================================

        "bombs (mm)": (
            20 + 10 * new_inventory.count("bomb bag (mm)")
            if new_inventory.count("bomb bag (mm)") > 0 else 0
        ),

        "bombchus (mm)": (
            10 + 10 * new_inventory.count("bombchu bag (mm)")
            if new_inventory.count("bombchu bag (mm)") > 0 else 0
        ),

        "deku sticks (mm)": (
            10 + 10 * new_inventory.count("deku stick upgrade (mm)")
        ),

        "deku nuts (mm)": (
            20 + 10 * new_inventory.count("deku nut upgrade (mm)")
        ),

        "magic beans (mm)": "magic beans (mm)" in new_inventory,

        "gold dust (mm)": "gold dust (mm)" in new_inventory,

        "empty bottles (mm)": new_inventory.count("empty bottle (mm)"),

        "power keg (mm)": "power keg (mm)" in new_inventory,

        "pictograph box (mm)": "pictograph box (mm)" in new_inventory,

        "lens of truth (mm)": "lens of truth (mm)" in new_inventory,

        # 0 = none, 1 = Hookshot
        "hookshot (mm)": new_inventory.count("progressive hookshot (mm)"),

        "fairy sword (mm)": "fairy sword (mm)" in new_inventory,

        # ============================================================
        # MAGIC / SHARED UPGRADES
        # ============================================================

        "din's fire (mm)": "din's fire (mm)" in new_inventory,

        # Same shared wallet progression as OoT
        "wallet (mm)": new_inventory.count("progressive wallet"),

        "progressive magic (mm)": new_inventory.count("progressive magic (mm)"),

        # ============================================================
        # SONGS
        # ============================================================

        "song of time (mm)": "song of time (mm)" in new_inventory,
        "song of healing (mm)": "song of healing (mm)" in new_inventory,
        "epona's song (mm)": "epona's song (mm)" in new_inventory,
        "song of soaring (mm)": "song of soaring (mm)" in new_inventory,
        "song of storms (mm)": "song of storms (mm)" in new_inventory,
        "sonata of awakening (mm)": "sonata of awakening (mm)" in new_inventory,
        "goron's lullaby (mm)": "goron's lullaby (mm)" in new_inventory,

        # 0 = none, 1 = Bossanova, 2 = New Wave Bossanova
        "bossanowa (mm)": new_inventory.count("progressive bossanowa (mm)"),

        "elegy of emptiness (mm)": "elegy of emptiness (mm)" in new_inventory,
        "oath of order (mm)": "oath of order (mm)" in new_inventory,

        # ============================================================
        # STRAY FAIRIES
        # ============================================================

        "clock town stray fairies (mm)": new_inventory.count(
            "stray fairy (clock town)"
        ), # Not sure if transcendet affect town fairy

        "woodfall temple stray fairies (mm)": new_inventory.count(
            "stray fairy (woodfall temple)"
        ) if "transcendent fairy" not in new_inventory else 15,

        "snowhead temple stray fairies (mm)": new_inventory.count(
            "stray fairy (snowhead temple)"
        ) if "transcendent fairy" not in new_inventory else 15,

        "great bay temple stray fairies (mm)": new_inventory.count(
            "stray fairy (great bay temple)"
        ) if "transcendent fairy" not in new_inventory else 15,

        "stone tower temple stray fairies (mm)": new_inventory.count(
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

        "woodfall temple small keys (mm)": new_inventory.count(
            "small key (woodfall temple)"
        ),

        "snowhead temple small keys (mm)": new_inventory.count(
            "small key (snowhead temple)"
        ),

        "great bay temple small keys (mm)": new_inventory.count(
            "small key (great bay temple)"
        ),

        "stone tower temple small keys (mm)": new_inventory.count(
            "small key (stone tower temple)"
        ),

        # ============================================================
        # DUNGEON BOSS KEYS
        # ============================================================

        "woodfall temple boss key (mm)": (
            "boss key (woodfall temple)" in new_inventory
        ),

        "snowhead temple boss key (mm)": (
            "boss key (snowhead temple)" in new_inventory
        ),

        "great bay temple boss key (mm)": (
            "boss key (great bay temple)" in new_inventory
        ),

        "stone tower temple boss key (mm)": (
            "boss key (stone tower temple)" in new_inventory
        ),

        # ============================================================
        # DUNGEON REMAINS
        # ============================================================

        "odolwa remains (mm)": "odolwa remains (mm)" in new_inventory,
        "goht remains (mm)": "goht remains (mm)" in new_inventory,
        "gyorg remains (mm)": "gyorg remains (mm)" in new_inventory,
        "twinmold remains (mm)": "twinmold remains (mm)" in new_inventory,

        # ============================================================
        # STORY / TRADING ITEMS
        # ============================================================

        "moon tear (mm)": "moon tear" in new_inventory,

        "pendant of memories (mm)": (
            "pendant of memories" in new_inventory
        ),

        "letter to kafei (mm)": (
            "letter to kafei" in new_inventory
        ),

        "mama's letter (mm)": (
            "mama's letter" in new_inventory
        ),

        "land title deed (mm)": (
            "land title deed" in new_inventory
        ),

        "forest title deed (mm)": (
            "forest title deed" in new_inventory
        ),

        "mountain title deed (mm)": (
            "mountain title deed" in new_inventory
        ),

        "ocean title deed (mm)": (
            "ocean title deed" in new_inventory
        ),

        "room key (mm)": "room key" in new_inventory,

        # ============================================================
        # MASKS — EXACTLY 24 MM MASKS
        # ============================================================

        # Transformation masks
        "deku mask (mm)": "deku mask" in new_inventory,
        "goron mask (mm)": "goron mask" in new_inventory,
        "zora mask (mm)": "zora mask" in new_inventory,
        "fierce deity mask (mm)": "fierce deity mask" in new_inventory,

        # Fairy / basic masks
        "great fairy's mask (mm)": (
            "great fairy's mask" in new_inventory
        ),

        "bunny hood (mm)": "bunny hood" in new_inventory,
        "blast mask (mm)": "blast mask (mm)" in new_inventory,
        "stone mask (mm)": "stone mask (mm)" in new_inventory,

        # Animal / character masks
        "keaton mask (mm)": "keaton mask" in new_inventory,
        "bremen mask (mm)": "bremen mask" in new_inventory,
        "don gero's mask (mm)": "don gero's mask" in new_inventory,
        "mask of scents (mm)": "mask of scents" in new_inventory,

        "captain's hat (mm)": "captain's hat" in new_inventory,
        "garo's mask (mm)": "garo's mask" in new_inventory,
        "gibdo mask (mm)": "gibdo mask" in new_inventory,

        "romani's mask (mm)": "romani's mask" in new_inventory,
        "couple's mask (mm)": "couple's mask" in new_inventory,
        "kamaro's mask (mm)": "kamaro's mask" in new_inventory,

        "postman's hat (mm)": "postman's hat" in new_inventory,
        "all-night mask (mm)": "all-night mask" in new_inventory,

        "circus leader's mask (mm)": (
            "circus leader's mask" in new_inventory
        ),

        "kafei's mask (mm)": "kafei's mask" in new_inventory,

        "mask of truth (mm)": "mask of truth" in new_inventory,

        "giant's mask (mm)": "giant's mask" in new_inventory,
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


