import tkinter as tk
from pathlib import Path
from inventory import update_inventory
from services import load_data
from globals import TRACKER_ITEMS


COLS = 8
ROWS = 12

IMAGE_DIR = Path("img")



# The order in which items appear in the grid
oot_items = TRACKER_ITEMS[:96]

mm_items = TRACKER_ITEMS[96:]

class ItemWindow(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Inventory")
        self.resizable(False, False)

        # VERY IMPORTANT:
        # Keep references to PhotoImages alive.
        self.inventory = update_inventory(load_data())
        self.images = {}

        # -------------------------
        # OoT
        # -------------------------

        tk.Label(
            self,
            text="Items OoT",
            font=("Arial", 16, "bold")
        ).pack(pady=(10, 5))

        self.oot_frame = tk.Frame(self)
        self.oot_frame.pack(padx=10)

        self.create_grid(
            self.oot_frame,
            oot_items
        )

        # -------------------------
        # MM
        # -------------------------

        tk.Label(
            self,
            text="Items MM",
            font=("Arial", 16, "bold")
        ).pack(pady=(15, 5))

        self.mm_frame = tk.Frame(self)
        self.mm_frame.pack(padx=10, pady=(0, 10))

        self.create_grid(
            self.mm_frame,
            mm_items
        )

        self.refresh(self.inventory)

    def create_grid(self, parent, items):

        for index, item in enumerate(items):

            row = index // COLS
            col = index % COLS

            button = tk.Button(
                parent,
                image=self.get_image(item), #type: ignore
                width=32,
                height=32,
                relief=tk.FLAT,
                bd=0,
                highlightthickness=0,
                command=lambda item=item: self.item_clicked(item)
            )

            button.grid(
                row=row,
                column=col,
                padx=1,
                pady=1
            )
        pause = ""


    def get_image(self, item):
        filename = get_image_filename(item)
        path = IMAGE_DIR / filename

        if not path.exists():
            print(f"Missing image for {item}: {path}")
            return None

        image = tk.PhotoImage(file=path)

        self.images[(item, self.inventory[item])] = image

        return image
    def item_clicked(self, item):

        # Toggle inventory state
        self.inventory[item] = not self.inventory[item]

        print(item, self.inventory[item])

        # Update the button's image
        #self.refresh()


    def refresh(self, data):

        inventory = update_inventory(load_data())

        if data != inventory:
            # Rebuild the grids
            for widget in self.oot_frame.winfo_children():
                widget.destroy()

            for widget in self.mm_frame.winfo_children():
                widget.destroy()

            self.images.clear()

            self.create_grid(
                self.oot_frame,
                oot_items
            )

            self.create_grid(
                self.mm_frame,
                mm_items
            )

        self.after(1000, lambda: self.refresh(inventory))

def get_image_filename(item):
    inventory = update_inventory(load_data())
    value = inventory[item]

    # ============================================================
    # OOT - CONSUMABLES
    # ============================================================

    if item == "deku stick upgrade (oot)" or item == "deku stick upgrade (mm)":
        if value >= 30:
            return "triple-oot-icons/items/sticks30_32x32.png"
        elif value >= 20:
            return "sticks20_32x32.png"
        elif value >= 10:
            return "sticks10_32x32.png"
        return "triple-oot-icons/items/sticks-dim_32x32.png"

    if item == "deku nut upgrade (oot)" or item == "deku nut upgrade (mm)":
        if value >= 40:
            return "triple-oot-icons/items/nuts40_32x32.png"
        elif value >= 30:
            return "nuts30_32x32.png"
        elif value >= 20:
            return "nuts20_32x32.png"
        return "triple-oot-icons/items/nuts-dim_32x32.png"

    if item == "bomb bag (oot)":
        if value >= 40:
            return "triple-oot-icons/items/bombs40_32x32.png"
        elif value >= 30:
            return "triple-oot-icons/items/bombs30_32x32.png"
        elif value >= 20:
            return "triple-oot-icons/items/bombs20_32x32.png"
        elif value >= 10:
            return "bombs_32x32.png"
        return "triple-oot-icons/items/bombs-dim_32x32.png"

    if item == "fairy bow (oot)":
        if value >= 50:
            return "triple-oot-icons/items/bow50_32x32.png"
        elif value >= 40:
            return "triple-oot-icons/items/bow40_32x32.png"
        elif value >= 30:
            return "triple-oot-icons/items/bow30_32x32.png"
        elif value >= 20:
            return "bow_32x32.png"
        return "triple-oot-icons/items/bow-dim_32x32.png"

    if item == "fairy slingshot (oot)":
        if value >= 50:
            return "triple-oot-icons/items/slingshot50_32x32.png"
        elif value >= 40:
            return "slingshot40_32x32.png"
        elif value >= 30:
            return "slingshot30_32x32.png"
        return "triple-oot-icons/items/slingshot-dim_32x32.png"

    if item == "bombchu bag (oot)" or item == "bombchu bag (mm)": #TODO: Bombchu counter (for bags)
        if value > 0 :
            return "bomb-chu_32x32.png"
        return "triple-oot-icons/items/bomb-chu-dim_32x32.png"

    # ============================================================
    # OOT - PROGRESSIVE ITEMS
    # ============================================================

    # 0 = none, 1 = Fairy Ocarina, 2 = Ocarina of Time
    if item == "ocarina (oot)":
        if value >= 2:
            return "ocarina-of-time_32x32.png"
        elif value == 1:
            return "ocarina_32x32.png"
        return "triple-oot-icons/items/ocarina-dim_32x32.png"

    # 0 = none, 1 = Hookshot, 2 = Longshot
    if item == "hookshot (oot)":
        if value >= 2:
            return "triple-oot-icons/items/longshot_32x32.png"
        elif value == 1:
            return "triple-oot-icons/items/hookshot_32x32.png"
        return "triple-oot-icons/items/hookshot-dim_32x32.png"

    # 0 = none, 1 = Silver Scale, 2 = Golden Scale
    if item == "progressive scale (oot)":
        if value >= 2:
            return "golden-scale_32x32.png"
        elif value == 1:
            return "scale_32x32.png"
        return "triple-oot-icons/items/scale-dim_32x32.png"

    # 0 = none, 1 = normal magic, 2 = double magic
    if item == "magic upgrade (oot)" or item == "magic upgrade (mm)":
        if value >= 2:
            return "double-magic_32x32.png"
        elif value == 1:
            return "magic_32x32.png"
        return "triple-oot-icons/items/magic-dim_32x32.png"

    # 0 = none, 1 = Goron Bracelet, 2 = Silver Gauntlets,
    # 3 = Golden Gauntlets
    if item == "progressive strength (oot)":
        if value >= 3:
            return "strength3_32x32.png"
        elif value == 2:
            return "strength2_32x32.png"
        elif value == 1:
            return "strength_32x32.png"
        return "triple-oot-icons/items/strength-dim_32x32.png"

    # 0 = none, 1 = Adult Wallet, 2 = Giant's Wallet,
    # 3 = Tycoon/500 wallet
    if item == "progressive wallet (oot)" or item == "progressive wallet (mm)":
        if value >= 3:
            return "wallet999_32x32_500colors.png"
        elif value == 2:
            return "wallet500_32x32_200colors.png"
        elif value == 1:
            return "wallet200_32x32.png"
        return "wallet99_32x32.png"

    # ============================================================
    # OOT - BOOLEAN ITEMS
    # ============================================================

    if item == "fire arrows (oot)" or item == "fire arrows (mm)":
        if value:
            return "fire-arrows_32x32.png"
        return "triple-oot-icons/items/fire-arrows-dim_32x32.png"

    if item == "din's fire (oot)" or item == "din's fire (mm)":
        if value:
            return "dins-fire_32x32.png"
        return "triple-oot-icons/items/dins-fire-dim_32x32.png"

    if item == "farore's wind (oot)":
        if value:
            return "farores-wind_32x32.png"
        return "triple-oot-icons/items/farores-wind-dim_32x32.png"

    if item == "kokiri sword (oot)":
        if value:
            return "kokiri-sword_32x32.png"
        return "triple-oot-icons/items/kokiri-sword-dim_32x32.png"

    if item == "deku shield (oot)":
        if value:
            return "deku-shield_32x32.png"
        return "triple-oot-icons/items/deku-shield-dim_32x32.png"

    if item == "ice arrows (oot)" or item == "ice arrows (mm)":
        if value:
            return "ice-arrows_32x32.png"
        return "triple-oot-icons/items/ice-arrows-dim_32x32.png"

    if item == "master sword (oot)":
        if value:
            return "master-sword_32x32.png"
        return "triple-oot-icons/items/master-sword-dim_32x32.png"

    if item == "hylian shield (oot)":
        if value:
            return "hylian-shield_32x32.png"
        return "triple-oot-icons/items/hylian-shield-dim_32x32.png"

    if item == "boomerang (oot)":
        if value:
            return "boomerang_32x32.png"
        return "triple-oot-icons/items/boomerang-dim_32x32.png"

    if item == "lens of truth (oot)" or item == "lens of truth (mm)":
        if value:
            return "lens_32x32.png"
        return "triple-oot-icons/items/lens-dim_32x32.png"

    if item == "magic beans (oot)" or item == "magic bean (mm)":
        if value:
            return "beans_32x32.png"
        return "triple-oot-icons/items/beans-dim_32x32.png"

    if item == "megaton hammer (oot)":
        if value:
            return "hammer_32x32.png"
        return "triple-oot-icons/items/hammer-dim_32x32.png"

    if item == "light arrows (oot)" or item == "light arrows (mm)":
        if value:
            return "light-arrows_32x32.png"
        return "triple-oot-icons/items/light-arrows-dim_32x32.png"

    if item == "nayru's love (oot)":
        if value:
            return "nayrus-love_32x32.png"
        return "triple-oot-icons/items/nayrus-love-dim_32x32.png"

    if item == "biggoron's sword (oot)":
        if value:
            return "biggoron-sword_32x32.png"
        return "triple-oot-icons/items/biggoron-sword-dim_32x32.png"

    if item == "mirror shield (oot)":
        if value:
            return "mirror-shield_32x32.png"
        return "triple-oot-icons/items/mirror-shield-dim_32x32.png"

    # ============================================================
    # OOT - SONGS
    # ============================================================

    if item == "zelda's lullaby (oot)":
        if value:
            return "zeldas-lullaby_32x32.png"
        return "triple-oot-icons/songs/zeldas-lullaby-dim_32x32.png"

    if item == "epona's song (oot)":
        if value:
            return "epona_32x32.png"
        return "triple-oot-icons/songs/epona-dim_32x32.png"

    if item == "saria's song (oot)":
        if value:
            return "saria_32x32.png"
        return "triple-oot-icons/songs/saria-dim_32x32.png"

    if item == "sun's song (oot)":
        if value:
            return "suns-song_32x32.png"
        return "triple-oot-icons/songs/suns-song-dim_32x32.png"

    if item == "song of time (oot)":
        if value:
            return "song-of-time_32x32.png"
        return "triple-oot-icons/items/song-of-time-dim_32x32.png"

    if item == "song of storms (oot)":
        if value:
            return "song-of-storms_32x32.png"
        return "triple-oot-icons/songs/song-of-storms-dim_32x32.png"

    # ============================================================
    # OOT - BOOTS / TUNICS
    # ============================================================

    if item == "iron boots (oot)":
        if value:
            return "iron-boots_32x32.png"
        return "triple-oot-icons/items/iron-boots-dim_32x32.png"

    if item == "hover boots (oot)":
        if value:
            return "hover-boots_32x32.png"
        return "triple-oot-icons/items/hover-boots-dim_32x32.png"

    if item == "goron tunic (oot)":
        if value:
            return "goron-tunic_32x32.png"
        return "triple-oot-icons/items/goron-tunic-dim_32x32.png"

    if item == "zora tunic (oot)":
        if value:
            return "zora-tunic_32x32.png"
        return "triple-oot-icons/items/zora-tunic-dim_32x32.png"

    # ============================================================
    # OOT - ADULT WARP SONGS
    # ============================================================

    if item == "minuet of forest (oot)":
        if value:
            return "minuet_32x32.png"
        return "minuet-dim_32x32.png"

    if item == "bolero of fire (oot)":
        if value:
            return "bolero_32x32.png"
        return "bolero-dim_32x40.png"

    if item == "serenade of water (oot)":
        if value:
            return "serenade_32x32.png"
        return "serenade-dim_32x32.png"

    if item == "requiem of spirit (oot)":
        if value:
            return "requiem_32x32.png"
        return "requiem-dim_32x32.png"

    if item == "nocturne of shadow (oot)":
        if value:
            return "nocturne_32x32.png"
        return "nocturne-dim_32x32.png"

    if item == "prelude of light (oot)":
        if value:
            return "prelude_32x32.png"
        return "prelude-dim_32x32.png"

    # ============================================================
    # OOT - BOTTLES
    # ============================================================

    if item == "ruto's letter (oot)":
        if value:
            return "bottle-rutos-letter_32x32.png"
        return "triple-oot-icons/items/bottle-rutos-letter-dim_32x32.png"

    if item == "empty bottle (oot) 2" or item == "empty bottle (mm) 2":
        if value:
            return "bottle-empty_32x32.png"
        return "triple-oot-icons/items/bottle-empty-dim_32x32.png"
    
    if item == "empty bottle (oot) 3"or item == "empty bottle (mm) 3":
            if value:
                return "bottle-empty_32x32.png"
            return "triple-oot-icons/items/bottle-empty-dim_32x32.png"
    
    if item == "empty bottle (oot) 4"or item == "empty bottle (mm) 4":
            if value:
                return "bottle-empty_32x32.png"
            return "triple-oot-icons/items/bottle-empty-dim_32x32.png"
    if item == "empty bottle (mm) 5":
        if value:
            return "bottle-empty_32x32.png"
        return "triple-oot-icons/items/bottle-empty-dim_32x32.png"
    if item == "empty bottle (mm) 6":
        if value:
            return "bottle-empty_32x32.png"
        return "triple-oot-icons/items/bottle-empty-dim_32x32.png"


    # ============================================================
    # OOT - OTHER EQUIPMENT / TRADING
    # ============================================================

    if item == "stone of agony (oot)":
        if value:
            return "stone-of-agony_32x32.png"
        return "triple-oot-icons/items/stone-of-agony-dim_32x32.png"

    if item == "gerudo's membership card (oot)":
        if value:
            return "gerudo-card_32x32.png"
        return "triple-oot-icons/items/gerudo-card-dim_32x32.png"

    if item == "pocket egg (oot)":
        if value:
            return "egg_32x32.png"
        return "triple-oot-icons/items/egg-dim_32x32.png"

    if item == "zelda's letter (oot)":
        if value:
            return "zeldas-letter_32x32.png"
        return "triple-oot-icons/items/zeldas-letter-dim_32x32.png"

    if item == "keaton mask (oot)" or item == "keaton mask (mm)":
        if value:
            return "keaton-mask_32x32.png"
        return "Keaton-dim.png"

    if item == "skull mask (oot)":
        if value:
            return "skull-mask2_32x32.png"
        return "skull-mask2-dim_32x32.png"

    if item == "spooky mask (oot)":
        if value:
            return "spooky-mask_32x32.png"
        return "spooky-mask-dim_32x32.png"

    if item == "bunny hood (oot)" or item == "bunny hood (mm)":
        if value:
            return "bunny-hood_32x32.png"
        return "Bunny-dim.png"

    if item == "mask of truth (oot)" or item == "mask of truth (mm)":
        if value:
            return "mask-of-truth_32x32.png"
        return "mask-of-truth-dim_32x32.png"

    if item == "pocket cucco (oot)":
        if value:
            return "chicken_32x32.png"
        return "chicken-dim_32x32.png"

    if item == "cojiro (oot)":
        if value:
            return "blue-chicken_32x32.png"
        return "blue-chicken-dim_32x32.png"

    if item == "odd mushroom (oot)":
        if value:
            return "mushroom_32x32.png"
        return "mushroom-dim_32x32.png"

    if item == "odd potion (oot)":
        if value:
            return "odd-potion_32x32.png"
        return "odd-potion-dim_32x32.png"

    if item == "poacher's saw (oot)":
        if value:
            return "saw_32x32.png"
        return "saw-dim_32x32.png"

    if item == "broken goron's sword (oot)":
        if value:
            return "broken-bgs_32x32.png"
        return "triple-oot-icons/items/broken-bgs-dim_32x32.png"

    if item == "prescription (oot)":
        if value:
            return "prescription_32x32.png"
        return "triple-oot-icons/items/prescription-dim_32x32.png"

    if item == "eyeball frog (oot)":
        if value:
            return "kz-frog_32x32.png"
        return "kz-frog-dim_32x32.png"

    if item == "eye drops (oot)":
        if value:
            return "eye-drops_32x32.png"
        return "eye-drops-dim_32x32.png"

    if item == "claim check (oot)":
        if value:
            return "claim-check_32x32.png"
        return "triple-oot-icons/items/claim-check-dim_32x32.png"

    # ============================================================
    # OOT - MEDALLIONS
    # ============================================================

    if item == "kokiri's emerald (oot)":
        if value:
            return "triple-oot-icons/stones/emerald_32x32.png"
        return "triple-oot-icons/stones/emerald-dim_32x32.png"
    
    if item == "goron's ruby (oot)":
            if value:
                return "triple-oot-icons/stones/ruby_32x32.png"
            return "triple-oot-icons/stones/ruby-dim_32x32.png"

    if item == "zora's sapphire (oot)":
        if value:
            return "triple-oot-icons/stones/sapphire_32x32.png"
        return "triple-oot-icons/stones/sapphire-dim_32x32.png"

    if item == "forest medallion (oot)":
        if value:
            return "triple-oot-icons/medallions/forestmedallion_32x32.png"
        return "triple-oot-icons/medallions/forestmedallion-dim_32x32.png"

    if item == "fire medallion (oot)":
        if value:
            return "triple-oot-icons/medallions/firemedallion_32x32.png"
        return "triple-oot-icons/medallions/firemedallion-dim_32x32.png"

    if item == "water medallion (oot)":
        if value:
            return "triple-oot-icons/medallions/watermedallion_32x32.png"
        return "triple-oot-icons/medallions/watermedallion-dim_32x32.png"

    if item == "spirit medallion (oot)":
        if value:
            return "triple-oot-icons/medallions/spiritmedallion_32x32.png"
        return "triple-oot-icons/medallions/spiritmedallion-dim_32x32.png"

    if item == "shadow medallion (oot)":
        if value:
            return "triple-oot-icons/medallions/shadowmedallion_32x32.png"
        return "triple-oot-icons/medallions/shadowmedallion-dim_32x32.png"

    if item == "light medallion (oot)":
        if value:
            return "triple-oot-icons/medallions/lightmedallion_32x32.png"
        return "triple-oot-icons/medallions/lightmedallion-dim_32x32.png"

    # ============================================================
    # OOT - SKULLTULA COUNTER
    # ============================================================

    if item == "gold skulltula tokens (oot)":
        if value == 100:
            return "triple-oot-icons/skulltula/skull_green_100.png"
        if value > 0:
            return f"triple-oot-icons/skulltula/skull_white_{value}.png"
        return "triple-oot-icons/skulltula/gold-skulltula-token-dim_32x32.png"

    # ============================================================
    # OOT - SMALL KEYS
    # ============================================================

    if item == "small key (forest temple) (oot)":
        if value >= 5:
            return f"triple-oot-icons/keys/key_green_5.png"
        if value > 0:
            return f"triple-oot-icons/keys/key_white_{value}.png"
        return "triple-oot-icons/keys/forest-temple-key-dim_32x32.png"

    if item == "small key (fire temple) (oot)":
        if value >= 7:
            return f"triple-oot-icons/keys/key_green_5.png"
        if value > 0:
            return f"triple-oot-icons/keys/key_white_{value}.png"
        return "triple-oot-icons/keys/fire-temple-key-dim_32x32.png"

    if item == "small key (water temple) (oot)":
        if value >= 5:
            return f"triple-oot-icons/keys/key_green_5.png"
        if value > 0:
            return f"triple-oot-icons/keys/key_white_{value}.png"
        return "triple-oot-icons/keys/water-temple-key-dim_32x32.png"

    if item == "small key (spirit temple) (oot)":
        if value >= 5:
            return f"triple-oot-icons/keys/key_green_5.png"
        if value > 0:
            return f"triple-oot-icons/keys/key_white_{value}.png"
        return "triple-oot-icons/keys/spirit-temple-key-dim_32x32.png"

    if item == "small key (shadow temple) (oot)":
        if value >= 5:
            return f"triple-oot-icons/keys/key_green_5.png"
        if value > 0:
            return f"triple-oot-icons/keys/key_white_{value}.png"
        return "triple-oot-icons/keys/shadow-temple-key-dim_32x32.png"

    if item == "small key (ganon's castle) (oot)":
        if value >= 2:
            return f"triple-oot-icons/keys/key_green_5.png"
        if value > 0:
            return f"triple-oot-icons/keys/key_white_{value}.png"
        return "triple-oot-icons/keys/ganon-key-dim_32x32.png"

    if item == "small key (gerudo's training ground) (oot)":
        if value >= 9:
            return f"triple-oot-icons/keys/key_green_5.png"
        if value > 0:
            return f"triple-oot-icons/keys/key_white_{value}.png"
        return "triple-oot-icons/keys/gtg-key-dim_32x32.png"

    if item == "small key (bottom of the well) (oot)":
        if value >= 3:
            return f"triple-oot-icons/keys/key_green_5.png"
        if value > 0:
            return f"triple-oot-icons/keys/key_white_{value}.png"
        return "triple-oot-icons/keys/botw-key-dim_32x32.png"

    # ============================================================
    # OOT - BOSS KEYS
    # ============================================================

    if item == "boss key (forest temple) (oot)":
        if value:
            return "bk_32x32.png"
        return "bk-dim_32x32.png"

    if item == "boss key (fire temple) (oot)":
        if value:
            return "bk_32x32.png"
        return "bk-dim_32x32.png"

    if item == "boss key (water temple) (oot)":
        if value:
            return "bk_32x32.png"
        return "bk-dim_32x32.png"

    if item == "boss key (spirit temple) (oot)":
        if value:
            return "bk_32x32.png"
        return "bk-dim_32x32.png"

    if item == "boss key (shadow temple) (oot)":
        if value:
            return "bk_32x32.png"
        return "bk-dim_32x32.png"

    if item == "key ring (hideout) (oot)":
        if value:
            return "triple-oot-icons/keys/key_green_4.png"
        return "triple-oot-icons/keys/thieves-hideout-key-dim_32x32.png"

    # ============================================================
    # MM - PROGRESSIVE ITEMS
    # ============================================================

    # 0 = none, 1 = Fairy Ocarina, 2 = Ocarina of Time
    if item == "ocarina (mm)":
        if value >= 2:
            return "ocarina-of-time_32x32.png"
        elif value == 1:
            return "ocarina_32x32.png"
        return "triple-oot-icons/items/ocarina-dim_32x32.png"

    if item == "hero's bow (mm)":
        if value >= 50:
            return "mm/Bow3.png"
        elif value >= 40:
            return "mm/Bow2.png"
        elif value >= 30:
            return "mm/Bow1.png"
        return "mm/Bow0-dim.png"

    # 0 = Kokiri, 1 = Razor, 2 = Gilded
    if item == "progressive sword (mm)":
        if value >= 3:
            return "mm/Sword3.png"
        elif value == 2:
            return "mm/Sword2.png"
        elif value == 1:
            return "mm/Sword1.png"
        return "mm/Sword0-dim.png"

    if item == "hookshot (mm)":
        if value:
            return "mm/Hookshot.png"
        return "mm/Hookshot-dim.png"

    # ============================================================
    # MM - ARROWS / SHIELDS
    # ============================================================

    if item == "fire arrows (mm)":
        if value:
            return "fire-arrows_32x32.png"
        return "triple-oot-icons/items/fire-arrows-dim_32x32.png"

    if item == "ice arrows (mm)":
        if value:
            return "mm/Ice.png"
        return "mm/blank.png"

    if item == "light arrows (mm)":
        if value:
            return "mm/Light.png"
        return "mm/blank.png"

    if item == "hero's shield (mm)":
        if value:
            return "mm/shield1.png"
        return "mm/shield0-dim.png"

    if item == "mirror shield (mm)":
        if value:
            return "mm/shield2.png"
        return "mm/shield2-dim.png"

    # ============================================================
    # MM - CONSUMABLES
    # ============================================================

    if item == "bomb bag (mm)":
        if value >= 40:
            return "triple-oot-icons/items/bombs40_32x32.png"
        elif value >= 30:
            return "triple-oot-icons/items/bombs30_32x32.png"
        elif value >= 20:
            return "triple-oot-icons/items/bombs20_32x32.png"
        elif value >= 10:
            return "bombs_32x32.png"
        return "triple-oot-icons/items/bombs-dim_32x32.png"

    if item == "deku sticks (mm)":
        if value:
            return "mm/stick.png"
        return "mm/blank.png"

    if item == "deku nuts (mm)":
        if value:
            return "mm/nut.png"
        return "mm/blank.png"

    if item == "magic beans (mm)":
        if value:
            return "mm/Beans.png"
        return "mm/blank.png"

    if item == "bottle of gold dust (mm)":
        if value:
            return "mm/GoldDust.png"
        return "mm/GoldDust-dim.png"

    if item == "powder keg (mm)":
        if value:
            return "mm/PowderKeg.png"
        return "mm/PowderKeg-dim.png"

    if item == "pictograph box (mm)":
        if value:
            return "mm/Pictobox.png"
        return "mm/Pictobox-dim.png"


    if item == "great fairy's sword (mm)":
        if value:
            return "mm/GFsword.png"
        return "mm/GFsword-dim.png"

    # ============================================================
    # MM - MAGIC / UPGRADES
    # ============================================================


    if item == "progressive wallet (mm)":
        if value >= 2:
            return "mm/Wallet2.png"
        elif value == 1:
            return "mm/Wallet1.png"
        return "mm/Wallet0.png"



    # ============================================================
    # MM - SONGS
    # ============================================================

    if item == "song of time (mm)":
        if value:
            return "mm/SongofTime.png"
        return "mm/SongofTime-dim.png"

    if item == "song of healing (mm)":
        if value:
            return "mm/Healing.png"
        return "mm/Healing-dim.png"

    if item == "epona's song (mm)":
        if value:
            return "mm/EponasSong.png"
        return "mm/EponasSong-dim.png"

    if item == "song of soaring (mm)":
        if value:
            return "mm/Soaring.png"
        return "mm/Soaring-dim.png"

    if item == "song of storms (mm)":
        if value:
            return "mm/SongofStorms.png"
        return "mm/SongofStorms-dim.png"

    if item == "sonata of awakening (mm)":
        if value:
            return "mm/Sonata.png"
        return "mm/Sonata-dim.png"

    if item == "progressive goron lullaby (mm)":
        if value >= 2:
            return "mm/Lullaby.png"
        if value >= 1:
            return "mm/Lullaby-dim.png"
        return "mm/Lullaby-dim.png"

    if item == "new wave bossa nova (mm)":
        if value:
            return "mm/NewWave.png"
        return "mm/NewWave-dim.png"

    if item == "elegy of emptiness (mm)":
        if value:
            return "mm/Elegy.png"
        return "mm/Elegy-dim.png"

    if item == "oath to order (mm)":
        if value:
            return "mm/Oath.png"
        return "mm/Oath-dim.png"

    # ============================================================
    # MM - STRAY FAIRIES
    # ============================================================

    if item == "stray fairy (clock town) (mm)":
        if value > 0:
            return "mm/clock_town_stray_fairy.png"
        return "mm/clock_town_stray_fairy_dim.png"

    if item == "stray fairy (woodfall temple) (mm)":
        if value > 0:
            return f"mm/fairy_skull_counter/fairy_counters/woodfall_stray_fairy_{value}.png"
        return "mm/woodfall_stray_fairy_dim.png"

    if item == "stray fairy (snowhead temple) (mm)":
        if value > 0:
            return f"mm/fairy_skull_counter/fairy_counters/snowhead_stray_fairy_{value}.png"
        return "mm/snowhead_stray_fairy_dim.png"

    if item == "stray fairy (great bay temple) (mm)":
        if value > 0:
            return f"mm/fairy_skull_counter/fairy_counters/greatbay_stray_fairy_{value}.png"
        return "mm/greatbay_stray_fairy_dim.png"

    if item == "stray fairy (stone tower temple) (mm)":
        if value > 0:
            return f"mm/fairy_skull_counter/fairy_counters/stonetower_stray_fairy_{value}.png"
        return "mm/stonetower_stray_fairy_dim.png"

    # ============================================================
    # MM - SKULLTULA TOKENS
    # ============================================================

    if item == "swamp skulltula token (mm)":
        if value > 0:
            return f"mm/fairy_skull_counter/skulltulla_counters/skulltulla_woodfall_{value}.png"
        return "mm/skulltulla_woodfall_dim.png"

    if item == "ocean skulltula token (mm)":
        if value > 0:
            return f"mm/fairy_skull_counter/skulltulla_counters/skulltulla_greatbay_{value}.png"
        return "mm/skulltulla_greatbay_dim.png"

    # ============================================================
    # MM - SMALL KEYS
    # ============================================================

    if item == "small key (woodfall temple) (mm)":
        if value >= 1:
            return f"triple-oot-icons/keys/key_green_1.png"
        return "triple-oot-icons/keys/forest-temple-key-dim_32x32.png"

    if item == "small key (snowhead temple) (mm)":
        if value >= 3:
            return f"triple-oot-icons/keys/key_green_3.png"
        if value > 0:
            return f"triple-oot-icons/keys/key_white_{value}.png"
        return "triple-oot-icons/keys/fire-temple-key-dim_32x32.png"

    if item == "small key (great bay temple) (mm)":
        if value >= 1:
            return f"triple-oot-icons/keys/key_green_1.png"
        return "triple-oot-icons/keys/water-temple-key-dim_32x32.png"

    if item == "small key (stone tower temple) (mm)":
        if value >= 4:
            return f"triple-oot-icons/keys/key_green_4.png"
        if value > 0:
            return f"triple-oot-icons/keys/key_white_{value}.png"
        return "triple-oot-icons/keys/spirit-temple-key-dim_32x32.png"

    # ============================================================
    # MM - BOSS KEYS
    # ============================================================

    if item == "boss key (woodfall temple) (mm)":
        if value:
            return "bk_32x32.png"
        return "bk-dim_32x32.png"

    if item == "boss key (snowhead temple) (mm)":
        if value:
            return "bk_32x32.png"
        return "bk-dim_32x32.png"

    if item == "boss key (great bay temple) (mm)":
        if value:
            return "bk_32x32.png"
        return "bk-dim_32x32.png"

    if item == "boss key (stone tower temple) (mm)":
        if value:
            return "bk_32x32.png"
        return "bk-dim_32x32.png"

    # ============================================================
    # MM - REMAINS
    # ============================================================

    if item == "odolwa's remains (mm)":
        if value:
            return "mm/Odolwa.png"
        return "mm/Odolwa-dim.png"

    if item == "goht's remains (mm)":
        if value:
            return "mm/Goht.png"
        return "mm/Goht-dim.png"

    if item == "gyorg's remains (mm)":
        if value:
            return "mm/Gyorg.png"
        return "mm/Gyorg-dim.png"

    if item == "twinmold's remains (mm)":
        if value:
            return "mm/Twinmold.png"
        return "mm/Twinmold-dim.png"

    # ============================================================
    # MM - STORY / TRADING ITEMS
    # ============================================================

    if item == "moon's tear (mm)":
        if value:
            return "mm/Moonstear.png"
        return "mm/Moonstear-dim.png"

    if item == "pendant of memories (mm)":
        if value:
            return "mm/Pendant.png"
        return "mm/Pendant-dim.png"

    if item == "letter to kafei (mm)":
        if value:
            return "mm/Letter.png"
        return "mm/Letter-dim.png"

    if item == "letter to mama (mm)":
        if value:
            return "mm/ExpressMail.png"
        return "mm/ExpressMail-dim.png"

    if item == "land title deed (mm)":
        if value:
            return "mm/LandDeed.png"
        return "mm/LandDeed-dim.png"

    if item == "swamp title deed (mm)":
        if value:
            return "mm/SwampDeed.png"
        return "mm/SwampDeed-dim.png"

    if item == "mountain title deed (mm)":
        if value:
            return "mm/MountainDeed.png"
        return "mm/MountainDeed-dim.png"

    if item == "ocean title deed (mm)":
        if value:
            return "mm/OceanDeed.png"
        return "mm/OceanDeed-dim.png"

    if item == "room key (mm)":
        if value:
            return "mm/Roomkey.png"
        return "mm/Roomkey-dim.png"

    # ============================================================
    # MM - MASKS
    # ============================================================

    if item == "deku mask (mm)":
        if value:
            return "mm/Deku.png"
        return "mm/Deku-dim.png"

    if item == "goron mask (mm)":
        if value:
            return "mm/Goron.png"
        return "mm/Goron-dim.png"

    if item == "zora mask (mm)":
        if value:
            return "mm/Zora.png"
        return "mm/Zora-dim.png"

    if item == "fierce deity's mask (mm)":
        if value:
            return "mm/FD.png"
        return "mm/FD-dim.png"

    if item == "great fairy's mask (mm)":
        if value:
            return "mm/GFMask.png"
        return "mm/GFMask-dim.png"

    if item == "bunny hood (mm)":
        if value:
            return "mm/Bunny.png"
        return "mm/blank.png"

    if item == "blast mask (mm)":
        if value:
            return "mm/Blast.png"
        return "mm/Blast-dim.png"

    if item == "stone mask (mm)":
        if value:
            return "mm/Stone.png"
        return "mm/Stone-dim.png"

    if item == "bremen mask (mm)":
        if value:
            return "mm/Bremen.png"
        return "mm/Bremen-dim.png"

    if item == "don gero's mask (mm)":
        if value:
            return "mm/DonGero.png"
        return "mm/DonGero-dim.png"

    if item == "mask of scents (mm)":
        if value:
            return "mm/Scents.png"
        return "mm/Scents-dim.png"

    if item == "captain's hat (mm)":
        if value:
            return "mm/Captain.png"
        return "mm/Captain-dim.png"

    if item == "garo's mask (mm)":
        if value:
            return "mm/Garo.png"
        return "mm/Garo-dim.png"

    if item == "gibdo mask (mm)":
        if value:
            return "mm/Gibdo.png"
        return "mm/Gibdo-dim.png"

    if item == "romani's mask (mm)":
        if value:
            return "mm/Romani.png"
        return "mm/Romani-dim.png"

    if item == "couple's mask (mm)":
        if value:
            return "mm/Couple.png"
        return "mm/Couple-dim.png"

    if item == "kamaro's mask (mm)":
        if value:
            return "mm/Kamaro.png"
        return "mm/Kamaro-dim.png"

    if item == "postman's hat (mm)":
        if value:
            return "mm/Postman.png"
        return "mm/Postman-dim.png"

    if item == "all-night mask (mm)":
        if value:
            return "mm/Allnight.png"
        return "mm/Allnight-dim.png"

    if item == "circus leader's mask (mm)":
        if value:
            return "mm/Circus.png"
        return "mm/Circus-dim.png"

    if item == "kafei's mask (mm)":
        if value:
            return "mm/Kafei.png"
        return "mm/Kafei-dim.png"

    if item == "giant's mask (mm)":
        if value:
            return "mm/Giant.png"
        return "mm/Giant_dim.png"

    # ============================================================
    # FALLBACK
    # ============================================================

    return "mm/blank.png"


if __name__=="__main__":
    app = ItemWindow()
    app.mainloop()