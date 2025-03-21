import json
from datetime import datetime

# File path to store memory
file_path = 'engine/Weilder/memory.json'

def impretion(user_keys):
    with open("Impretion.json", 'r') as file:
        data = json.load(file)
    results = {}
    try:
        # Loop through the list of user keys
        for user_key in user_keys:
            # Check if the user exists in the loaded data
            if "users" in data and user_key in data["users"]:
                results[user_key] = data["users"][user_key]
            else:
                print(f"User '{user_key}' not found in the file.")
                results[user_key] = None

        return results

    except Exception as e:
        print(f"An error occurred while loading data: {e}")
        return None

# Function to load the last 5 user interactions
def loadmemory(user_key="SHounak"):

    try:
        # Load the JSON file
        with open(file_path, "r") as file:
            data = json.load(file)
        
        # Extract the user data
        user_data = data.get("users", {}).get(user_key, [])
        
        # Get the last 5 entries
        last_5_entries = user_data[-5:]
        
        # Format the entries into the desired structure
        formatted_entries = []
        for entry in last_5_entries:
            user_input = entry.get("user_input", "")
            assistant_response = entry.get("assistant_response", "")
            
            # Add user and assistant entries to the formatted list
            if user_input:
                formatted_entries.append({"role": "user", "content": user_input})
            if assistant_response:
                formatted_entries.append({"role": "assistant", "content": assistant_response})
        
        return formatted_entries
    except (FileNotFoundError, json.JSONDecodeError) as e:
        return {"error": str(e)}

# Function to save a conversation
def save_conversation(user_input, assistant_response,username ="SHounak"):

    new_entry = {
        "timestamp": datetime.now().isoformat(),
        "user_input": user_input,
        "assistant_response": assistant_response
    }
    
    try:
        # Load existing data from the file
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # If file doesn't exist or is invalid, initialize a new structure
            data = {"users": {}}
        
        # Add or update the user's conversation list
        if username not in data["users"]:
            data["users"][username] = []
        data["users"][username].append(new_entry)
        
        # Save the updated data back to the file
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
        print("Conversation saved successfully.")
    except Exception as e:
        print(f"Error saving conversation: {e}")

# Example usage
if __name__ == "__main__":
    # Test loading memory
    user_key = "SHounak"
    result = loadmemory()
    print("Last 5 interactions:", result)
    
    # Test saving a conversation
    user_input = "I want pasta "
    assistant_response = "I am not your mom"
    save_conversation(user_input, assistant_response)
