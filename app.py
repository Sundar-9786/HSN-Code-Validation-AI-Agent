from flask import Flask, request, jsonify
from validation import load_hsn_data, validate_hsn_code, validate_multiple_hsn_codes

app = Flask(__name__)

# Load HSN data only once at startup
file_path = "HSN_SAC.xlsx"  # Adjusted for server path
hsn_dict = load_hsn_data(file_path)

@app.route("/", methods=["GET"])
def home():
    return "✅ HSN Validator is running."

@app.route("/webhook", methods=["POST"])
def webhook():
    req = request.get_json()

    # Step 1: Extract text from Dialogflow request
    user_input = req.get("queryResult", {}).get("queryText", "")

    # Step 2: Extract 2–8 digit codes from user input
    import re
    codes = re.findall(r'\b\d{2,8}\b', user_input)

    # Step 3: Validate
    if not codes:
        return jsonify({"fulfillmentText": "❌ I couldn't find any valid HSN codes in your input."})

    if len(codes) == 1:
        result = validate_hsn_code(codes[0], hsn_dict)
        return jsonify({"fulfillmentText": format_single_result(result)})

    results = validate_multiple_hsn_codes(codes, hsn_dict)
    formatted = "\n".join([format_single_result(r) for r in results])
    return jsonify({"fulfillmentText": formatted})


def format_single_result(result):
    if result["Valid"]:
        return f"✅ {result['Code']} → {result['Description']}"
    else:
        msg = f"❌ {result['Code']} → {result['Reason']}"
        if result.get("Suggestions"):
            msg += "\n   🔎 Suggestions:\n"
            for c, d in result["Suggestions"]:
                msg += f"   • {c}: {d}\n"
        return msg.strip()


#if __name__ == '__main__':
#    app.run(debug=True)

