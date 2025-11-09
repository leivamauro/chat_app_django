const btnSend = document.getElementById('sendMessage');
const messageBox = document.querySelector('.message-box');
const inputMessage = document.getElementById('message');

btnSend.addEventListener('click', sendMessage);

// websocket javascrip

url = "ws://" + window.location.host + "/ws/room/" + room_id + "/";

const chatSocket = new WebSocket(url);

chatSocket.onopen = function (e) {
    console.log("Conexion abrierta del cliente");
}

chatSocket.addEventListener("message", (e) => {
    let data = JSON.parse(e.data)
    if (user === data.username) return;
    messageBox.innerHTML += 
    `
    <div class="container">
        <div class="alert alert-success" role="alert">
            ${data.message}
            <div class="d-flex align-items-end justify-content-between text-body-secondary">
                <small class="text-start fst-italic">${data.username}</small>
                <small class="text-end">12/7/5 12:00</small>
            </div>
        </div>
    </div>
    `;
});

chatSocket.onclose = function (e) {
    console.log("cierre de conexion con el websocket del cliente");
}


function sendMessage() {
    let msg = inputMessage.value.trim();
    if (msg !== ''){
        chatSocket.send(JSON.stringify({"message": msg})); // envia el mensaje al servidor
        inputMessage.value = '';

        messageBox.innerHTML += 
        `
        <div class="container">
            <div class="alert alert-primary" role="alert">
                ${msg}
                <div class="d-flex align-items-end justify-content-between text-body-secondary">
                    <small class="text-start fst-italic">${user}</small>
                    <small class="text-end">12/7/5 12:00</small>
                </div>
            </div>
        </div>
        `;
        
    }
}