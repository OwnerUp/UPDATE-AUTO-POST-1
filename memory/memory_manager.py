import json
import os

# =========================
# FILE PATH
# =========================

MEMORY_FILE = "active_data.json"

# =========================
# LOAD MEMORY
# =========================

def load_memory():

    if not os.path.exists(MEMORY_FILE):

        return {
            "tosses": [],
            "matches": [],
            "sessions": [],
            "sballs": [],
            "inning_breaks": [],
            "entries": []
        }

    with open(MEMORY_FILE, "r") as file:

        data = json.load(file)

    return data

# =========================
# SAVE MEMORY
# =========================

def save_memory(data):

    with open(MEMORY_FILE, "w") as file:

        json.dump(data, file, indent=4)

# =========================
# RESET MEMORY
# =========================

def reset_memory():

    data = {
        "tosses": [],
        "matches": [],
        "sessions": [],
        "sballs": [],
        "inning_breaks": [],
        "entries": []
    }

    save_memory(data)

# =========================
# GET NEXT ID
# =========================

def get_next_id(section):

    data = load_memory()

    items = data.get(section, [])

    if not items:
        return 1

    return items[-1]["id"] + 1