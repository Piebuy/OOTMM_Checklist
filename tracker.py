import tkinter as tk
from pathlib import Path


COLS = 8
ROWS = 11

IMAGE_DIR = Path("img")


inventory = {
    "deku sticks (oot)": 20,
    "deku nuts (oot)": 30
}


# The order in which items appear in the grid
oot_items = [
    "deku sticks (oot)",
    "deku nuts (oot)",
    #"bombs (oot)",
    #"fairy bow (oot)",
    #"fire arrows (oot)",
    #"din's fire (oot)",
    #"kokiri sword (oot)",
    #"deku shield (oot)",
    #"boomerang (oot)",
]

mm_items = [

]

images = {
    "deku sticks (oot)":("",""),
    "deku nuts (oot)":("",""),
    "bombs (oot)":("",""),
    "fairy bow (oot)":("",""),
    "fire arrows (oot)":("",""),
    "din's fire (oot)":("",""),
    "kokiri sword (oot)":("",""),
    "deku shield (oot)":("",""),
    "boomerang (oot)": (
        "boomerang-dim_32x32.png",
        "boomerang_32x32.png"

    )
}

class ItemWindow(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Inventory")
        self.resizable(False, False)

        # VERY IMPORTANT:
        # Keep references to PhotoImages alive.
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

    def create_grid(self, parent, items):

        for index, item in enumerate(items):

            row = index // COLS
            col = index % COLS

            button = tk.Button(
                parent,
                image=self.get_image(item),
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


    def get_image(self, item):

        filename = get_image_filename(item)

        path = IMAGE_DIR / filename

        image = tk.PhotoImage(file=path)

        self.images[(item, inventory[item])] = image

        return image

    def item_clicked(self, item):

        # Toggle inventory state
        inventory[item] = not inventory[item]

        print(item, inventory[item])

        # Update the button's image
        self.refresh()


    def refresh(self):

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

def get_image_filename(item):
    value = inventory[item]

    if item == "deku sticks (oot)" or item == "deku sticks (mm)":
        if value == 10:
            return "sticks10_32x32.png"
        elif value == 20:
            return "sticks20_32x32.png"
        elif value == 30:
            return "/triple-oot-icons/items/sticks30_32x32.png"
        else:
            return "sticks-dim_32x32.png"
        
    if item == "deku nuts (oot)" or item =="deku nuts (mm)":
        if value == 20:
            return "nuts20_32x32.png"
        if value == 30:
            return "nuts30_32x32.png"
        if value == 40:
            return "/triple-oot-icons/items/nuts40_32x32.png"
        else:
            return "nuts-dim_32x32.png"


    # Default
    return "empty.png"

if __name__ == "__main__":
    app = ItemWindow()
    app.mainloop()