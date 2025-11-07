# Multi-Provider LLM Web App Guide

## 🚀 Quick Start

The `llm-multi-provider.html` file gives you access to **three major LLM providers** from your iPhone:
1. **OpenAI** (GPT-4o, GPT-4, o1, etc.)
2. **Anthropic** (Claude 3.5 Sonnet, Claude 3 Opus, etc.)
3. **Google** (Gemini 2.0, Gemini 1.5 Pro, etc.)

## 📱 How to Access on iPhone

### Option 1: GitHub Pages (Best for Long-Term Use)

1. **Enable GitHub Pages:**
   - Go to repository settings: `https://github.com/[username]/llm/settings/pages`
   - Source: "Deploy from a branch"
   - Branch: `claude/llm-iphone-wasm-011CUsw28xwSQcZkArSvBqgP`
   - Folder: `/ (root)`
   - Save

2. **Access the app:**
   ```
   https://[username].github.io/llm/llm-multi-provider.html
   ```

3. **Add to Home Screen for app-like experience**

### Option 2: HTML Preview (Instant Access)

Open in Safari on iPhone:
```
https://htmlpreview.github.io/?https://github.com/[username]/llm/blob/claude/llm-iphone-wasm-011CUsw28xwSQcZkArSvBqgP/llm-multi-provider.html
```

### Option 3: iCloud Drive (Most Private)

1. Download `llm-multi-provider.html` to your computer
2. Upload to iCloud Drive
3. Open Files app on iPhone
4. Tap the file → Opens in Safari
5. Add to Home Screen

## 🔑 Getting API Keys

### OpenAI
1. Go to https://platform.openai.com/api-keys
2. Click "Create new secret key"
3. Copy the key (starts with `sk-`)
4. Paste into OpenAI tab in the app

**Cost:** ~$0.10-$1.00 per day for moderate use
- gpt-4o-mini: Cheapest (~$0.15 per 1M tokens)
- gpt-4o: Most capable (~$2.50 per 1M tokens)

### Anthropic Claude
1. Go to https://console.anthropic.com/settings/keys
2. Create new API key
3. Copy the key (starts with `sk-ant-`)
4. Paste into Anthropic tab in the app

**Cost:** ~$0.50-$2.00 per day for moderate use
- Claude 3.5 Haiku: Fastest (~$1 per 1M tokens)
- Claude 3.5 Sonnet: Best balance (~$3 per 1M tokens)
- Claude 3 Opus: Most capable (~$15 per 1M tokens)

### Google Gemini
1. Go to https://aistudio.google.com/app/apikey
2. Create new API key
3. Copy the key (starts with `AIza`)
4. Paste into Gemini tab in the app

**Cost:** FREE tier available!
- Gemini 1.5 Flash: Free (with rate limits)
- Gemini 1.5 Pro: Free (with rate limits)
- Gemini 2.0 Flash: Free experimental

## 🎯 Using the App

### First Time Setup

1. **Open the app** (wait 30-60 seconds for first load)
2. **Click the provider tab** you want to use
3. **Enter your API key** for that provider
4. **Select a model** from the dropdown
5. **Enter a prompt** and tap "Run Prompt"

### Switching Providers

Just click a different tab! Your API keys are saved automatically.

**Example workflow:**
- Use **Gemini** for quick questions (free!)
- Use **GPT-4o-mini** for coding help (cheap)
- Use **Claude 3.5 Sonnet** for long-form writing (best)
- Use **o1** for complex reasoning (most advanced)

### Model Recommendations

**For general questions:**
- Gemini 1.5 Flash (free, fast)
- gpt-4o-mini (cheap, good)

**For coding:**
- Claude 3.5 Sonnet (excellent at code)
- gpt-4o (very good)

**For creative writing:**
- Claude 3.5 Sonnet (natural, coherent)
- gpt-4o (creative)

**For complex reasoning:**
- o1 (best for math, logic)
- Claude 3 Opus (deep thinking)

**For speed:**
- Gemini 1.5 Flash
- Claude 3.5 Haiku
- gpt-4o-mini

## 🔒 Security & Privacy

### Where Are Your API Keys Stored?

- **In your iPhone's browser localStorage**
- **Never sent anywhere except to the LLM provider**
- **Not visible in the HTML file**
- **Not sent to GitHub or any server**

### What Do the Providers See?

**All three providers (OpenAI, Anthropic, Google) see:**
- Your prompts
- Your responses
- IP address
- Usage patterns

**Privacy policies:**
- **Anthropic**: Better privacy (no training on your data by default)
- **OpenAI**: 30-day retention, opt-out available
- **Google**: Check their privacy policy

### Best Practices

1. **Don't enter sensitive personal info** in prompts
2. **Use different API keys for different devices** (easy to revoke)
3. **Monitor usage** on provider dashboards
4. **Set spending limits** on each platform
5. **Clear browser data** if you sell/give away device

## ⚙️ Advanced Features

### Want Conversation History?

The app currently doesn't save conversation history. Each prompt is independent.

**To add history**, I can implement:
- localStorage-based history (simple)
- SQLite-based history (like desktop LLM)
- Export/import conversations

Let me know if you want this feature!

### Want System Prompts?

Currently not implemented, but easy to add:
- A text area for system prompt
- Applied to all conversations
- Saved per provider

### Want to Compare Responses?

Could add a "Compare" mode:
- Send same prompt to multiple providers
- See responses side-by-side
- Compare speed, quality, cost

## 📊 Cost Comparison

For 100 typical prompts (~500 tokens each):

| Provider | Model | Approximate Cost |
|----------|-------|------------------|
| Google | Gemini 1.5 Flash | **FREE** |
| OpenAI | gpt-4o-mini | ~$0.08 |
| OpenAI | gpt-4o | ~$1.25 |
| Anthropic | Claude 3.5 Haiku | ~$0.05 |
| Anthropic | Claude 3.5 Sonnet | ~$0.15 |
| Anthropic | Claude 3 Opus | ~$0.75 |
| OpenAI | o1-mini | ~$0.30 |
| OpenAI | o1 | ~$1.50 |

**Strategy for saving money:**
1. Use Gemini for simple questions (free!)
2. Use mini/haiku models for most tasks (cheap)
3. Use premium models only when needed (best quality)

## 🐛 Troubleshooting

### "Failed to initialize Pyodide"
- **Check internet connection** (needed for first load)
- **Wait 60 seconds** (downloads Python packages)
- **Clear browser cache** and try again
- **Try different browser** (Safari recommended)

### "Error: API key not set"
- **Enter API key** in the active provider tab
- **Check key is correct** (starts with sk-, sk-ant-, or AIza)
- **Verify key is active** on provider dashboard

### "Error: Invalid API key"
- **Key might be expired** - create a new one
- **Key might be restricted** - check API key settings
- **Account might be out of credits** - add payment method

### "Anthropic error: Rate limit"
- **Wait a few seconds** and try again
- **Upgrade to paid tier** for higher limits
- **Use different provider** temporarily

### "Gemini error: API not enabled"
- **Enable Gemini API** in Google Cloud Console
- **Accept terms of service**
- **Wait a few minutes** for activation

### "Response is cut off"
- **Hit token limit** for that model
- **Try asking for shorter response**
- **Use model with higher token limit** (e.g., Claude 3.5 Sonnet)

## 💡 Tips & Tricks

### Add to Home Screen
Tap Share → "Add to Home Screen" for app-like experience:
- Full-screen mode
- No browser UI
- Fast access
- Custom icon

### Voice Input
Use iPhone's built-in dictation:
1. Tap microphone on keyboard
2. Speak your prompt
3. Tap "Run Prompt"

### Copy Responses
Long-press on output → Select All → Copy
Paste into Notes, Messages, etc.

### Quick Provider Switching
API keys are saved automatically, so you can:
- OpenAI tab for coding question
- Gemini tab for quick fact check
- Claude tab for writing help
All without re-entering keys!

### Offline Usage
After first load, the app works offline for:
- Interface (works)
- Previous responses (if not cleared)
- New prompts (won't work - needs internet for API)

## 🔄 Updating the App

**If hosted on GitHub Pages:**
- Just reload the page to get latest version
- Changes appear after ~2 minutes

**If using iCloud file:**
- Download new version
- Replace old file
- Reopen in Safari

**Your settings persist:**
- API keys are saved in browser
- Don't need to re-enter after update

## 🆚 Comparison with Desktop LLM

| Feature | Multi-Provider Web | Desktop LLM CLI |
|---------|-------------------|-----------------|
| **Providers** | 3 (manual) | 50+ (via plugins) |
| **Installation** | None | pip install |
| **Conversation logs** | ❌ Not yet | ✅ SQLite |
| **Templates** | ❌ Not yet | ✅ Built-in |
| **Embeddings** | ❌ No | ✅ Yes |
| **Works on iPhone** | ✅ Yes | ❌ No |
| **Easy to update** | ✅ Reload page | pip upgrade |
| **Plugin system** | ❌ No | ✅ Yes |
| **Cost** | Free | Free |

**Use web app for:** Quick mobile access
**Use desktop for:** Advanced features, plugins, logging

## 🤝 Contributing

Want to add features? You can:

1. **Fork the repo**
2. **Edit `llm-multi-provider.html`**
3. **Test your changes**
4. **Submit a pull request**

**Ideas for contributions:**
- Add conversation history
- Add system prompts
- Add response comparison mode
- Add export functionality
- Add streaming responses
- Add image support (for GPT-4o, Claude 3.5, Gemini)
- Add cost tracking
- Add usage statistics

## 📚 Resources

- [OpenAI API Docs](https://platform.openai.com/docs)
- [Anthropic API Docs](https://docs.anthropic.com/)
- [Google Gemini API Docs](https://ai.google.dev/)
- [Pyodide Documentation](https://pyodide.org/)
- [Original LLM CLI](https://github.com/simonw/llm)

---

**Enjoy using LLM on your iPhone! 🚀**
