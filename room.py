## importing
from flask import Flask, redirect, render_template, request, json

app = Flask(__name__)
# room class 
class Room:
    #constructor
    def __init__(self, id, title, description, image, available):
        self.id = id
        self.title = title
        self.description = description
        self.image = image
        self.available = available
   #method the made the json file objects instance of the room class 
    def load_time_from_json(self,room_id):
        with open('rooms.json') as f:
            data_list = json.load(f)
        for obj in data_list:
            if obj['id'] == room_id:
                available_time = obj['available']
                self.available = available_time  
    #static method that create list of room objects
    @staticmethod
    def get_details():
        with open('rooms.json') as f:
            data_list = json.load(f)
        details_list = []
        for obj in data_list:
            if 'id' in obj and isinstance(obj['id'], int):
                room = Room(obj['id'], obj['room']['title'], obj['room']['description'], obj['room']['image'], obj['room']['available'])
                details_list.append(room)

        return details_list 

#function that deleted the selected time from json file according to user id 
def remove_time_from_json(room_id, time):
    with open('rooms.json', 'r') as f:
        data_list = json.load(f)
        for obj in data_list:
            if int( obj["id"]) == int(room_id):
                if time in  obj['room']['available']:
                    obj['room']['available'].remove(time)
                    break   # exit the loop if the time is found
    with open('rooms.json', 'w') as f:
        json.dump(data_list, f)
        f.close()  # add this line to close the file

#function to generate different id for every added room 
def get_next_id():
    with open('rooms.json') as f:
        data_list = json.load(f)
    max_id = max([obj['id'] for obj in data_list if 'id' in obj and isinstance(obj['id'], int)])
    return max_id + 1

# updated function that update the available time
@app.route('/update', methods=['POST'])
def update_room():
    room_id = request.form["room_id"]
    # load data from JSON file
    with open('rooms.json') as f:
     data_list = json.load(f)
    available_time = [
        "9:00 AM",
        "10:00 AM",
        "11:00 AM",
        "12:00 PM",
        "01:00 pM",
        "02:00 PM",
        "03:00 PM",
        "04:00 PM",
        "05:00 PM"
    ]
    for obj in data_list:
        if int(obj.get('id') )== int(room_id):
            obj['room']['available'] = available_time
            break  
    with open('rooms.json', 'w') as f:
        json.dump(data_list, f)

    room_details = Room.get_details()
    return render_template("admin.html", page_title="Rooms",
                           custom_css="room",
                           details=room_details
                           )

# added function that add new room
@app.route('/add', methods=['POST'])
def add_room():
    # load data from JSON file
    with open('rooms.json') as f:
        data_list = json.load(f)

    # parse form data
    room_id = get_next_id()
    room_title = request.form['roomTitle']
    room_desc = request.form['roomDesc']
    room_img = request.form['roomImg']
    room_time = [
        "9:00 AM",
        "10:00 AM",
        "11:00 AM",
        "12:00 PM",
        "01:00 pM",
        "02:00 PM",
        "03:00 PM",
        "04:00 PM",
        "05:00 PM"
    ]

    # create new room object
    new_room = {
        'id': room_id,
        'room': {
            'title': room_title,
            'description': room_desc,
            'image': "static/img/" + room_img,
            'available': room_time
        }
    }

    # append new room to data list
    data_list.append(new_room)

    # save data back to JSON file
    with open('rooms.json', 'w') as f:
        json.dump(data_list, f)

    # render the admin page with updated data
    room_details = Room.get_details()
    return render_template("admin.html", page_title="Rooms",
                           custom_css="room",
                           details=room_details)

#index page route
@app.route("/")
def indexpage():
    return render_template("index.html", page_title="Home")
#admin page route
@app.route("/admin")
def adminpage():
    admin_password = request.args.get('admin_password')
    if admin_password is None or admin_password!="123456":
        return redirect('/')
    else:
     room_details = Room.get_details()
     return render_template("admin.html", page_title="Rooms",
                           custom_css="room",
                           details=room_details)
#show page route
@app.route("/show")
def showpage():
    user_name = request.args.get('user_name')
    if user_name is None or user_name.strip() == "":
        return redirect('/')
    else:
        room_details = Room.get_details()
        return render_template("show.html", page_title="Rooms",
                               custom_css="room",
                               details=room_details)
#result page route
@app.route('/result')
def result():
    requested_time = request.args.get('time')
    room_id = request.args.get('room_id')
    remove_time_from_json(room_id,requested_time)
    return render_template('result.html', page_title="Result", time=requested_time,id=room_id)

if __name__ == "__main__":
    app.run(debug=True)
