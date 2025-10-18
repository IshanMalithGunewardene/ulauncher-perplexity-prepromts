# 🔍 Perplexity Preprompts Extension for Ulauncher

> ⚡ Search Perplexity AI with custom preprompts directly from your Ulauncher interface!

This powerful Ulauncher extension allows you to quickly search Perplexity AI with or without premade prompts, all without leaving your keyboard.

---

## ✨ Features

- 🚀 **Quick Search**: Search Perplexity AI without opening a browser first
- 📝 **Custom Preprompts**: Combine premade prompts with your queries
- 🎯 **Smart Detection**: Automatically detects and uses preprompt files
- 🔄 **Fallback Mode**: Works as a regular search if no preprompt is found
- ⌨️ **Keyboard-Friendly**: Stay productive without touching your mouse

---

## 📦 Installation

### Method 1: Via GitHub URL
1. 🎛️ Open Ulauncher preferences
2. 📑 Go to "Extensions" tab
3. ➕ Click "Add extension"
4. 🔗 Paste the following URL:
   ```
   https://github.com/IshanMalithGunewardene/ulauncher-perplexity-prepromts
   ```

### Method 2: Manual Installation
1. 📂 Clone this repository to your Ulauncher extensions folder:
   ```bash
   cd ~/.local/share/ulauncher/extensions/
   git clone https://github.com/IshanMalithGunewardene/ulauncher-perplexity-prepromts
   ```
2. 🔄 Restart Ulauncher

---

## 🎯 Usage

### 🔰 Basic Usage

1. ⌨️ Open Ulauncher (usually `Ctrl+Space`)
2. 💬 Type `px` (the default keyword) followed by your search query
3. ↩️ Press Enter to open the search results in Perplexity AI

**Example:**
```
px what is quantum computing
```

---

### 🎨 Using Preprompts (The Power Feature!)

Preprompts allow you to create reusable prompt templates that get combined with your custom queries.

#### 📖 How It Works

1. 📄 Create a file in the `prepromts/` folder with your preprompt text
2. ⌨️ In Ulauncher, type: `px [preprompt-name] [your custom query]`
3. 🔗 The extension combines the preprompt with your query and searches Perplexity AI

#### 🌟 Example Workflow

**Step 1:** Create a preprompt file at `prepromts/doc`
```
you need only use refernce of devdoc and offical programing language defualt doc and give me explanation using only those and here my concept to i need learn :
```

**Step 2:** Use it in Ulauncher
```
px doc react useStates
```

**Step 3:** The Result
Perplexity AI opens with the combined query:
```
you need only use refernce of devdoc and offical programing language defualt doc and give me explanation using only those and here my concept to i need learn : react useStates
```

---

### 🛠️ Creating Your Own Preprompts

1. 📁 Navigate to the `prepromts/` folder in the extension directory
2. 📝 Create a new text file with your desired keyword name
   - Example: `explain`, `summarize`, `code`, `debug`, etc.
3. ✍️ Write your preprompt text in the file
4. 💾 Save the file
5. 🎉 Use it immediately in Ulauncher: `px [your-preprompt-name] [custom query]`

#### 💡 Preprompt Ideas

Here are some useful preprompts you can create:

**`prepromts/explain`**
```
Explain the following concept in simple terms with examples:
```
Usage: `px explain async/await in JavaScript`

**`prepromts/code`**
```
Provide a code example with detailed comments for:
```
Usage: `px code binary search algorithm`

**`prepromts/debug`**
```
Help me debug this issue and suggest solutions:
```
Usage: `px debug TypeScript type error`

**`prepromts/eli5`**
```
Explain like I'm 5 years old:
```
Usage: `px eli5 blockchain technology`

**`prepromts/compare`**
```
Compare and contrast the following technologies with pros and cons:
```
Usage: `px compare React vs Vue`

---

### 🔄 Fallback Behavior

If the first word after `px` doesn't match any preprompt file, the extension intelligently falls back to using your entire query as a regular Perplexity AI search. This means you never lose functionality!

**Example:**
```
px what is machine learning
```
→ Searches for "what is machine learning" (no preprompt applied)

---

## 📋 Requirements

- 🖥️ **Ulauncher** 5.0+
- 🐍 **Python** 3.5+
- 📚 **Dependencies**: All included with Python standard library

---

## 📂 Project Structure

```
ulauncher-perplexity-prepromts/
├── 📄 main.py              # Main extension code
├── 📄 manifest.json        # Extension manifest
├── 📄 readme.md           # This file
├── 📁 images/             # Extension icons
│   └── 🖼️ icon.png
├── 📁 prepromts/          # Your custom preprompts folder
│   ├── 📝 doc             # Documentation preprompt
│   └── 📝 explain         # Explanation preprompt
└── 📄 versions.json       # Version information
```

---

## 🎓 Tips & Tricks

- 💡 **Tip 1**: Keep preprompt names short and memorable (e.g., `doc`, `exp`, `code`)
- 💡 **Tip 2**: End your preprompts with a colon or appropriate punctuation for natural flow
- 💡 **Tip 3**: Create preprompts for your most common search patterns
- 💡 **Tip 4**: Share useful preprompts with your team by committing them to version control
- 💡 **Tip 5**: Test your preprompts by checking the generated Perplexity URL

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/amazing-feature`)
3. 💻 Make your changes
4. ✅ Test your changes thoroughly
5. 📤 Commit your changes (`git commit -m 'Add amazing feature'`)
6. 📮 Push to the branch (`git push origin feature/amazing-feature`)
7. 🎉 Open a Pull Request

---

## 🐛 Troubleshooting

### Preprompt not working?
- ✅ Check that the preprompt file exists in the `prepromts/` folder
- ✅ Verify the filename matches exactly what you're typing (case-sensitive)
- ✅ Ensure the preprompt file has read permissions

### Extension not loading?
- ✅ Restart Ulauncher
- ✅ Check Python version compatibility
- ✅ Verify the extension is enabled in Ulauncher preferences

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- 🎉 Original extension by Igor Varyvoda
- 🧠 Powered by Perplexity AI
- 🚀 Built for the Ulauncher community

---

<div align="center">

### ⭐ If you find this extension helpful, consider giving it a star!

**Made with ❤️ for productivity enthusiasts**

</div>
