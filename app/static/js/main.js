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
        console.log(parseInt(document.getElementById('recipientId').textContent), parseInt(document.getElementById('senderId').textContent));
        if ((data['recipient_id'] == parseInt(document.getElementById('recipientId').textContent) && data['sender_id'] == parseInt(document.getElementById('senderId').textContent)) || (data['recipient_id'] == parseInt(document.getElementById('senderId').textContent) && data['sender_id'] == parseInt(document.getElementById('recipientId').textContent))) {
                console.log('Message is for this chat');
                var parent = document.getElementById('messagesContainer');
                var messageElement = document.createElement('div');
                messageElement.className = 'message ' + (data.sender_id == document.getElementById('senderId').textContent ? 'sent' : 'received');
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

