from flask import Flask, jsonify, request, make_response
import time

app = Flask(__name__)

# In-memory storage to emulate system state
mock_state = {
    "tcpPacketsCount": 120,
    "arpPacketsCount": 5,
    "udpPacketsCount": 15,
    "totalPacketsCount": 140,
    "portStatus": True,
    "config": {
        "logTCP": True,
        "logARP": False,
        "logUDP": True
    },
    "systemTime": time.time_ns()
}

# --- 1. GET /api/status ---
@app.route('/api/status', methods=['GET'])
def get_status():
    response_data = {
        "tcpPacketsCount": mock_state["tcpPacketsCount"],
        "arpPacketsCount": mock_state["arpPacketsCount"],
        "udpPacketsCount": mock_state["udpPacketsCount"],
        "totalPacketsCount": mock_state["totalPacketsCount"],
        "logging PortStatus": mock_state["portStatus"]
    }
    return jsonify(response_data), 200


# --- 2. UPDATE (PUT) /api/set/time ---
@app.route('/api/set/time', methods=['PUT'])
def set_time():
    try:
        content = request.get_data(as_text=True)
        new_time = int(content)
        mock_state["systemTime"] = new_time
        return "", 200
    except ValueError:
        # CHANGED: Returns 400 Bad Request on failure
        return make_response("Invalid format", 400)


# --- 3. UPDATE (PUT) /api/updateConfig ---
@app.route('/api/updateConfig', methods=['PUT'])
def update_config():
    try:
        data = request.json
        if not all(k in data and isinstance(data[k], bool) for k in ("logTCP", "logARP", "logUDP")):
            raise ValueError("Missing keys or wrong type")

        mock_state["config"]["logTCP"] = data["logTCP"]
        mock_state["config"]["logARP"] = data["logARP"]
        mock_state["config"]["logUDP"] = data["logUDP"]

        return "", 200
    except (TypeError, ValueError, AttributeError):
        # CHANGED: Returns 400 Bad Request on failure
        return make_response("Failed/Wrong Format", 400)


# --- 4. GET /api/loadConfig ---
@app.route('/api/loadConfig', methods=['GET'])
def load_config():
    response_data = {
        "logTCP": mock_state["config"]["logTCP"],
        "logARP": mock_state["config"]["logARP"],
        "logUDP": mock_state["config"]["logUDP"]
    }
    return jsonify(response_data), 200


# --- 5. POST /api/injectPacket ---
@app.route('/api/injectPacket', methods=['POST'])
def inject_packet():
    try:
        data = request.json
        if "bytes" not in data or not isinstance(data["bytes"], list):
            raise ValueError("Invalid JSON structure")
        
        if not all(isinstance(b, int) for b in data["bytes"]):
             raise ValueError("Bytes array must contain integers")

        mock_state["udpPacketsCount"] += 1
        mock_state["totalPacketsCount"] += 1

        return "", 200
    except (TypeError, ValueError, AttributeError):
        # CHANGED: Returns 400 Bad Request on failure
        return make_response("Failed", 400)

if __name__ == '__main__':
    app.run(debug=True, port=5000)