# LLM CLI for iPhone

Run [Simon Willison's LLM tool](https://github.com/simonw/llm) on your iPhone using WebAssembly (Pyodide) or a-Shell app.

## 🎯 Overview

This project provides **two ways** to run the LLM CLI tool on iPhone:

1. **🌐 WebAssembly/Pyodide (Recommended)** - Run in Safari browser with no app installation required
2. **📱 a-Shell App** - Run in a native iOS terminal emulator

## 🌐 Method 1: WebAssembly (Pyodide) - Recommended

### Why This Approach?

- ✅ Works in Safari on iPhone (iOS compatibility fixed in 2025)
- ✅ No app installation required
- ✅ Full support for Pydantic 2.10.5, SQLite, and all dependencies
- ✅ Can be saved as a web app to home screen
- ✅ Works offline after initial load (except API calls)
- ✅ More portable and easier to update

### Setup Instructions

1. **Open the web interface:**
   - Host `llm-iphone.html` on any web server, OR
   - Open the file directly in Safari from iCloud Drive/Files app

2. **Add to Home Screen (Optional but recommended):**
   - Open `llm-iphone.html` in Safari
   - Tap the Share button (square with arrow)
   - Select "Add to Home Screen"
   - Name it "LLM CLI" and tap Add
   - Now you have a full-screen app!

3. **Configure your API key:**
   - Open the app
   - Enter your OpenAI API key (get one at https://platform.openai.com/api-keys)
   - Your key is stored locally in browser storage only

4. **Start prompting:**
   - Enter your prompt in the text area
   - Select your preferred model
   - Tap "Run Prompt"
   - Wait for the response!

### Features

- 🤖 Works with OpenAI models (GPT-4, GPT-4o, GPT-3.5-turbo, etc.)
- 💾 API key stored locally (localStorage)
- 🎨 Terminal-style dark interface
- 📱 Mobile-optimized and responsive
- ⚡ Fast after initial load (~30-60 seconds first time)

### Extending to Other LLM Providers

The current implementation uses OpenAI, but you can easily extend it to support:

- **Anthropic Claude** - Modify the Python code to use the `anthropic` package
- **Google Gemini** - Use `google-generativeai` package
- **Local models** - Would require additional backend server (not possible in pure browser)

### Limitations

- ❌ No local model support (only API-based models)
- ❌ No persistent conversation history (yet)
- ❌ First load takes 30-60 seconds to download Pyodide + packages
- ⚠️ Large responses may be slower than desktop

---

## 📱 Method 2: a-Shell App

### Why This Approach?

- ✅ Native iOS terminal environment
- ✅ Full Python 3.11+ support
- ✅ Can install pure Python packages via pip
- ✅ Supports multiple windows
- ✅ Works completely offline

### Setup Instructions

1. **Install a-Shell:**
   - Download from App Store: https://apps.apple.com/us/app/a-shell/id1473805438
   - Free and open source

2. **Install Python packages:**
   ```bash
   pip install click
   pip install openai
   pip install python-ulid
   pip install pluggy
   pip install PyYAML
   ```

3. **Try installing dependencies:**
   ```bash
   # These might work (pure Python)
   pip install click-default-group
   pip install condense-json

   # These might fail (have C extensions)
   pip install pydantic  # May fail due to C extensions
   pip install sqlite-utils  # May fail due to C extensions
   ```

4. **Install LLM (if dependencies work):**
   ```bash
   pip install llm
   ```

5. **Configure API key:**
   ```bash
   # Set OpenAI API key
   export OPENAI_API_KEY="sk-your-key-here"

   # Or for persistence, add to ~/.profile
   echo 'export OPENAI_API_KEY="sk-your-key-here"' >> ~/.profile
   ```

6. **Use LLM:**
   ```bash
   llm "What is the capital of France?"
   llm -m gpt-4o "Explain quantum computing"
   ```

### Limitations

- ⚠️ Some packages with C extensions may not install
- ⚠️ Pydantic might not work (has C extensions in v2)
- ⚠️ sqlite-utils might not work fully
- ⚠️ Requires manual package installation
- ❌ No pre-built binary wheels for iOS

### Alternative: Simplified a-Shell Script

If the full LLM package doesn't work due to dependencies, use this simplified script:

```python
# save as llm_simple.py
import sys
from openai import OpenAI

def main():
    if len(sys.argv) < 2:
        print("Usage: python llm_simple.py 'your prompt here'")
        return

    # Get API key from environment
    import os
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("Error: OPENAI_API_KEY not set")
        return

    # Create client
    client = OpenAI(api_key=api_key)

    # Get prompt from args
    prompt = ' '.join(sys.argv[1:])

    # Send request
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    # Print response
    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
```

Usage:
```bash
python llm_simple.py "What is the capital of France?"
```

---

## 📊 Comparison

| Feature | Pyodide/WebAssembly | a-Shell |
|---------|---------------------|---------|
| Installation | None (just open in browser) | App Store install required |
| Package Support | Excellent (Pydantic, SQLite, etc.) | Limited (pure Python only) |
| First Load Time | 30-60 seconds | Instant |
| Offline Support | After first load | Full offline |
| Native Feel | Web app | Native terminal |
| Updates | Just reload page | Manual pip updates |
| LLM Package | ⚠️ Custom wrapper | ❓ May or may not work |
| **Recommended?** | ✅ **YES** | ⚠️ If you need terminal |

---

## 🚀 Quick Start (Pyodide)

1. Open `llm-iphone.html` in Safari
2. Enter OpenAI API key
3. Type a prompt
4. Tap "Run Prompt"
5. Done! 🎉

---

## 🔧 Technical Details

### Pyodide Implementation

The `llm-iphone.html` file includes:

- **Pyodide 0.26.4** - Python WebAssembly runtime
- **OpenAI Python SDK** - For API calls
- **Pydantic, Click, SQLite** - Core dependencies
- **Custom SimpleLLM wrapper** - Minimal interface for prompting

### How It Works

1. Loads Pyodide runtime (~15MB)
2. Installs Python packages via micropip
3. Creates a Python interface for LLM functionality
4. JavaScript handles UI and calls Python functions
5. Responses displayed in terminal-style interface

### Why Not Full LLM Package?

The full LLM CLI has many features (plugins, embeddings, logging) that add complexity. For iPhone use, a simplified interface focused on prompting is more practical and loads faster.

However, you can extend the implementation to include:
- Conversation history/logging
- Multiple provider support (Anthropic, Gemini, etc.)
- Embeddings generation
- Custom system prompts
- Temperature/parameter controls

---

## 🎨 Customization

### Add Anthropic Claude Support

```javascript
// In the Python code, add:
await pyodide.runPythonAsync(`
    await micropip.install('anthropic')
    from anthropic import Anthropic

    def claude_prompt(api_key, prompt_text, model="claude-3-5-sonnet-20241022"):
        client = Anthropic(api_key=api_key)
        response = client.messages.create(
            model=model,
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt_text}]
        )
        return response.content[0].text
`);
```

### Add Conversation History

```javascript
// Store messages in localStorage
let conversation = JSON.parse(localStorage.getItem('conversation') || '[]');

// Modify prompt function to include history
const result = await pyodide.runPythonAsync(`
    messages = ${JSON.stringify(conversation)}
    messages.append({"role": "user", "content": '''${prompt}'''})

    response = simple_llm.client.chat.completions.create(
        model="${model}",
        messages=messages
    )
    response.choices[0].message.content
`);

conversation.push({"role": "user", "content": prompt});
conversation.push({"role": "assistant", "content": result});
localStorage.setItem('conversation', JSON.stringify(conversation));
```

---

## 📝 License

This implementation is provided as-is for running Simon Willison's LLM tool on iPhone.

- Original LLM tool: https://github.com/simonw/llm (Apache 2.0 License)
- Pyodide: https://github.com/pyodide/pyodide (Mozilla Public License 2.0)
- a-Shell: https://github.com/holzschu/a-shell (BSD 3-Clause License)

---

## 🤝 Contributing

Improvements welcome! Some ideas:

- [ ] Add more LLM providers (Anthropic, Gemini, etc.)
- [ ] Implement conversation history
- [ ] Add SQLite logging like original LLM tool
- [ ] Support for embeddings
- [ ] Plugin system
- [ ] Better error handling
- [ ] Streaming responses
- [ ] Voice input support
- [ ] Shortcuts integration

---

## ⚠️ Security Note

Your API keys are stored in browser localStorage and never sent anywhere except directly to the LLM provider (OpenAI, Anthropic, etc.). The app runs entirely client-side with no backend server.

For maximum security:
- Don't use this on shared devices
- Clear browser data to remove stored keys
- Use API keys with usage limits
- Monitor your API usage

---

## 🐛 Troubleshooting

### "Failed to load Pyodide"
- Check internet connection (needed for first load)
- Try a different browser (Safari recommended)
- Clear browser cache and reload

### "Error: API key not set"
- Make sure you've entered your API key
- Check that the key starts with "sk-"
- Verify the key is valid at OpenAI dashboard

### "Initialization takes too long"
- First load downloads ~20-30MB of packages
- Subsequent loads are much faster (cached)
- Be patient for 30-60 seconds on first load

### a-Shell: "pip install failed"
- Package likely has C extensions
- Try pure Python alternatives
- Use the simplified script instead

---

## 📚 Resources

- [Simon Willison's LLM](https://github.com/simonw/llm)
- [Pyodide Documentation](https://pyodide.org/)
- [a-Shell App](https://holzschu.github.io/a-Shell_iOS/)
- [OpenAI API](https://platform.openai.com/)
- [Anthropic API](https://www.anthropic.com/api)

---

**Made with ❤️ for iPhone users who want LLM access anywhere**
