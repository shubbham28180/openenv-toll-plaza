fastag_db = {
    "RJ14CV0002": "Valid"
}

def check_fastag(number):
    return fastag_db.get(number, "Invalid")