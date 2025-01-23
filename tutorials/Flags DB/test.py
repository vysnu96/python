from datetime import datetime
import pytz
from pymongo import MongoClient

timezone = pytz.timezone("Asia/Kolkata")
now = datetime.now(timezone)
formatted_time = now.strftime("%d-%B-%Y %I:%M %p")
print("Current date and time:", formatted_time)

client = MongoClient(
    "mongodb+srv://vishnu:C1kW0dlbf0UTsSb4@targeryen.bvinedn.mongodb.net/?retryWrites=true&w=majority&appName=targeryen")
database = client['flagQuiz']
collection = database['users_historic_data']

# users_choices = ['india', 'pak', 'chn', 'japan', 'nepal']
# selected = ['nepal', 'chn', 'india', 'pak', 'japan']
#
# score_data = {"users_choices": users_choices,
#               "selected": selected }
#
# # collection.insert_one(score_data)
# collection.update_one({"username":"vishnu"},
#                       {"$set": score_data})

username = "vishnu"
new_result = {
            "score": 50,
            "correct_options": ["Q", "R", "Z"],
            "selected_options": ["Q", "Z", "R"],
            "date": f"{formatted_time} IST"
}
# collection.insert_one(first_result)
collection.update_one(
    {"username": username},  # Find the user
    {"$push": {"quiz_results": new_result}}  # Append the new quiz result
)