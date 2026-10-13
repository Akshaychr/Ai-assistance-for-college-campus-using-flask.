const form = document.querySelector('#question-form');
const input = document.querySelector('#question');
const chat = document.querySelector('#chat-area');

function escapeHtml(value) {
  return value.replace(/[&<>"']/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));
}

function addQuestion(text) {
  const row = document.createElement('div');
  row.className = 'message user-message';
  row.innerHTML = `<div class="bubble"><p>${escapeHtml(text)}</p></div>`;
  chat.appendChild(row);
}

function addAnswers(answers) {
  const row = document.createElement('div');
  row.className = 'message assistant-message answer-message';
  const cards = answers.map(item => `<div class="answer-item"><span class="answer-category">${escapeHtml(item.category)}</span>${item.question ? `<strong>${escapeHtml(item.question)}</strong>` : ''}<p>${escapeHtml(item.answer)}</p></div>`).join('');
  row.innerHTML = `<div class="mini-avatar">✦</div><div class="bubble">${cards}<small>Campus Companion · just now</small></div>`;
  chat.appendChild(row);
  chat.scrollTop = chat.scrollHeight;
}

async function ask(question) {
  if (!question.trim()) return;
  addQuestion(question.trim());
  input.value = '';
  chat.scrollTop = chat.scrollHeight;
  try {
    const response = await fetch('/api/ask', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({question})});
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || 'Please try again.');
    addAnswers(data.answers);
  } catch (error) {
    addAnswers([{category:'Connection', answer:'The campus guide could not be reached. Please try again in a moment.'}]);
  }
}

form.addEventListener('submit', event => { event.preventDefault(); ask(input.value); });
document.querySelectorAll('[data-question]').forEach(button => button.addEventListener('click', () => ask(button.dataset.question)));
document.querySelector('#clear-chat').addEventListener('click', () => {
  chat.innerHTML = '<div class="welcome-message"><div class="message-avatar"><img src="/static/mira.svg" alt=""></div><div class="message-content"><div class="message-bubble"><span class="bubble-kicker">MIRA · SOUNDARYA CAMPUS GUIDE</span><p>Hi! I can help you find information about programs, the library, canteen, events, transport, and more. What would you like to know?</p></div><small class="message-time">A quick answer is just a question away.</small></div></div>';
  chat.scrollTop = 0;
});
document.querySelectorAll('[data-category]').forEach(button => button.addEventListener('click', async () => {
  const category = button.dataset.category;
  try {
    const response = await fetch(`/api/faqs?category=${encodeURIComponent(category)}`);
    const items = await response.json();
    addQuestion(`Show me ${category} questions`);
    addAnswers(items.slice(0, 5));
  } catch {
    addAnswers([{category:'Connection', answer:'The campus guide could not be reached. Please try again in a moment.'}]);
  }
  document.querySelector('#question').focus();
}));
