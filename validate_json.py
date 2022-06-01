fields = {
        "first_name": {"type": "string"},
        "last_name": {"type": ["string", "null"]},
        "country": {"type": ["string", "null"]},
        "city": {"type": ["string", "null"]},
        "address": {"type": ["string", "null"]},
        "phone": {"type": ["string", "null"], "pattern": r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$"},
        "email": {"type": "string", "pattern": r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"}
    }

validate_create_user_json = {
  "type": "object",
  "properties": fields,
  "required": ["email", "first_name"]
}

validate_change_user_info = {
  "type": "object",
  "properties": fields,
}