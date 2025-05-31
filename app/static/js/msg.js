const textarea = document.getElementById("messageInput");
const submitBtn = document.getElementById("submitBtnmsg");
textarea.addEventListener("keypress", function (e) {
    if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        submitBtn.click();
    }
});
function scrollToBottom() {
    const messagesContainer = document.getElementById('messagesContainer');
    if (messagesContainer) {
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }
}
scrollToBottom();
window.onload = function() {
            has_read(document.getElementById('friendid').textContent)};