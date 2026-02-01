# Suruchi's Kitchen - OpenAI ChatKit Production Demo

A complete production-ready restaurant website showcasing OpenAI Agent Builder integration with ChatKit for enhanced customer experience.

## 🎯 Project Overview

This project demonstrates a live implementation of:
- **OpenAI Agent Builder**: Custom agent workflow for restaurant operations
- **ChatKit Integration**: Embedded AI chat interface for customer interaction
- **Production Deployment**: Real-world F&B industry use case

## 🏗️ Architecture

```
┌─────────────────┐
│   Frontend      │
│  (HTML + JS)    │
│   ChatKit UI    │
└────────┬────────┘
         │
         ↓ HTTP
┌─────────────────┐
│  Backend API    │
│   (FastAPI)     │
└────────┬────────┘
         │
         ↓ Session Creation
┌─────────────────┐
│  OpenAI Agent   │
│    Builder      │
│  (Your Agent)   │
└─────────────────┘
```

## 📋 Prerequisites

- Python 3.8 or higher
- Node.js (for serving static files, optional)
- OpenAI API Key
- Agent Builder Workflow ID

## 🚀 Quick Start

### 1. Clone and Navigate

```bash
cd nisargs-kitchen
```

### 2. Set Up Environment Variables

Create a `.env` file from the template:

```bash
cp .env.example .env
```

Edit `.env` and add your credentials:

```env
OPENAI_API_KEY=sk-proj-your-actual-api-key-here
WORKFLOW_ID=wf_694817bace748190857ed8ad2f86b6730df6a376fb67bef8
WORKFLOW_VERSION=3
```

### 3. Install Python Dependencies

```bash
# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 4. Start the Backend Server

```bash
python server.py
```

The backend will start at `http://localhost:8000`

You should see:
```
INFO:     Started server process
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### 5. Serve the Frontend

Open a new terminal and serve the static files:

**Option A: Using Python's built-in server**
```bash
cd public
python -m http.server 3000
```

**Option B: Using Node.js http-server**
```bash
# Install globally if you haven't
npm install -g http-server

# Serve from public directory
cd public
http-server -p 3000
```

**Option C: Using VS Code Live Server Extension**
- Install "Live Server" extension in VS Code
- Right-click on `public/index.html`
- Select "Open with Live Server"

### 6. Access the Website

Open your browser and navigate to:
```
http://localhost:3000
```

## 🧪 Testing the Integration

1. **Health Check**: Visit `http://localhost:8000/health` to verify backend is running
2. **Session Creation**: The backend should successfully create ChatKit sessions
3. **Chat Interaction**: Try the AI assistant on the website
4. **Sample Prompts**: Click on starter prompts or ask custom questions

## 📁 Project Structure

```
nisargs-kitchen/
├── server.py              # FastAPI backend for ChatKit sessions
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .env                  # Your actual environment variables (git-ignored)
├── README.md             # This file
└── public/
    ├── index.html        # Main website
    └── chatkit-init.js   # ChatKit initialization script
```

## 🎨 Features

### Restaurant Website
- **Responsive Design**: Mobile-friendly layout
- **Hero Section**: Eye-catching landing page
- **Menu Preview**: Featured dishes display
- **About Section**: Restaurant story and vision

### AI Assistant (ChatKit)
- **Live Chat Interface**: Real-time conversation with AI
- **Starter Prompts**: Quick access to common queries
- **File Attachments**: Support for image and PDF uploads
- **Custom Theming**: Matches restaurant brand colors
- **Conversation History**: Thread management

### Backend Features
- **Session Management**: Secure ChatKit session creation
- **CORS Support**: Enabled for local development
- **Error Handling**: Comprehensive error logging
- **Environment Configuration**: Secure credential management

## 🔧 Customization

### Modify Restaurant Branding

Edit `public/index.html`:
- Change restaurant name, colors, and content
- Update menu items and pricing
- Modify hero image and sections

### Customize ChatKit Appearance

Edit `public/chatkit-init.js`:
```javascript
theme: {
    colorScheme: 'light', // or 'dark'
    color: {
        accent: {
            primary: '#d4af37', // Your brand color
        }
    },
    radius: 'round', // or 'sharp', 'pill'
}
```

### Update Starter Prompts

Modify the `prompts` array in `chatkit-init.js`:
```javascript
prompts: [
    {
        icon: 'sparkles',
        name: 'Your Prompt Name',
        prompt: 'Your prompt text here'
    }
]
```

## 🐛 Troubleshooting

### ChatKit Not Loading
- Ensure backend server is running on port 8000
- Check browser console for errors
- Verify OPENAI_API_KEY in .env file
- Confirm WORKFLOW_ID is correct

### CORS Errors
- Backend includes CORS middleware for localhost:3000
- If using different port, update `allow_origins` in server.py

### Session Creation Fails
- Verify OpenAI API key is valid
- Check workflow ID and version are correct
- Review backend logs for detailed error messages

### Module Import Errors
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt` again

## 📊 Production Deployment

### Backend Deployment Options

1. **Railway/Render/Fly.io**
   - Push code to GitHub
   - Connect repository
   - Set environment variables
   - Deploy

2. **AWS/Azure/GCP**
   - Use container services (ECS, App Service, Cloud Run)
   - Deploy as Docker container
   - Configure environment variables

3. **DigitalOcean App Platform**
   - Connect GitHub repository
   - Configure build/run commands
   - Set environment variables

### Frontend Deployment Options

1. **Vercel/Netlify**
   - Deploy `public` directory
   - Configure environment variables for API URL

2. **AWS S3 + CloudFront**
   - Upload static files to S3
   - Serve via CloudFront CDN

3. **GitHub Pages**
   - Push to gh-pages branch
   - Update API URL to production backend

### Environment Variables for Production

Update `chatkit-init.js` to use environment-based URLs:
```javascript
const BACKEND_URL = process.env.BACKEND_URL || 'http://localhost:8000';
```

## 🔒 Security Considerations

- Never commit `.env` file to version control
- Use environment variables for all secrets
- Implement rate limiting for production
- Add authentication if needed
- Use HTTPS in production
- Validate user inputs on backend

## 📚 Additional Resources

- [OpenAI ChatKit Documentation](https://platform.openai.com/docs/chatkit)
- [Agent Builder Guide](https://platform.openai.com/docs/agent-builder)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

## 👨‍💼 About

**Project**: Nisarg's Kitchen AI Demo
**Purpose**: Production demonstration of OpenAI Agent Builder with ChatKit
**Industry**: Food & Beverage
**Technology**: OpenAI Agent Builder, ChatKit, FastAPI, HTML/CSS/JavaScript

## 📝 License

This is a demonstration project for educational and portfolio purposes.

## 🤝 Support

For issues or questions:
1. Check the troubleshooting section
2. Review backend logs
3. Consult OpenAI ChatKit documentation
4. Check browser console for frontend errors

---

**Built with ❤️ using OpenAI Agent Builder & ChatKit**
