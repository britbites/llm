# Hypothetical Prompt That Would Create This App

## The Ideal User Prompt

Here's what a user would need to ask to get this solution built from scratch:

---

**Prompt:**

> "I want to run Simon Willison's LLM CLI tool (https://github.com/simonw/llm) on my iPhone. The tool normally runs on desktop via Python, but I need it to work in Safari on iOS without installing any apps.
>
> Requirements:
> 1. Access to OpenAI, Anthropic Claude, and Google Gemini APIs
> 2. Works entirely in the browser (no backend server)
> 3. Can be added to iPhone home screen like a native app
> 4. Saves my API keys locally (secure)
> 5. Has command history like a shell (up/down arrows to recall previous prompts)
> 6. Mobile-friendly interface optimized for touch
> 7. Works offline after initial load (at least the UI)
> 8. Handles network interruptions gracefully (auto-retry)
>
> I want it to be a single HTML file I can just open in Safari. Make it look like a terminal (dark theme, green text).
>
> Can you build this using WebAssembly/Pyodide if needed, but make it fast and reliable. I don't want to use my computer - everything should work just from my phone."

---

## Why This Prompt Would Work

### 1. **Clear Goal**
- Specific tool mentioned (LLM CLI)
- Specific platform (iPhone/Safari)
- Specific constraint (no app installation)

### 2. **Technical Requirements Specified**
- Browser-based solution
- Multiple LLM providers
- Offline capability
- Security (local storage)

### 3. **UX Requirements Clear**
- Shell-like history navigation
- Mobile-friendly
- Terminal aesthetic
- Add to home screen

### 4. **Constraints Defined**
- Single HTML file
- Phone-only workflow
- Fast and reliable

### 5. **Implicit Requirements** (AI would need to infer)
- Use Pyodide for Python runtime
- Use JavaScript fetch for API calls (not Python SDKs)
- Implement retry logic for mobile networks
- Handle localStorage for persistence
- Progressive web app patterns

---

## Alternative Minimal Prompt

If the user was less specific, here's the minimal viable prompt:

> "Build a web app for iPhone that lets me use ChatGPT, Claude, and Gemini from one interface. Make it work like a terminal with command history. Single HTML file, no server needed."

**What the AI would need to infer:**
- Use Pyodide or similar for complex features
- Direct API integration via fetch
- localStorage for state
- Mobile-first design
- Error handling for network issues

---

## What Makes a Good Prompt for Complex Projects

### Essential Elements

1. **Context:** "I want to run LLM CLI on iPhone"
   - Establishes the domain and platform

2. **Constraints:** "No app installation, browser only"
   - Narrows solution space

3. **Requirements:** "OpenAI + Claude + Gemini, history navigation"
   - Defines success criteria

4. **User Workflow:** "Everything from phone only"
   - Guides architecture decisions

5. **Quality Attributes:** "Fast, reliable, handles network issues"
   - Ensures production-ready solution

### Optional But Helpful

1. **Technical Preferences:** "Use Pyodide if needed"
   - Guides technology choices

2. **Design Preferences:** "Terminal-style, dark theme"
   - Defines aesthetic

3. **Similar Examples:** "Like Simon Willison's LLM tool"
   - Provides reference point

4. **Anti-Requirements:** "No backend server"
   - Eliminates unwanted approaches

---

## How This Prompt Differs From Typical Requests

### Typical Request:
> "Make me a chatbot app"

**Problems:**
- Too vague (which LLM? which platform?)
- No constraints (cloud? local? mobile?)
- No UX requirements (UI design undefined)
- No quality requirements (security? performance?)

### This Project's Request:
> "Run LLM CLI on iPhone, browser-only, multi-provider, with history, single file, works offline"

**Advantages:**
- Specific tool referenced (LLM CLI)
- Platform defined (iPhone/Safari)
- Architecture constrained (browser, single file)
- Features enumerated (multi-provider, history)
- Quality attributes (offline, fast)

---

## Evolution of the Prompt (What Actually Happened)

### Actual Opening Prompt:
> "find a way to run this on iphone. https://github.com/simonw/llm. eg by converting to web assembly for execution on iphone ashell app"

**What was good:**
- ✅ Specific tool (LLM CLI)
- ✅ Specific platform (iPhone)
- ✅ Technology suggestion (WebAssembly)
- ✅ Alternative approach (a-Shell)

**What was missing:**
- ⚠️ Didn't specify "browser-based" vs "app-based"
- ⚠️ Didn't mention multiple providers initially
- ⚠️ Didn't specify UX requirements (history, etc.)

### Follow-up That Refined Requirements:
> "i want to be able to access openai, gemini, anthropic models"

**This clarified:**
- Multi-provider requirement
- Scope expansion beyond original LLM CLI

### UX Enhancement Request:
> "i want to be able to edit previous prompts and re issue them like a shell"

**This added:**
- Shell-like history navigation
- Edit-and-retry workflow
- Power user feature

### Reliability Request:
> "does it retry if there are any transient network errors or network disruption"

**This added:**
- Mobile-specific requirement
- Quality of service concern
- Network resilience

---

## Lessons for Crafting Effective Prompts

### 1. Start Specific, Then Refine

**Good Pattern:**
```
Initial: "Run LLM CLI on iPhone"
Refinement: "Use OpenAI, Claude, Gemini"
Refinement: "Shell-like history navigation"
Refinement: "Auto-retry on network errors"
```

**Bad Pattern:**
```
Initial: "Make me something cool with AI"
Refinement: "Actually, can it work on my phone?"
Refinement: "Wait, I want multiple providers"
Refinement: [endless scope creep]
```

### 2. Specify Constraints Early

**Good:**
- "Browser-based, no app installation"
- "Single HTML file, no backend"
- "Phone-only workflow"

**Bad:**
- "However you think is best" (too open-ended)
- "Use the latest technologies" (no constraint)

### 3. Provide Examples or References

**Good:**
- "Like Simon Willison's LLM CLI"
- "Shell-like history (bash/zsh style)"
- "Terminal aesthetic (green on black)"

**Bad:**
- "Make it look professional" (subjective)
- "Good UX" (undefined)

### 4. Mention Quality Attributes

**Good:**
- "Fast loading (< 10 seconds)"
- "Handle network interruptions"
- "Works offline after first load"
- "Secure (local key storage)"

**Bad:**
- "Make it work well" (vague)
- "Good performance" (no metrics)

### 5. Clarify What You Don't Want

**Good:**
- "No app installation required"
- "No backend server"
- "Don't want to use my computer"

**Bad:**
- [Assumes AI knows all constraints]
- [Discovers unwanted features after implementation]

---

## Template for Similar Projects

```markdown
# Project: [Name]

## Goal
Run/build [specific tool/feature] on [platform/device]

## Context
- Currently works on: [current platform]
- Need it to work on: [target platform]
- Reference implementation: [URL or description]

## Hard Constraints
- Must: [required features]
- Must not: [prohibited approaches]
- Platform: [specific platform requirements]

## Functional Requirements
1. [Feature 1 with success criteria]
2. [Feature 2 with success criteria]
3. [Feature 3 with success criteria]

## Quality Requirements
- Performance: [specific metrics]
- Reliability: [failure handling]
- Security: [data protection needs]
- Usability: [UX expectations]

## Technical Preferences
- Technology: [suggestions, not requirements]
- Architecture: [constraints or preferences]
- Deployment: [how it should be delivered]

## User Workflow
"As a user, I want to [workflow description] without [pain points to avoid]"

## Success Criteria
The project is successful when:
1. [Measurable outcome 1]
2. [Measurable outcome 2]
3. [Measurable outcome 3]
```

---

## Comparison: Good vs. Bad Prompts

### Bad Prompt Example:
> "Build me a ChatGPT app"

**Problems:**
- No platform specified
- No constraints
- No features beyond basic chat
- No quality requirements
- "ChatGPT" is ambiguous (web interface? API?)

**Result:**
- Could be anything from a simple curl wrapper to a full web app
- AI has to guess platform (web? mobile? desktop?)
- Unclear if using official API or web scraping
- No guidance on UX, security, performance

### Good Prompt Example (This Project):
> "Build a browser-based LLM interface for iPhone that:
> - Accesses OpenAI, Claude, and Gemini via official APIs
> - Works in Safari without app installation
> - Has shell-like command history (↑/↓ navigation)
> - Stores API keys locally (secure)
> - Single HTML file for easy deployment
> - Mobile-optimized touch interface
> - Handles network interruptions (auto-retry)
> - Terminal aesthetic (dark theme)
>
> Requirements: Must work entirely from phone, no computer needed."

**Advantages:**
- Platform clear (iPhone/Safari browser)
- Constraints explicit (no app, single file, phone-only)
- Features enumerated (multi-provider, history, retry)
- Quality attributes defined (security, reliability)
- Design guidance (terminal aesthetic)
- Technology hints (API-based, not web scraping)

**Result:**
- AI knows exactly what to build
- Clear success criteria
- Minimal ambiguity
- Iterative refinement possible

---

## Key Takeaway

The difference between a mediocre solution and an excellent one often comes down to **prompt specificity**:

- ❌ "Build a chatbot" → Generic, could be anything
- ✅ "Build a browser-based multi-provider LLM interface for iPhone with shell-like history, single HTML file, works offline, handles network errors" → Specific, actionable

**The best prompts are:** Specific enough to constrain the solution space, but flexible enough to allow for technical decisions and optimizations.
