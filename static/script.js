let chatHistory = [];

document.addEventListener("DOMContentLoaded", function() {
    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: "hi", chat_history: chatHistory })
    })
    .then(response => response.json())
    .then(data => {
        appendMessage(data.response, "bot");
        chatHistory = data.chat_history;
    })
    .catch(error => console.error("Erreur:", error));
});


function appendMessage(text, className) {
    let chatBox = document.getElementById("chat-box");
    let msg = document.createElement("div");
    msg.className = "message " + className;
    
    // Replace line breaks (\n) with <br> to display them correctly in HTML
    msg.innerHTML = text.replace(/\n/g, "<br>");
    
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
}


function sendMessage() {
    let inputField = document.getElementById("message-input");

    let userMessage = inputField.value;
    if (!userMessage.trim()) return;

    appendMessage(userMessage, "user");
    inputField.value = "";

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userMessage, chat_history: chatHistory })
    })
    .then(response => response.json())
    .then(data => {
        appendMessage(data.response, "bot");
        chatHistory = data.chat_history;
    })
    .catch(error => console.error("Erreur:", error));

    console.log("|" + inputField.value + "|")
    inputField.value = "";
    inputField.style.height = 'auto'; 
    console.log("|" + inputField.value + "|")
}

function handleKeyPress(event) {
    if (event.key === "Enter" && !event.shiftKey){
        event.preventDefault();
        sendMessage();
    }
}


const messageInput = document.getElementById("message-input");

messageInput.addEventListener("input", () => {
    // Reset height to auto to shrink as necessary
    messageInput.style.height = 'auto';
    
    // Adjust height based on the scrollHeight (which includes all lines)
    messageInput.style.height = messageInput.scrollHeight + 'px';
});

