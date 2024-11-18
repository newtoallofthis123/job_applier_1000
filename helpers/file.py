import json
import os

APP_NAME = "job_applier"
CONFIG_FILE = "config.json"
CONFIG_PATH = os.path.join(os.path.expanduser("~"), f".{APP_NAME}", CONFIG_FILE)
DB_FILE = "store.db"
DB_PATH = os.path.join(os.path.expanduser("~"), f".{APP_NAME}", DB_FILE)
STORE_FILE = "resume.json"
STORE_PATH = os.path.join(os.path.expanduser("~"), f".{APP_NAME}", STORE_FILE)


def setup_file_handlers() -> None:
    if (
        os.path.exists(CONFIG_PATH)
        and os.path.exists(DB_PATH)
        and os.path.exists(STORE_PATH)
    ):
        return
    else:
        os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
        if not os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH, "w") as f:
                f.write("{}")

        if not os.path.exists(DB_PATH):
            with open(DB_PATH, "w") as f:
                f.write("")

        if not os.path.exists(STORE_PATH):
            with open(STORE_PATH, "w") as f:
                f.write("")


def get_config_file() -> dict:
    with open(CONFIG_PATH, "r") as f:
        return json.loads(f.read())


def get_db_path() -> str:
    return DB_PATH


def get_store_file() -> dict:
    with open(STORE_PATH, "r") as f:
        return json.loads(f.read())


def save_store_file(data: dict) -> None:
    with open(STORE_PATH, "w") as f:
        f.write(json.dumps(data, indent=4))
