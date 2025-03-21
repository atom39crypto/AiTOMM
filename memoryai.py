import json
from datetime import datetime
from groq import Groq

with open("engine/Weilder/memory.json", 'r') as file:
    data = json.load(file)

def usernames():
    try:
        # Extract the user names from the 'users' section of the loaded data
        user_names = list(data["users"].keys())
        return user_names
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def loaddata(user_key):
    try:
        # Check if the user exists in the loaded data and return the corresponding user data
        if "users" in data and user_key in data["users"]:
            return data["users"][user_key]  # Return the entire user data (not a dictionary)
        else:
            print(f"User '{user_key}' not found in the file.")
            return None
    except Exception as e:
        print(f"An error occurred while loading data for {user_key}: {e}")
        return None

def firstframe(user_data):
    client = Groq()
    try:
        # You can modify this prompt if needed, as it's now directly using the user data
        prompt = f"Create a report from the following user data: {user_data}"

        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": """from the conversations provided to you create a report of the person in the structure of 
                                    {
                                        "Name":
                                        "overall_personality":             
                                        "interests": ,
                                        "last_updated": "       
                                    }    
                                don't provide anything else before or after"""
                },
                {
                    "role": "user",
                    "content": f"{prompt}"
                }
            ],
            temperature=1,
            max_completion_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )

        # Collecting the response from the streaming output
        report = ""
        for chunk in completion:
            report += chunk.choices[0].delta.content or ""
        
        return report
    except Exception as e:
        return f"An error occurred: {str(e)}"

def save(json_string, user_name):
    try:
        # Load existing data from "Impretion.json" if it exists
        try:
            with open("Impretion.json", "r") as file:
                data_dict = json.load(file)
        except FileNotFoundError:
            data_dict = {"users": {}}
        
        # Add or update the user data
        data_dict["users"][user_name] = json.loads(json_string)
    
        # Save the updated dictionary to "Impretion.json"
        with open("Impretion.json", "w") as file:
            json.dump(data_dict, file, indent=4)
        
        print(f"Data successfully saved to 'Impretion.json' for user: {user_name}.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to process multiple users
def Impretions():
    user_keys = usernames()
    for user_key in user_keys:
        user_data = loaddata(user_key)

        if user_data:
            report = firstframe(user_data)
            save(report, user_key)

# Example usage
if __name__ == "__main__":  # Get the list of user keys
    Impretions()  # Process all users
