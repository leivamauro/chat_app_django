const btnSend = document.getElementById('sendMessage')
const messageBox = document.querySelector('.message-box')
const inputMessage = document.getElementById('message')

btnSend.addEventListener('click', sendMessage)

url = 'ws://' + window.location.host + '/ws/room/' + room_id + '/'
console.log(url)

chatSocket = new WebSocket(url)

chatSocket.onopen = function(e) {
    console.log("CONEXION ESTABLECIDA")
}

chatSocket.onclose = function(e) {
    console.log("CONEXION CERRADA")
}

function sendMessage() {
    let msg = inputMessage.value.trim()

    if (msg !== ''){
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
        `
        inputMessage.value = ''
    } else {
        console.log("mensaje vacio")
    }

}    
