from typing import Any, Dict

def create_response(success: bool, message: str, data: Any = None) -> Dict[str, Any]:
    response = {"success": success, "message": message}
    if data is not None:
        response["data"] = data
    return response
