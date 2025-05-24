var socket = io();
socket.on('connect', function() {
        console.log('Connected to the server');
    });

function add_friend(id) {
        socket.emit('add_friend', { friend_id: id });
}
socket.on('add_friend_response', function(data) {
        console.log('Add friend response:', data);
    });