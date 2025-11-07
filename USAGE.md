# Usage Guide: LLM on iPhone

## 🚀 Quick Start Guide

### For Web App (Recommended)

#### Option 1: Use Hosted Version

1. **Upload to GitHub Pages or any web host:**
   ```bash
   # If using GitHub Pages
   git add llm-iphone.html
   git commit -m "Add LLM iPhone web app"
   git push origin main

   # Enable GitHub Pages in repository settings
   # Access at: https://yourusername.github.io/llm/llm-iphone.html
   ```

2. **Or use simple Python server for local testing:**
   ```bash
   # On your computer (not iPhone)
   cd /path/to/llm
   python -m http.server 8000

   # Then on iPhone, open Safari and go to:
   # http://your-computer-ip:8000/llm-iphone.html
   ```

3. **Or use iCloud Drive:**
   - Upload `llm-iphone.html` to iCloud Drive
   - Open Files app on iPhone
   - Navigate to the file
   - Tap to open in Safari
   - Add to Home Screen

#### Option 2: Copy-Paste Direct

1. Open Safari on iPhone
2. Go to any text editor with HTML support
3. Create a new `.html` file
4. Copy the entire content of `llm-iphone.html`
5. Save and open in Safari

### For a-Shell App

#### Installation Steps

1. **Download a-Shell from App Store**
   - Search "a-Shell" in App Store
   - Install the free version (or a-Shell mini)

2. **Open a-Shell and install dependencies:**
   ```bash
   # Test Python
   python --version

   # Install OpenAI package (essential)
   pip install openai

   # Try installing other packages
   pip install click PyYAML python-ulid pluggy
   ```

3. **Download the simple script:**
   ```bash
   # Using curl (if available in a-Shell)
   curl -O https://raw.githubusercontent.com/yourusername/llm/main/llm_simple.py

   # Or create manually
   cat > llm_simple.py << 'EOF'
   [paste content of llm_simple.py here]
   EOF

   # Make executable
   chmod +x llm_simple.py
   ```

4. **Set up API key:**
   ```bash
   # For current session
   export OPENAI_API_KEY="sk-your-actual-key-here"

   # For all sessions (add to profile)
   echo 'export OPENAI_API_KEY="sk-your-actual-key-here"' >> ~/.profile
   source ~/.profile
   ```

5. **Test it:**
   ```bash
   python llm_simple.py "What is 2+2?"
   ```

---

## 📱 Using the Web App

### First Time Setup

1. **Open the app** (in Safari or from Home Screen)

2. **Wait for initialization** (~30-60 seconds first time)
   - Pyodide runtime loads
   - Python packages install
   - Status shows "Ready!" when done

3. **Enter your API key**
   - Get from: https://platform.openai.com/api-keys
   - Enter in the "OpenAI API Key" field
   - It's saved automatically in browser storage

4. **Select model**
   - gpt-4o-mini (fastest, cheapest)
   - gpt-4o (most capable)
   - gpt-3.5-turbo (good balance)

5. **Enter prompt and run!**

### Daily Usage

Once set up, just:
1. Open app (instant load from cache)
2. Type prompt
3. Tap "Run Prompt"
4. Read response

### Tips & Tricks

**Add to Home Screen for App Experience:**
- Safari → Share → Add to Home Screen
- Looks and feels like a native app
- Opens in full screen

**Works Offline (Mostly):**
- After first load, works offline
- Still needs internet for API calls
- Perfect for travel with internet

**Multiple Prompts:**
- Clear output between prompts
- Or keep scrolling to see history
- Consider implementing conversation mode

**Security:**
- API key stored locally only
- Never transmitted except to OpenAI
- Clear browser data to remove key

---

## 💻 Using a-Shell

### Basic Commands

```bash
# Simple prompt
python llm_simple.py "Tell me a joke"

# Specify model
python llm_simple.py -m gpt-4o "Explain quantum computing"

# Multi-word prompts (use quotes)
python llm_simple.py "What is the capital of France and why?"

# Piping (if supported)
echo "Translate to Spanish: Hello World" | python llm_simple.py
```

### Creating an Alias

Make it easier to use:

```bash
# Add to ~/.profile
echo "alias llm='python ~/llm_simple.py'" >> ~/.profile
source ~/.profile

# Now you can just use:
llm "Your prompt here"
llm -m gpt-4o "Your prompt"
```

### Advanced Usage

```bash
# Save response to file
python llm_simple.py "Generate a haiku" > haiku.txt

# Process file content
python llm_simple.py "Summarize this: $(cat notes.txt)"

# Chain with other commands
python llm_simple.py "Generate 5 random numbers" | python process.py
```

### Managing API Keys

```bash
# Check if key is set
echo $OPENAI_API_KEY

# Set for current session only
export OPENAI_API_KEY="sk-..."

# Set permanently (add to ~/.profile)
echo 'export OPENAI_API_KEY="sk-..."' >> ~/.profile

# Test the key
python llm_simple.py "Say hello"
```

---

## 🔧 Extending the Web App

### Add Anthropic Claude

1. Open `llm-iphone.html` in a text editor

2. Find the initialization section and add:

```javascript
await pyodide.runPythonAsync(`
    await micropip.install('anthropic')
    from anthropic import Anthropic

    class ClaudeLLM:
        def __init__(self):
            self.client = None

        def set_api_key(self, api_key):
            self.client = Anthropic(api_key=api_key)

        def prompt(self, prompt_text, model="claude-3-5-sonnet-20241022"):
            if not self.client:
                return "Error: API key not set"

            try:
                response = self.client.messages.create(
                    model=model,
                    max_tokens=1024,
                    messages=[{"role": "user", "content": prompt_text}]
                )
                return response.content[0].text
            except Exception as e:
                return f"Error: {str(e)}"

    claude_llm = ClaudeLLM()
`);
```

3. Add UI elements for Claude:

```html
<label for="provider">Provider:</label>
<select id="provider">
    <option value="openai">OpenAI</option>
    <option value="claude">Anthropic Claude</option>
</select>

<label for="claudeKey">Claude API Key:</label>
<input type="text" id="claudeKey" placeholder="sk-ant-...">
```

4. Update the `runPrompt()` function to handle both providers

### Add Conversation History

```javascript
// Add after pyodide initialization
let conversation = JSON.parse(localStorage.getItem('conversation') || '[]');

// Modify runPrompt function
async function runPrompt() {
    // ... existing code ...

    // Add message to conversation
    conversation.push({
        role: "user",
        content: prompt
    });

    // Use conversation in API call
    const result = await pyodide.runPythonAsync(`
        messages = ${JSON.stringify(conversation)}
        response = simple_llm.client.chat.completions.create(
            model="${model}",
            messages=messages
        )
        response.choices[0].message.content
    `);

    // Add assistant response
    conversation.push({
        role: "assistant",
        content: result
    });

    // Save to localStorage
    localStorage.setItem('conversation', JSON.stringify(conversation));

    // ... rest of code ...
}

// Add clear conversation button
function clearConversation() {
    conversation = [];
    localStorage.removeItem('conversation');
    addOutput('Conversation cleared.');
}
```

### Add System Prompts

```html
<label for="systemPrompt">System Prompt (Optional):</label>
<textarea id="systemPrompt" rows="2" placeholder="You are a helpful assistant..."></textarea>
```

```javascript
// In runPrompt function
const systemPrompt = document.getElementById('systemPrompt').value.trim();

let messages = [];
if (systemPrompt) {
    messages.push({
        role: "system",
        content: systemPrompt
    });
}
messages.push({
    role: "user",
    content: prompt
});

const result = await pyodide.runPythonAsync(`
    messages = ${JSON.stringify(messages)}
    response = simple_llm.client.chat.completions.create(
        model="${model}",
        messages=messages
    )
    response.choices[0].message.content
`);
```

---

## 🎯 Example Use Cases

### Research Assistant
```
Prompt: "Explain the main ideas of quantum entanglement in simple terms"
```

### Code Helper
```
Prompt: "Write a Python function to check if a string is a palindrome"
```

### Writing Assistant
```
Prompt: "Help me write a professional email requesting a meeting"
```

### Quick Lookups
```
Prompt: "What are the capitals of Scandinavian countries?"
```

### Creative Tasks
```
Prompt: "Generate 3 creative startup ideas for sustainable fashion"
```

---

## ⚙️ Configuration Options

### Web App Settings

Stored in browser localStorage:
- `openai_api_key` - Your OpenAI API key
- `conversation` - Chat history (if implemented)
- `preferred_model` - Last selected model

To clear all settings:
```javascript
// In browser console
localStorage.clear()
```

### a-Shell Configuration

Stored in `~/.profile`:
```bash
# API Keys
export OPENAI_API_KEY="sk-..."
export ANTHROPIC_API_KEY="sk-ant-..."

# Aliases
alias llm='python ~/llm_simple.py'
alias llm4='python ~/llm_simple.py -m gpt-4o'

# Default settings
export LLM_DEFAULT_MODEL="gpt-4o-mini"
```

---

## 📊 Cost Management

### OpenAI Pricing (as of 2024)

- **gpt-4o-mini**: ~$0.15 per 1M input tokens
- **gpt-4o**: ~$2.50 per 1M input tokens
- **gpt-3.5-turbo**: ~$0.50 per 1M input tokens

**Typical prompt**: 100-500 tokens
**Typical response**: 200-1000 tokens

**Example costs:**
- Simple question with gpt-4o-mini: < $0.001
- Complex task with gpt-4o: ~$0.01-0.05
- Daily casual use: $0.10-1.00

### Tips to Save Costs

1. **Use appropriate models:**
   - gpt-4o-mini for simple tasks
   - gpt-4o for complex reasoning

2. **Be concise:**
   - Shorter prompts = lower cost
   - Avoid unnecessary context

3. **Set usage limits:**
   - OpenAI dashboard → Usage limits
   - Set monthly budget cap

4. **Monitor usage:**
   - Check OpenAI dashboard regularly
   - Track spending per day/week

---

## 🐛 Common Issues

### Web App Issues

**Problem:** "Failed to load Pyodide"
- **Solution:** Check internet connection, clear cache, try again

**Problem:** "API key invalid"
- **Solution:** Verify key at https://platform.openai.com/api-keys

**Problem:** "Slow to load"
- **Solution:** Normal on first load. Wait 30-60 seconds.

**Problem:** "Works on computer but not iPhone"
- **Solution:** Ensure using Safari. Update iOS to latest version.

### a-Shell Issues

**Problem:** "pip install failed"
- **Solution:** Package has C extensions. Use simplified script.

**Problem:** "Command not found: python"
- **Solution:** Try `python3` instead of `python`

**Problem:** "ModuleNotFoundError: No module named 'openai'"
- **Solution:** Run `pip install openai` first

**Problem:** "API key not found"
- **Solution:** Run `export OPENAI_API_KEY="sk-..."` or add to `~/.profile`

---

## 📱 iOS-Specific Tips

### Shortcuts Integration

Create an iOS Shortcut to quickly prompt:

1. Open Shortcuts app
2. Create new shortcut
3. Add "Open URL" action
4. URL: Your hosted web app
5. Add to Home Screen
6. Or add "Ask for input" → Open URL with query parameter

### Voice Input

Safari supports voice input:
1. Tap microphone icon on keyboard
2. Speak your prompt
3. Tap "Run Prompt"

### Split View (iPad)

- Open web app in one side
- Open Notes or another app in other side
- Copy responses directly to Notes

### Siri Integration (Advanced)

Create Siri shortcut:
1. Shortcuts app → Automation
2. "When I say 'Ask LLM'"
3. Open your web app URL
4. Now: "Hey Siri, Ask LLM" → Opens app

---

## 🔐 Security Best Practices

1. **API Key Safety:**
   - Never share your API key
   - Don't commit keys to git
   - Rotate keys periodically

2. **Usage Monitoring:**
   - Check OpenAI usage dashboard weekly
   - Set up usage alerts
   - Monitor for unusual activity

3. **Device Security:**
   - Use passcode/Face ID on iPhone
   - Don't use on public/shared devices
   - Clear browser data if selling device

4. **Prompt Privacy:**
   - Don't send sensitive personal info
   - Remember all prompts go to OpenAI servers
   - Use Claude/local models for sensitive data

---

## 📚 Additional Resources

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Pyodide Documentation](https://pyodide.org/en/stable/)
- [a-Shell GitHub](https://github.com/holzschu/a-shell)
- [LLM CLI Original](https://github.com/simonw/llm)
- [iOS Shortcuts Guide](https://support.apple.com/guide/shortcuts/welcome/ios)

---

**Happy prompting! 🚀**
