var socket = io();
socket.on('connect', function () {
        console.log('Connected to the server');
});

function add_friend(id) {
        document.getElementById("btn_"+id).classList.add("disabled");
        socket.emit('add_friend', { friend_id: id });
}
socket.on('add_friend_response', function (data) {
        console.log('Add friend response:', data);
});

socket.on('new_message', function (data) {
        console.log('New message received:', data);
        if(data['recipient_id'] == parseInt(document.getElementById('userid').textContent)){
                has_read(data['sender_id']);
        }
        console.log(parseInt(document.getElementById('friendid').textContent), parseInt(document.getElementById('userid').textContent));
        if ((data['recipient_id'] == parseInt(document.getElementById('friendid').textContent) && data['sender_id'] == parseInt(document.getElementById('userid').textContent)) || (data['recipient_id'] == parseInt(document.getElementById('userid').textContent) && data['sender_id'] == parseInt(document.getElementById('friendid').textContent))) {
                console.log('Message is for this chat');
                var parent = document.getElementById('messagesContainer');
                var messageElement = document.createElement('div');
                messageElement.className = 'message ' + (data.sender_id == document.getElementById('userid').textContent ? 'sent' : 'received');
                messageElement.innerText = ` ${data.content}`;
                parent.appendChild(messageElement);
                parent.scrollTop = parent.scrollHeight;
        }
});

function send_message(id) {
        console.log('Sending message to friend with ID:', id);
        var message = document.getElementById('messageInput').value;
        socket.emit('send_message', { recipient_id: id, content: message });
        document.getElementById('messageInput').value = '';
}

function has_read(id) {
        socket.emit('has_read', { friend_id: id });
}
