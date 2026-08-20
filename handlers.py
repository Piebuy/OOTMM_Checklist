from services import get_scene_change

# Handlers incase of multiple dataprocessing from the emulator
HANDLERS = {
    "scene_changed": get_scene_change,
}