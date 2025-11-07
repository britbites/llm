# GitHub Pages Setup Instructions

Since CDNs are having issues with the branch name and serving HTML,
here's how to set up GitHub Pages for permanent hosting:

## On iPhone (GitHub.com):

1. Go to: https://github.com/britbites/llm/settings/pages

2. Under "Source":
   - Select "Deploy from a branch"

3. Under "Branch":
   - Select: `claude/llm-iphone-wasm-011CUsw28xwSQcZkArSvBqgP`
   - Folder: `/ (root)`
   - Click "Save"

4. Wait 2-3 minutes

5. Access at:
   https://britbites.github.io/llm/llm-multi-provider.html

This gives you a permanent, working URL!

## Alternative: Use Commit Hash URLs

If GitHub Pages doesn't work with the branch name, use:

**rawgithack (serves proper HTML):**
https://raw.githack.com/britbites/llm/abe68ec/llm-multi-provider.html

**jsDelivr:**
https://cdn.jsdelivr.net/gh/britbites/llm@abe68ec/llm-multi-provider.html
