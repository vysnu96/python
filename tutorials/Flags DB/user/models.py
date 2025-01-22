# from flask import Flask, jsonify, request
# import random, os, hashlib, uuid
#
#
# # import flags
# class User:
#     def signup(self):
#         from flags import database
#         user = {
#             "_id": uuid.uuid4().hex,
#             "username": request.form.get('username'),
#             "password": request.form.get('password'),
#             "salt": ""
#         }
#         salt = os.urandom(16)
#         user['salt'] = salt.hex()  #Converted to hex for JSON serializable
#         user['password'] = hashlib.sha256(user['password'].encode() + salt).hexdigest()
#         collection = database['users']
#         if collection.find_one({"username": user['username']}):
#             return "Username exists"
#         collection.insert_one(user)
#         print("original salt", salt)
#         print(user)
#         return user, 200
#
#
from flask import Flask, jsonify, request, session
import random, os, hashlib, uuid

class User:

    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200

    def login(self):
        from flags import database
        collection = database['users']
        username = request.form.get('username')
        password = request.form.get('password')
        user = collection.find_one({"username": "vishnu"}, {"_id": 0})
        computed_password = hashlib.sha256(password.encode() + bytes.fromhex(user['salt'])).hexdigest()
        print("stored", user['password'])
        print("computed", computed_password)
        if (user['username'] == username) and (user['password'] == computed_password):
            return self.start_session(user)
        else:
            return jsonify({"error": "Invalid login credentials"}), 401