from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/key&althaf/number', methods=['GET'])
def lookup_number():
    number = request.args.get('number')
    
    if not number:
        return jsonify({
            "status": False,
            "error": "Number parameter is missing. Use ?number=YOUR_NUMBER",
            "developer": "@Your_father_786k"
        }), 400
    
    # Original Supabase Backend URL
    target_url = f"https://nmdllpezcocquamhgpmb.supabase.co/functions/v1/lookup?number={number}"
    
    try:
        # Fetch response from the original backend
        response = requests.get(target_url, timeout=10)
        data = response.json()
    except Exception as e:
        return jsonify({
            "status": False,
            "error": "Failed to fetch data",
            "developer": "@Your_father_786k"
        }), 500
    
    # Clean and modify the response data to hide original credits/tags
    if isinstance(data, dict):
        # Remove common old credit/tag keys if they exist in the response
        keys_to_remove = ['credit', 'credits', 'tag', 'tags', 'author', 'developer', 'source', 'creator']
        for key in keys_to_remove:
            data.pop(key, None)
            
        # Inject your custom developer tag
        data['developer'] = '@Your_father_786k'
        
    elif isinstance(data, list):
        # If the API returns a list, wrap it in a dictionary to include the developer tag
        data = {
            "result": data,
            "developer": "@Your_father_786k"
        }
    
    return jsonify(data)

# Local testing support
if __name__ == '__main__':
    app.run(debug=True)
