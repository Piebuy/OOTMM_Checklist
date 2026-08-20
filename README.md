# OOTMM Checklist

Discalimer: This README file is 100% AI generated based on the repository

A local checklist and tracker for **OoTMM (Ocarina of Time / Majora's Mask)** randomizer runs.

The application reads the current game and scene from an emulator connection, matches that scene against the known OoT/MM scene tables, and displays the relevant spoiler-log checks in the current location of the player in a web interface. Checks can be marked complete and are persisted locally so progress survives restarts.

## Features

* **Automatic location tracking** — receives scene information from the emulator and determines the player's current location.
* **OoT and MM support** — includes scene mappings for both *Ocarina of Time* and *Majora's Mask*.
* **Spoiler-log based checklist** — creates a checklist from a spoiler log and associates each location with its randomized item.
* **Current-location view** — shows the checks relevant to the player's current scene.
* **All-locations view** — view the complete checklist across all scenes.
* **Progress tracking** — displays both current-location and overall completion percentages.
* **Hide checked locations** — optionally hide completed checks.
* **Persistent progress** — checklist state is saved to `locations.json`.
* **Automatic backups** — changes are also written to `backup/locations.json`.
* **Local web interface** — Flask serves the tracker UI on `127.0.0.1:5001`.

## How It Works

The application consists of two cooperating processes:

```text
                    ┌─────────────────────┐
                    │      Emulator       │
                    │                     │
                    │  Game / Scene data  │
                    └──────────┬──────────┘
                               │
                         TCP :5000
                               │
                               ▼
                    ┌─────────────────────┐
                    │      main.py        │
                    │                     │
                    │ Parse emulator data │
                    │ Match scene         │
                    │ Update current      │
                    └──────────┬──────────┘
                               │
                         JSON files
                               │
                               ▼
                    ┌─────────────────────┐
                    │     services.py     │
                    │                     │
                    │ Checklist state     │
                    │ Scene state         │
                    │ Spoiler processing  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │       app.py        │
                    │                     │
                    │     Flask API       │
                    │                     │
                    │       :5001         │
                    └──────────┬──────────┘
                               │
                         HTTP / JSON
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Web Checklist     │
                    │ templates/index.html│
                    └─────────────────────┘
```

`main.py` listens for emulator data on `127.0.0.1:5000`. Incoming messages are parsed into key/value pairs and dispatched through the handler table in `handlers.py`. The current scene is then saved to `current_scene.json`, which the Flask application uses to determine what should be displayed.

The web application runs independently on `127.0.0.1:5001`. Its frontend polls the current-location API once per second so that the checklist follows the player's movement through the game.

## Requirements

The project is written primarily in Python and uses Flask for the web server.

The repository currently pins its Python dependencies in `requirements.txt`, including:

* Flask 3.1.3

See `requirements.txt` for the complete pinned dependency set.

A working Python installation and a local emulator capable of providing the expected TCP scene data are required.

## Installation

Clone the repository:

```bash
git clone https://github.com/Piebuy/OOTMM_Checklist.git
cd OOTMM_Checklist
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bat
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Spoiler Log Setup

Place your spoiler log in the repository's main directory and name it:

```text
spoiler_file.txt
```

When a checklist does not already exist, the application processes this file and creates the checklist data used by the tracker.

The spoiler processing code looks for the **Location List** section, removes irrelevant blank lines, normalizes location headers, and extracts location/item pairs. The resulting data is converted into the application's JSON checklist format.

The generated checklist is stored as:

```text
locations.json
```

The repository intentionally ignores generated `.json` and `.txt` files, so spoiler logs and save data should remain local.

## Running the Tracker

### Windows

After creating the virtual environment and installing dependencies, the included batch file can start both processes:

```bat
start servers only.bat
```

This activates `.venv` and opens separate command windows for:

* the Flask web application
* the emulator TCP listener

The supplied startup script runs `python app.py` and `python main.py`.

### Start Manually

The Flask application can be started with:

```bash
python app.py
```

It listens on:

```text
http://127.0.0.1:5001
```

The emulator listener can be started separately with:

```bash
python main.py
```

It listens for the emulator connection on:

```text
127.0.0.1:5000
```

## Web Interface

Once the Flask server is running, open:

```text
http://127.0.0.1:5001
```

The interface provides two primary views.

### Current Location

The default view displays the checks associated with the scene currently reported by the emulator.

The UI shows:

* current scene
* checks for that scene
* completed/total count
* current completion percentage
* overall completion percentage
* randomized item information for completed checks

The browser polls `/api/current` every second to detect location changes.

### All Locations

The **Show All** view displays every checklist location grouped by scene.

The `/api/all` endpoint returns the scene, location, item, and checked state for every checklist entry.

### Hiding Completed Checks

The interface can hide completed locations, making it easier to focus on remaining checks.

## API

The Flask application exposes the following endpoints.

| Endpoint       | Method | Purpose                                          |
| -------------- | ------ | ------------------------------------------------ |
| `/`            | GET    | Serves the checklist web page                    |
| `/api/current` | GET    | Returns the current scene and its checklist data |
| `/api/check`   | POST   | Marks an individual location checked/unchecked   |
| `/api/all`     | GET    | Returns all checklist locations                  |
| `/api/reset`   | POST   | Recreates the checklist data                     |

### `GET /api/current`

Returns information about the current scene, including its locations and completion counts.

It also returns global completion information:

```json
{
  "current_key": "Current Scene",
  "locations": [],
  "checked_locations": 0,
  "total_locations": 0,
  "all_checked": 0,
  "all_total": 0
}
```

### `POST /api/check`

Updates a checklist entry.

Example request:

```json
{
  "scene": "South Clock Town",
  "location": "Example Location",
  "checked": true
}
```

The server validates the scene, location, and boolean `checked` value before saving the updated checklist.

### `GET /api/all`

Returns every checklist location in a flattened format:

```json
{
  "locations": [
    {
      "scene": "South Clock Town",
      "location": "Example Location",
      "checked": false,
      "item": "Example Item"
    }
  ]
}
```

### `POST /api/reset`

Rebuilds the checklist from the spoiler data.

**Warning:** resetting should be treated as a destructive operation for the current checklist state.

## Data Files

The application uses three important local JSON files:

```text
locations.json
backup/
└── locations.json

current_scene.json
```

### `locations.json`

The main checklist save file.

It contains scene information, individual locations, randomized items, and checked state.

### `backup/locations.json`

A backup copy of the checklist written when checklist progress is saved.

This provides a recovery point if the main save file is accidentally damaged or overwritten.

### `current_scene.json`

Stores the most recently detected scene so the Flask application knows which location to display.

These generated files are ignored by Git.

## Project Structure

```text
OOTMM_Checklist/
│
├── app.py
├── main.py
├── handlers.py
├── services.py
├── globals.py
├── requirements.txt
├── start servers only.bat
├── .gitignore
│
└── templates/
    └── index.html
```

### `main.py`

The emulator-facing process.

Responsibilities:

* open the TCP server on port `5000`
* accept the emulator connection
* parse incoming messages
* dispatch messages to handlers
* maintain the current scene

### `app.py`

The Flask web server.

Responsibilities:

* serve the web interface
* expose the checklist API
* read and update checklist data
* calculate completion statistics
* reset the checklist

### `handlers.py`

Maps incoming emulator events to processing functions.

Currently the `scene_changed` event is handled by `get_scene_change` in `services.py`.

### `services.py`

Contains the core application logic.

Responsibilities include:

* translating emulator scene IDs
* matching emulator scenes against checklist scenes
* parsing spoiler logs
* converting spoiler data into checklist dictionaries
* loading/saving checklist data
* saving/loading the current scene
* normalizing mismatched scene names

### `globals.py`

Contains application constants and the scene lookup tables for both games.

The OoT table maps emulator scene IDs to locations such as Hyrule Field, Kokiri Forest, temples, shops, houses, and dungeons. The MM table provides equivalent mappings for Majora's Mask locations.

### `templates/index.html`

Contains the complete browser UI, including:

* HTML
* CSS
* JavaScript
* checklist rendering
* progress counters
* current/all location switching
* checked-location filtering
* API communication

## Emulator Data

`main.py` expects messages in a pipe-delimited format.

The first field identifies the event, while subsequent fields are parsed as key/value pairs.

Conceptually:

```text
scene_changed|game=mm|scene=0x006c|previousScene=0x006d
```

The handler receives the parsed values and uses the appropriate scene dictionary depending on whether the game is OoT or MM.

For a `scene_changed` event, the application:

1. Determines the game.
2. Selects the OoT or MM scene table.
3. Converts the emulator scene ID into a readable location.
4. Normalizes the location name.
5. Checks whether that location exists in the spoiler-derived checklist.
6. Updates the current scene.
7. Saves the current scene for the Flask frontend.

## Location Name Normalization

The emulator scene names and spoiler-log names do not always match exactly.

`services.py` contains normalization rules for cases such as:

* Market
* Kakariko Village
* Ganon's Castle
* Ganon's Castle Tower
* Southern Swamp variants
* Deku Tree
* Inverted Stone Tower Temple
* seasonal Mountain Village locations
* Snowhead paths
* Goron Village paths

This allows emulator scene names to resolve to the corresponding spoiler-log scene.

## Resetting the Checklist

The application provides a reset endpoint:

```text
POST /api/reset
```

This calls `create_check_dict()`, which processes `spoiler_file.txt` and regenerates `locations.json`.

If you want to preserve an existing run, make a copy of your `locations.json` before resetting.

## Troubleshooting

### The web page loads but the current location never changes

Make sure `main.py` is running and that the emulator is connecting to:

```text
127.0.0.1:5000
```

The Flask server and emulator listener are separate processes.

### The current location is blank or incorrect

The reported emulator scene must exist in the corresponding scene dictionary and, after normalization, must match a scene present in the generated checklist.

Check:

* the selected game value
* the emulator scene ID
* `globals.py`
* the spoiler log's location names
* the normalization rules in `services.py`

### The checklist does not exist

Place the spoiler log in the project root as:

```text
spoiler_file.txt
```

Then allow the application to generate the checklist data.

### Progress disappeared

Check whether `locations.json` exists.

A backup is normally maintained at:

```text
backup/locations.json
```

## Development Notes

The project currently has no automated test suite or CI workflow visible in the repository. The GitHub repository currently contains four commits and exposes no configured GitHub Actions workflow in its tracked file tree.

The architecture is intentionally simple:

* TCP socket for emulator input
* Python dictionaries for in-memory state
* JSON for persistence
* Flask for the local API
* HTML/CSS/JavaScript for the UI

This makes the project straightforward to modify, but also means that the application currently relies on local files and a single emulator connection rather than a database or multi-user architecture.

## License

No license file is currently present in the repository. If this project is intended for public redistribution, consider adding an appropriate open-source license.

## Repository

**GitHub:**
https://github.com/Piebuy/OOTMM_Checklist

## Credits

Created by [Piebuy](https://github.com/Piebuy).

This project is an OoT/MM checklist/tracking utility intended to work alongside an emulator and randomizer spoiler logs.
