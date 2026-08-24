from flask import Flask, render_template, request, jsonify
from services import load_matching_scene,load_data,save_data,create_check_dict
from globals import LOCATIONS_FILE,CURRENT_SCENE_FILE

app = Flask(__name__)


# ============================================================
# CURRENT LOCATION
# ============================================================

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

    # A location is completed if it is checked OR marked as junk.
    def is_completed(location):
        return (
            location.get("checked") is True
            or location.get("junk") is True
        )

    # =========================================
    # Current scene count
    # =========================================

    current_checked = sum(
        1
        for location in current_locations
        if is_completed(location)
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
            if is_completed(location)
        )

    return jsonify({
        "current_key": current_key,
        "locations": current_locations,
        "checked_locations": current_checked,
        "total_locations": current_total,
        "all_checked": all_checked,
        "all_total": all_total
    })


# ============================================================
# UPDATE CHECKBOX / JUNK CHECKBOX
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
    check_type = request_data.get("type", "checked")
    value = request_data.get("value")

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

    if check_type not in ("checked", "junk"):
        return jsonify({
            "success": False,
            "error": "type must be 'checked' or 'junk'"
        }), 400

    if not isinstance(value, bool):
        return jsonify({
            "success": False,
            "error": "value must be true or false"
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

            # Preserve the two states independently.
            check[check_type] = value
            found = True
            break

    if not found:
        return jsonify({
            "success": False,
            "error": f"Location '{location}' not found in scene '{scene}'"
        }), 404

    # Recalculate this scene's completed count.
    scene_data["checked_locations"] = sum(
        1
        for check in scene_data.get("locations", [])
        if (
            check.get("checked") is True
            or check.get("junk") is True
        )
    )

    save_data(data)

    # Calculate global completed count as well.
    all_locations = []

    for scene_name, scene_data in data.items(): # type: ignore

        for check in scene_data.get("locations", []):

            all_locations.append(check)

    all_checked = sum(
        1
        for check in all_locations
        if (
            check.get("checked") is True
            or check.get("junk") is True
        )
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
                "junk": location.get("junk", False),
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