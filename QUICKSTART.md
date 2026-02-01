# QUICK SETUP GUIDE - Nisarg's Kitchen

## 🚀 5-Minute Setup

### Step 1: Setup Environment (1 min)
```bash
# Copy environment template
cp .env.example .env

# Edit .env file and add your OpenAI API key
# The workflow ID and version are already set!
```

### Step 2: Install Dependencies (2 min)
```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install packages
pip install -r requirements.txt
```

### Step 3: Run the Project (2 min)

**Option A: Automatic (Recommended)**
```bash
# Windows:
start.bat

# Mac/Linux:
./start.sh
```

**Option B: Manual**

Terminal 1 - Backend:
```bash
python server.py
```

Terminal 2 - Frontend:
```bash
cd public
python -m http.server 3000
```

Then open: http://localhost:3000

---

## ✅ Verification Checklist

- [ ] .env file created with OPENAI_API_KEY
- [ ] Virtual environment activated
- [ ] Dependencies installed (no errors)
- [ ] Backend running on port 8000
- [ ] Frontend running on port 3000
- [ ] Website opens in browser
- [ ] ChatKit widget loads
- [ ] Can send messages to AI assistant

---

## 🎯 What You'll See

1. **Beautiful Restaurant Website**
   - Hero section with restaurant name
   - Menu preview
   - About section

2. **AI Assistant Section**
   - Live ChatKit widget embedded
   - Starter prompts for quick interaction
   - Real-time conversation with your agent

3. **Working Features**
   - Message sending/receiving
   - File attachments
   - Conversation history
   - Themed interface matching restaurant branding

---

## 🔥 Demo Script (For Presentations)

1. **Show the Website**
   - "This is Nisarg's Kitchen, a modern restaurant website"
   - Scroll through sections

2. **Introduce AI Assistant**
   - "Now let me show you our AI-powered customer service"
   - Scroll to AI Assistant section

3. **Demonstrate Starter Prompts**
   - Click on "Menu Recommendations"
   - Show how AI responds

4. **Show Custom Queries**
   - Type: "What are your vegetarian options?"
   - Type: "I need a table for 4 people tonight"

5. **Highlight Technical Implementation**
   - "This is powered by OpenAI Agent Builder"
   - "Uses ChatKit for the embedded interface"
   - "Connected to a custom workflow ID"
   - "Backend handles session management"

6. **Show Production-Ready Features**
   - File attachments capability
   - Conversation history
   - Custom theming
   - Mobile responsive design

---

## 📝 Important Notes

- Keep both terminals running (backend + frontend)
- Backend logs show session creation
- Browser console shows ChatKit initialization
- Any errors? Check README.md troubleshooting section

---

## 🎓 For Your Training Course

This demo showcases:
- ✅ OpenAI Agent Builder integration
- ✅ ChatKit embedded UI
- ✅ Production-grade architecture
- ✅ Real-world F&B use case
- ✅ Custom branding and theming
- ✅ Session management
- ✅ Local deployment workflow

Perfect for demonstrating to your "Agentic AI Builder Expert: Batch 2" students!

---

**Ready to impress? Let's go! 🚀**
