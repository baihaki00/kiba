console.log("Chat.js is running!");

const input = document.querySelector('input[type="text"]');
const textBox = document.querySelector('.text-box');

const kibaTextSound = new Audio('../sounds/kibasound2.wav');

input.addEventListener('keypress', function (e) {   
    console.log("Key pressed:", e.key); // Check if event is triggered
    if (e.key === 'Enter') {
        const userMessage = input.value.trim();
        if (userMessage) {
            console.log('User message entered:', userMessage); // Log user input
            displayMessage(userMessage, 'user-chatbubble');
            input.value = '';
            getBotResponse(userMessage);
        }
    }
});

function displayMessage(message, sender) {
    const messageElement = document.createElement('div');
    messageElement.textContent = message;
    messageElement.classList.add('message', sender);

    // Append the new message element to the text box
    textBox.appendChild(messageElement);

    // Scroll to the latest message
    textBox.scrollTop = textBox.scrollHeight;
}

function getBotResponse(userMessage) {
    fetch('http://127.0.0.1:5000/api/message', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userMessage })
    })
        .then(response => response.json())
        .then(data => {
            console.log('Bot reply:', data.reply); // Log the bot reply
            displayMessage(data.reply, 'kiba-chatbubble');
            kibaTextSound.play();
        })
        .catch(err => {
            console.error(err);
            displayMessage("Oops! Something went wrong. Please try again.", 'kiba-chatbubble');
        });
}