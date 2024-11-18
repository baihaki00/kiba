console.log("Chat.js is running!");

const input = document.querySelector('input[type="text"]');
const textBox = document.querySelector('.text-box');

input.addEventListener('keypress', function (e) {
    console.log("Key pressed:", e.key);  // Check if event is being triggered
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
    const botReply = "Hello, I'm KIBA!";
    console.log('Bot reply:', botReply); // Log the bot reply
    displayMessage(botReply, 'kiba-chatbubble');
}
