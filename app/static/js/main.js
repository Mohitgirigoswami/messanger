var socket = io();
socket.on('connect', function () {
        console.log('Connected to the server');
});

function add_friend(id) {
        btn = document.getElementById("add_frnd_prfl" );
        if (btn) {
                btn.classList.add('disabled');
                btn.disabled = true;
                btn.textContent = 'Request Sent';
        }
        socket.emit('add_friend', { friend_id: id });
}
socket.on('add_friend_response', function (data) {
        console.log('Add friend response:', data);
});

socket.on('new_message', function (data) {
        console.log('New message received:', data);
        if (data['recipient_id'] == parseInt(document.getElementById('userid').textContent)) {
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

document.getElementById('notificationLink')?.addEventListener('click', function (e) {
        e.preventDefault();
        socket.emit('get_notifications');
        const panel = document.getElementById('notificationPanel');
        if (panel) {
                panel.style.display = (panel.style.display === 'none') ? 'block' : 'none';
        }
});



socket.on('notification_list', function (data) {
        const notificationList = document.getElementById('notificationList');
        notificationList.innerHTML = '';
        data.notifications.forEach(n => {
                const item = document.createElement('a');
                item.href = `/message/${n.sender}`;
                item.className = 'notification-item';
                item.innerHTML = `
            <strong>From:</strong> ${n.sender}<br>
            ${n.content}
        `;
                notificationList.appendChild(item);
        });
});
