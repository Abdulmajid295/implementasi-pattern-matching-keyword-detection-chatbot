function addMessage(message, sender) {

    const chatBox = document.getElementById("chatBox");

    if (sender === "bot") {

        chatBox.innerHTML += `
            <div class="message bot">
                <div class="avatar">🤖</div>
                <div class="bubble">${message}</div>
            </div>
        `;

    } else {

        chatBox.innerHTML += `
            <div class="message user">
                <div class="bubble">${message}</div>
            </div>
        `;

    }

    chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {

    const input = document.getElementById("message");
    const message = input.value.trim();

    if (message === "") return;

    addMessage(message, "user");

    input.value = "";

    try {

        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        const data = await response.json();

        addMessage(data.response, "bot");

    } catch (error) {

        addMessage(
            "Terjadi kesalahan pada server.",
            "bot"
        );

    }
}

function handleEnter(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
}

window.onload = function() {

    addMessage(
        "Halo! Saya chatbot FAQ kampus.<br>Silakan ajukan pertanyaan Anda.",
        "bot"
    );

};