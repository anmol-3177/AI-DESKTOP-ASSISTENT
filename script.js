const serverStatus = document.getElementById("serverStatus");
const languageSelect = document.getElementById("languageSelect");
const startBtn = document.getElementById("startBtn");
const sendBtn = document.getElementById("sendBtn");
const userInput = document.getElementById("userInput");
const historyList = document.getElementById("historyList");

// Simulate checking server status
setTimeout(() => {
  serverStatus.textContent = "online";
  serverStatus.classList.remove("error");
  serverStatus.classList.add("online");
}, 1500);

// Handle language change
languageSelect.addEventListener("change", () => {
  alert("Language changed to: " + languageSelect.options[languageSelect.selectedIndex].text);
});

// Simulate voice input
startBtn.addEventListener("click", () => {
  alert("🎙️ Listening for command (simulated)...");
});

// Handle Send button
sendBtn.addEventListener("click", () => {
  const command = userInput.value.trim();
  if (!command) return;

  const entry = document.createElement("div");
  entry.textContent = "🧠 " + command;
  historyList.prepend(entry);

  userInput.value = "";
});

// Optional: Speech synthesis
document.getElementById("speakBtn").addEventListener("click", () => {
  const msg = new SpeechSynthesisUtterance("Hello! I am your AI desktop assistant.");
  msg.lang = "en-US";
  window.speechSynthesis.speak(msg);
});
