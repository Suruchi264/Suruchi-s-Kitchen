# Nisarg's Kitchen - Complete Deployment & Demo Guide

## 📦 Project Delivered

You now have a complete, production-ready restaurant website with OpenAI ChatKit integration!

---

## 🎯 What's Included

### 1. **Backend Server** (`server.py`)
- FastAPI-based REST API
- ChatKit session management
- CORS enabled for local development
- Environment variable configuration
- Error handling and logging

### 2. **Frontend Website** (`public/index.html`)
- Beautiful, responsive restaurant website
- Professional design with custom theming
- Hero section, menu preview, about section
- Embedded ChatKit widget
- Mobile-friendly layout

### 3. **ChatKit Integration** (`public/chatkit-init.js`)
- Custom configuration for restaurant branding
- Starter prompts for quick interaction
- File attachment support
- Error handling and user feedback
- Session management

### 4. **Configuration Files**
- `requirements.txt` - Python dependencies
- `.env.example` - Environment template
- `.gitignore` - Version control exclusions
- `README.md` - Comprehensive documentation
- `QUICKSTART.md` - 5-minute setup guide

### 5. **Startup Scripts**
- `start.bat` - Windows automation
- `start.sh` - Mac/Linux automation

---

## 🚀 Getting Started (VS Code)

### Step 1: Open in VS Code
```bash
# Navigate to project folder
cd nisargs-kitchen

# Open in VS Code
code .
```

### Step 2: Configure Environment
1. Locate `.env.example` file
2. Create a copy named `.env`
3. Add your OpenAI API key:
```env
OPENAI_API_KEY=sk-proj-your-actual-key-here
WORKFLOW_ID=wf_694817bace748190857ed8ad2f86b6730df6a376fb67bef8
WORKFLOW_VERSION=3
```

### Step 3: Setup Python Environment

**In VS Code Terminal:**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# Windows (CMD):
venv\Scripts\activate.bat
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 4: Start Services

**Option A: Use Startup Scripts**
```bash
# Windows:
start.bat

# Mac/Linux:
./start.sh
```

**Option B: Manual (Two Terminals)**

Terminal 1 - Backend:
```bash
python server.py
```

Terminal 2 - Frontend:
```bash
cd public
python -m http.server 3000
```

### Step 5: Access Your Website
Open browser: **http://localhost:3000**

---

## 🎬 Demo Presentation Script

### Introduction (30 seconds)
"Today I'm excited to show you a production deployment of OpenAI Agent Builder integrated with ChatKit in a real-world F&B application."

### Website Tour (1 minute)
1. **Hero Section**: "This is Nisarg's Kitchen, a modern restaurant website"
2. **Menu Preview**: "Here are some featured dishes"
3. **About Section**: "Restaurant story and mission"
4. **Scroll to AI Assistant**: "Now for the exciting part..."

### AI Assistant Demo (2-3 minutes)

**Starter Prompt #1 - Menu Recommendations**
- Click on "Menu Recommendations" starter prompt
- Watch the AI respond with personalized suggestions
- "Notice how the AI understands our menu context"

**Starter Prompt #2 - Dietary Options**
- Click on "Dietary Options"
- AI provides vegetarian/vegan information
- "This helps customers with dietary restrictions"

**Custom Query #1 - Reservation**
- Type: "I need a table for 4 people tonight at 7 PM"
- AI handles reservation logic
- "Real-time interaction with natural language"

**Custom Query #2 - Chef's Special**
- Type: "What's the chef's special today?"
- AI provides contextual information
- "Personalized responses based on restaurant data"

**File Attachment Demo (if applicable)**
- Upload an image or PDF
- "Users can share dietary requirements, menu photos, etc."

### Technical Breakdown (2 minutes)

**Architecture**
- "Frontend: Pure HTML/CSS/JavaScript with ChatKit SDK"
- "Backend: FastAPI handling session management"
- "Agent: OpenAI Agent Builder with custom workflow"

**Show the Code**
1. Open `server.py` in VS Code
   - "Simple FastAPI endpoint creates ChatKit sessions"
   - Point to workflow ID configuration

2. Open `public/chatkit-init.js`
   - "Custom theming matches restaurant branding"
   - Show starter prompts configuration
   - Demonstrate error handling

3. Open `public/index.html`
   - "Professional frontend with embedded ChatKit"
   - Responsive design for mobile

**Production Features**
- ✅ Secure session management
- ✅ Custom branding and theming
- ✅ Error handling and recovery
- ✅ File attachment support
- ✅ Conversation history
- ✅ Mobile responsive
- ✅ Easy deployment

### Deployment Discussion (1 minute)
"This is production-ready and can be deployed to:
- Backend: Railway, Render, AWS, Azure
- Frontend: Vercel, Netlify, S3
- Full stack: DigitalOcean App Platform

All configuration is environment-based, making it secure and scalable."

### Q&A Points

**"How does ChatKit connect to the agent?"**
- Backend creates session with workflow ID
- Returns client secret to frontend
- ChatKit uses secret to establish connection
- All communication goes through OpenAI's infrastructure

**"Can this handle production traffic?"**
- Yes! OpenAI handles backend scaling
- Our FastAPI server is stateless
- Can add rate limiting, authentication as needed

**"How do you customize the agent's behavior?"**
- Use Agent Builder to configure workflow
- Update prompts and tools in the builder
- ChatKit automatically reflects changes

**"What about security?"**
- API keys stored in environment variables
- Client never sees API key
- Session secrets are short-lived
- HTTPS in production

---

## 📊 Training Course Integration

### For "Agentic AI Builder Expert: Batch 2"

**Module Alignment:**
- **Day 1-2**: Foundation - Show agent setup
- **Day 3-4**: RAG & Tools - Demonstrate knowledge integration
- **Day 5-6**: MCP Integration - Explain session management
- **Day 7-8**: Production Deployment - Use this as case study
- **Day 9-10**: Best Practices - Reference this architecture

**Hands-On Exercise Ideas:**
1. Clone this project
2. Modify the restaurant theme
3. Add new starter prompts
4. Customize the agent workflow
5. Deploy to production platform

**Key Learning Points:**
- End-to-end AI agent deployment
- Frontend-backend integration
- Production-grade architecture
- Real-world industry application
- Professional presentation techniques

---

## 🔧 Customization Guide

### Change Restaurant Name/Theme
1. Edit `public/index.html`
2. Update CSS variables in `<style>` section
3. Modify hero image URL
4. Change menu items and prices

### Modify AI Assistant Behavior
1. Update starter prompts in `chatkit-init.js`
2. Change greeting message
3. Adjust theme colors to match branding
4. Configure file attachment types

### Update Agent Workflow
1. Log into OpenAI Agent Builder
2. Modify your workflow
3. Test changes
4. Deploy new version
5. Update `WORKFLOW_VERSION` in `.env` if needed

---

## 📋 Pre-Demo Checklist

- [ ] .env file configured with API key
- [ ] Virtual environment activated
- [ ] Dependencies installed successfully
- [ ] Backend server running (port 8000)
- [ ] Frontend server running (port 3000)
- [ ] Website loads in browser
- [ ] ChatKit widget initializes
- [ ] Test all starter prompts
- [ ] Try custom queries
- [ ] Check file upload (if needed)
- [ ] Browser console shows no errors
- [ ] Backend logs show successful sessions

---

## 🐛 Common Issues & Solutions

### Issue: "ChatKit not loading"
**Solution:** 
- Check backend is running: http://localhost:8000/health
- Verify API key in .env
- Check browser console for errors
- Ensure workflow ID is correct

### Issue: "CORS errors"
**Solution:**
- Backend runs on port 8000
- Frontend on port 3000
- CORS is configured for these ports
- Using different ports? Update server.py

### Issue: "Module not found errors"
**Solution:**
- Activate virtual environment
- Run: `pip install -r requirements.txt`
- Verify installation completed

### Issue: "Session creation fails"
**Solution:**
- Verify OpenAI API key is valid
- Check you have ChatKit access
- Confirm workflow ID exists
- Review backend logs for details

---

## 🌟 Success Metrics

Your demo is successful if you can:
1. ✅ Load the website smoothly
2. ✅ ChatKit widget appears and initializes
3. ✅ Send and receive messages
4. ✅ Demonstrate all starter prompts
5. ✅ Show custom query handling
6. ✅ Explain the architecture clearly
7. ✅ Answer technical questions confidently

---

## 📚 Additional Resources

- **OpenAI ChatKit Docs**: https://platform.openai.com/docs/chatkit
- **Agent Builder**: https://platform.openai.com/docs/agent-builder
- **FastAPI Docs**: https://fastapi.tiangolo.com/
- **Your Agent**: https://platform.openai.com/agents/[your-workflow-id]

---

## 🎓 Next Steps

1. **Practice the demo** multiple times
2. **Customize** the restaurant theme to your preference
3. **Prepare** for common questions
4. **Test** on different devices/browsers
5. **Deploy** to production platform (optional)
6. **Share** with your training course students

---

## 💡 Pro Tips

- Keep both terminal windows visible during demo
- Have browser console open to show real-time logs
- Prepare 3-4 interesting custom queries ahead of time
- Test file upload feature before demo
- Have backup queries ready if something fails
- Know your workflow ID and version number
- Be ready to explain architecture diagram

---

**You're all set! Good luck with your demo! 🚀**

For questions or issues, refer to README.md or check the troubleshooting section.

---

**Built by Cognithic AI Labs**
*Showcasing Production-Ready AI Agent Deployment*
