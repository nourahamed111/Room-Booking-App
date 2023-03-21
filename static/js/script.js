
// declerations
const welcomeP = document.getElementById("welcomeUser");
const openDetailsBtn = document.getElementById("openDetails");
const mainShowDiv = document.getElementById("main");
const addRoomBtn = document.getElementById("addRoomBtn");
const showUserBtn = document.getElementById("showUser");
const showAdminBtn = document.getElementById("showAdmin");
const indexContent = document.getElementById("contentIndex");
const form = document.getElementById('addForm');
//functions
// function to display the user login div 
function userDiv() {
    indexContent.classList.add("blur");
    const adminNameInput = document.getElementById("adminNameInput");
    const userNameInput = document.getElementById("userNameInput");
    adminNameInput.classList.add("popupDetailsHide");
    userNameInput.classList.remove("popupDetailsHide");
}
// function to display the admin login div 
function adminDiv() {
    indexContent.classList.add("blur");
    const adminNameInput = document.getElementById("adminNameInput");
    const userNameInput = document.getElementById("userNameInput");
    userNameInput.classList.add("popupDetailsHide");
    adminNameInput.classList.remove("popupDetailsHide");
}
// function to display  close th admin and user login div 
function cancelLogin() {
    userNameInput.classList.add("popupDetailsHide");
    adminNameInput.classList.add("popupDetailsHide");
    indexContent.classList.remove("blur");
}
// function to to save username in local storage and display msg and display the alert if the user name is null

function userLogin() {
    const userName = document.getElementById("user_id");
    userNameValue = userName.value;
    if (userNameValue !== "") {
        nameKey = userNameValue + "U"
        if (localStorage.getItem(nameKey) === null) {
            localStorage.setItem(nameKey, userNameValue);
            alert("Welcome " + userNameValue + " Happy to have you here");
        }
        else if (localStorage.getItem(nameKey) !== null) {
            alert("Welcome Back");
        }
    } else {
        alert("Please enter Your username");
    }

}
// function to display alert if the admin password is wrong or null
function adminLogin() {
    const adminId = document.getElementById("admin_id");
    adminIdValue = adminId.value;
    if (adminIdValue == "") {

        alert("Please Enter Your Password ");
    } else if (adminIdValue != "123456") {
        alert("Wrong Password");
    }
}
//open room details popup
function showItems(roomId) {
    const popupDetailsDiv = document.getElementById("popupDetails" + roomId);
    popupDetailsDiv.classList.remove("popupDetailsHide");
    mainShowDiv.classList.add("blur");
}
//close room details popup
function hideItems(roomId) {
    const popupDetailsDiv = document.getElementById("popupDetails" + roomId);
    popupDetailsDiv.classList.add("popupDetailsHide");
    mainShowDiv.classList.remove("blur");
}
//function open add room div
function showAddForm() {
    const addDiv = document.getElementById("addDiv");
    addDiv.classList.toggle("popupDetailsHide");
}

// add room validation from (chatGPT)
form.addEventListener('submit', (event) => {
    event.preventDefault();
    const roomTitle = document.getElementById('roomTitle').value;
    const roomDesc = document.getElementById('roomDesc').value;
    const roomImg = document.getElementById('roomImg').value;

    // Check for valid input
    if (roomTitle === '') {
        alert('Please enter a room name.');
        return;
    }

    if (roomDesc === '') {
        alert('Please enter a room description.');
        return;
    }

    if (roomImg === '') {
        alert('Please select a room image.');
        return;
    }

    // Submit the form if all fields are valid
    form.submit();
});



