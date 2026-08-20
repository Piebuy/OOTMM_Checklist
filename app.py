from flask import Flask, render_template, request, jsonify
from services import load_matching_scene,load_data,save_data,create_check_dict
from globals import LOCATIONS_FILE,CURRENT_SCENE_FILE

app = Flask(__name__)


# ============================================================
# CURRENT LOCATION
# ============================================================

# Your existing code should update this variable.
#
# For example:
#
# matching_scene = "Whiterun"
# current_key = matching_scene
#
# If your existing code already has current_key, you can
# remove this variable and use your existing one instead.

current_key = ""

# ============================================================
# MAIN PAGE
# ============================================================

@app.route("/")
def index():
    return render_template("index.html")


# ============================================================
# GET CURRENT LOCATION
# ============================================================

@app.route("/api/current")
def api_current():

    current_key = load_matching_scene()

    data = load_data()

    scene_data = data.get(current_key, {}) # type: ignore

    current_locations = scene_data.get(
        "locations",
        []
    )


    # =========================================
    # Current scene count
    # =========================================

    current_checked = sum(
        1
        for location in current_locations
        if location.get("checked") is True
    )


    current_total = len(current_locations)


    # =========================================
    # ALL scenes count
    # =========================================

    all_checked = 0
    all_total = 0


    for scene_data in data.values(): # type: ignore

        locations = scene_data.get(
            "locations",
            []
        )

        all_total += len(locations)

        all_checked += sum(
            1
            for location in locations
            if location.get("checked") is True
        )


    return jsonify({

        "current_key":
            current_key,

        "locations":
            current_locations,

        "checked_locations":
            current_checked,

        "total_locations":
            current_total,

        "all_checked":
            all_checked,

        "all_total":
            all_total

    })


# ============================================================
# UPDATE CHECKBOX
# ============================================================

@app.route("/api/check", methods=["POST"])
def api_check():

    request_data = request.get_json()

    if not request_data:
        return jsonify({
            "success": False,
            "error": "No JSON data received"
        }), 400

    scene = request_data.get("scene")
    location = request_data.get("location")
    checked = request_data.get("checked")

    if scene is None:
        return jsonify({
            "success": False,
            "error": "Missing scene"
        }), 400

    if location is None:
        return jsonify({
            "success": False,
            "error": "Missing location"
        }), 400

    if not isinstance(checked, bool):
        return jsonify({
            "success": False,
            "error": "checked must be true or false"
        }), 400

    data = load_data()

    if scene not in data:
        return jsonify({
            "success": False,
            "error": f"Scene '{scene}' not found"
        }), 404

    scene_data = data[scene] # type: ignore

    found = False

    for check in scene_data.get("locations", []):

        if check.get("location") == location:

            check["checked"] = checked
            found = True
            break

    if not found:
        return jsonify({
            "success": False,
            "error": f"Location '{location}' not found in scene '{scene}'"
        }), 404

    # Recalculate this scene's checked count
    scene_data["checked_locations"] = sum(
        1
        for check in scene_data.get("locations", [])
        if check.get("checked") is True
    )

    save_data(data)

    # Calculate global count as well
    all_locations = []

    for scene_name, scene_data in data.items(): # type: ignore

        for check in scene_data.get("locations", []):

            all_locations.append(check)

    all_checked = sum(
        1
        for check in all_locations
        if check.get("checked") is True
    )

    return jsonify({
        "success": True,
        "checked_locations": scene_data["checked_locations"],
        "all_checked": all_checked,
        "all_total": len(all_locations)
    })

@app.route("/api/all")
def api_all():

    data = load_data()

    all_locations = []

    for scene, scene_data in data.items(): # type: ignore

        for location in scene_data.get("locations", []):

            all_locations.append({
                "scene": scene,
                "location": location.get("location", ""),
                "checked": location.get("checked", False),
                "item": location.get("item", "")
            })

    return jsonify({
        "locations": all_locations
    })

@app.route("/api/reset", methods=["POST"])
def api_reset():

    try:
        create_check_dict()

        return jsonify({
            "success": True
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500
# ============================================================
# START SERVER
# ============================================================

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5001,
        debug=False
    )