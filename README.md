# 🤖 Yashasvi's Enhanced ChatBot

A powerful, feature-rich chatbot application built with Streamlit and powered by Groq AI. This enhanced version includes conversation memory, multiple AI models, customizable settings, and a modern UI.

## ✨ Features

### 🧠 Core Features
- **Multiple AI Models**: Choose from LLaMA 3 70B, Mixtral 8x7B, or Gemma 7B
- **Conversation Memory**: Maintains chat history for contextual conversations
- **Real-time Responses**: Fast AI responses with typing indicators
- **Export Functionality**: Download your chat history as JSON

### 🎨 User Interface
- **Modern Design**: Beautiful gradient headers and styled components
- **Responsive Layout**: Works on desktop and mobile devices
- **Interactive Sidebar**: Easy access to settings and statistics
- **Visual Feedback**: Typing indicators and response time display

### ⚙️ Customization
- **Temperature Control**: Adjust AI creativity (0.0 - 2.0)
- **Response Length**: Set maximum token limit (50 - 4000)
- **Model Selection**: Switch between different AI models
- **Chat Management**: Clear history and export conversations

### 🛡️ Error Handling
- **API Validation**: Checks for valid API keys
- **Connection Monitoring**: Handles network issues gracefully
- **User Guidance**: Provides troubleshooting tips
- **Graceful Degradation**: Informative error messages

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Groq API key (get one at [console.groq.com](https://console.groq.com))

### Installation

1. **Clone or download the project**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   - Copy your `.env` file and ensure it contains:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

4. **Run the application**:
   ```bash
   streamlit run ChatBot.py
   ```

The application will open in your browser at `http://localhost:8501`

## 📁 Project Structure

```
ML Interniship/
├── ChatBot.py              # Enhanced chatbot application
├── requirements.txt        # Python dependencies
├── .env                   # Environment variables (API key)
├── README.md              # This documentation
├── basic.py               # Basic Python exercises
├── face_detection.py      # Face detection script
├── face_detection_video.py # Video face detection
├── filter_image.py        # Image filtering
├── image_open.py          # Image operations
├── automation/            # Automation scripts
│   ├── automate.py
│   ├── whatsapp_auto.py
│   └── yt_auto.py
└── images/               # Sample images
    ├── group.png
    └── image.png
```

## 🎯 Usage Guide

### Starting a Conversation
1. Open the application in your browser
2. Type your message in the chat input box
3. Press Enter or click the send button
4. The AI will respond with a thoughtful answer

### Customizing Settings
- **Model Selection**: Choose different AI models from the sidebar
- **Temperature**: Lower values (0.0-0.3) for factual responses, higher values (1.0-2.0) for creative responses
- **Max Tokens**: Control the maximum length of AI responses

### Managing Your Chat
- **Clear History**: Remove all previous conversations
- **Export Chat**: Download your conversation history as a JSON file
- **Statistics**: Track message count and chat history length

## 🔧 Technical Details

### API Configuration
- Uses Groq's high-performance inference API
- Supports streaming and non-streaming responses
- Automatic retry logic for failed requests
- Response time tracking and optimization

### Session Management
- Persistent chat history using Streamlit session state
- Context awareness with last 5 conversation exchanges
- Memory-efficient message handling
- Automatic cleanup on session end

### Error Handling
- Comprehensive exception handling
- User-friendly error messages
- Automatic recovery suggestions
- Network connectivity checks

## 🎨 UI Components

### Header Section
- Gradient background with modern styling
- Application title and description
- Responsive design for all screen sizes

### Sidebar Controls
- Model selection dropdown
- Temperature and token sliders
- Real-time statistics display
- Action buttons for chat management

### Chat Interface
- Message bubbles with user/assistant avatars
- Typing indicators during processing
- Response time information
- Scrollable conversation history

## 📊 Available Models

| Model | Description | Use Case |
|-------|-------------|----------|
| LLaMA 3 70B | High-performance general model | Most conversations |
| Mixtral 8x7B | Fast, efficient model | Quick responses |
| Gemma 7B | Lightweight model | Simple queries |

## 🔒 Security

- API keys stored in environment variables
- No sensitive data in source code
- Secure API communication
- Local data processing only

## 🐛 Troubleshooting

### Common Issues

1. **API Key Error**
   - Ensure your `.env` file contains a valid Groq API key
   - Check that the API key has sufficient credits

2. **Connection Issues**
   - Verify your internet connection
   - Try selecting a different model
   - Check Groq service status

3. **Slow Responses**
   - Reduce max tokens setting
   - Try a faster model (Mixtral or Gemma)
   - Check network latency

### Performance Tips
- Use LLaMA 3 for best quality
- Use Mixtral for balanced speed/quality
- Lower temperature for faster responses
- Limit conversation history for better performance

## 🚀 Future Enhancements

- [ ] Voice input/output support
- [ ] File upload capabilities
- [ ] Multiple conversation threads
- [ ] Custom prompt templates
- [ ] Integration with other AI providers
- [ ] Advanced analytics dashboard
- [ ] User authentication system

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue for any bugs or feature requests.

## 📞 Support

For support or questions:
- Check the troubleshooting section above
- Review Groq API documentation
- Open an issue in the project repository

---

**Built with ❤️ using Streamlit and Groq AI**
