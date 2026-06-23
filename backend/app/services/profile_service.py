from app.services.master_profile import get_master_profile

PROFILE = {}


def load_master_profile():
    global PROFILE

    PROFILE = get_master_profile()

    print("MASTER PROFILE LOADED (HARD CODED)")
    print(PROFILE)

    return PROFILE

