var socket = io();
socket.on('connect', function () {
        console.log('Connected to the server');
});

function add_friend(id) {
        btn = document.getElementById("add_frnd_prfl");
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
                var messagespan = document.createElement('span');
                messagespan.className = 'message  inline-block py-2 px-3 my-1 max-w-[75%] break-words border-white border-2 ' + (data.sender_id != document.getElementById('userid').textContent ? 'bg-indigo-100 text-slate-800 border-indigo-300 rounded-t-xl rounded-r-xl rounded-bl-xl mr-auto' : 'bg-indigo-500 text-white border-indigo-600 rounded-t-xl rounded-l-xl rounded-br-xl ml-auto');

                messagespan.innerText = ` ${data.content}`;
                messageElement = document.createElement('div');
                messageElement.appendChild(messagespan);
                messageElement.className = 'h-auto flex'
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
                notificationPanel.classList.toggle('hidden'); // Toggles hidden class
                notificationPanel.classList.toggle('flex');
        }
});
document.getElementById('notificationLink1')?.addEventListener('click', function (e) {
        e.preventDefault();
        socket.emit('get_notifications');
        const panel = document.getElementById('notificationPanel');
        if (panel) {
                notificationPanel.classList.toggle('hidden'); // Toggles hidden class
                notificationPanel.classList.toggle('flex');
        }
});



socket.on('notification_list', function (data) {
        const notificationList = document.getElementById('notificationList');
        notificationList.innerHTML = '';
        data.notifications.forEach(n => {
                const item = document.createElement('a');
                item.href = `/message/${n.sender}`;
                item.className = 'notification-item p-2  text-wrap overflow-x-clip bg-yellow-50 m-2 mb-0 rounded-[8px]';
                item.innerHTML = `
        <strong>From:</strong> ${n.sender}<br>
        ${n.content}
        `;
                notificationList.appendChild(item);
        });
});
