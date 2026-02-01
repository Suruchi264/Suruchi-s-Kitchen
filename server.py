from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from openai import OpenAI
from dotenv import load_dotenv
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

app = FastAPI(title="RestaurantIQ - Nisarg's Kitchen AI Assistant")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Store for assistant IDs
ASSISTANTS = {}

class ChatRequest(BaseModel):
    message: str
    thread_id: str | None = None

class ChatResponse(BaseModel):
    response: str
    thread_id: str
    category: str | None = None

def get_or_create_triage_assistant():
    """
    Creates a triage assistant based on your RestaurantIQ logic
    This mimics your Triage Agent from Agent Builder
    """
    if "triage" in ASSISTANTS:
        return ASSISTANTS["triage"]
    
    assistant = client.beta.assistants.create(
        name="RestaurantIQ Triage Agent",
        instructions="""You are a triage agent for RestaurantIQ, a restaurant operations system. 

Your job: Analyze queries and categorize them into ONE of these categories:

**CATEGORIES:**
1. **MENU** - menu items, recipes, nutrition, food trends, pricing, dish recommendations
2. **INVENTORY** - stock levels, ordering, suppliers, reordering, ingredient availability
3. **CUSTOMER** - reviews, feedback, complaints, satisfaction, service issues
4. **COMPLIANCE** - food safety, regulations, health codes, certifications, FDA/USDA rules
5. **GENERAL** - anything else (hours, location, general questions)

**CLASSIFICATION RULES:**
- Choose EXACTLY ONE category
- Base decision ONLY on the query content
- If multiple categories apply, pick the PRIMARY focus
- When in doubt, use GENERAL

**EXAMPLES:**
- "What are 2025 burger trends?" → MENU
- "We're low on chicken" → INVENTORY
- "Customer complained about wait time" → CUSTOMER
- "What's the cold holding temperature?" → COMPLIANCE
- "What are your business hours?" → GENERAL

**YOUR RESPONSE:**
Respond with ONLY the category name in uppercase: MENU, INVENTORY, CUSTOMER, COMPLIANCE, or GENERAL""",
        model="gpt-4o-mini"
    )
    
    ASSISTANTS["triage"] = assistant.id
    logger.info(f"Created triage assistant: {assistant.id}")
    return assistant.id

def get_or_create_specialist_assistant(category: str):
    """
    Creates specialist assistants based on your Agent Builder agents
    """
    if category in ASSISTANTS:
        return ASSISTANTS[category]
    
    # Instructions based on your RestaurantIQ agents
    instructions_map = {
        "MENU": """You are the Menu Intelligence Agent for RestaurantIQ.

**CAPABILITIES:**
- Research food trends and industry insights
- Analyze recipes and menu items
- Provide nutritional information
- Suggest menu optimizations
- Recommend pricing strategies

**YOUR APPROACH:**
- Use data-driven recommendations
- Consider current F&B trends
- Factor in seasonal availability
- Balance profitability with customer appeal
- Provide specific, actionable suggestions

**RESTAURANT CONTEXT - Nisarg's Kitchen:**
Menu items include:
- Paneer Tikka Masala ($14.99) - Cottage cheese in creamy tomato sauce
- Biryani Special ($16.99) - Aromatic basmati rice with vegetables
- Dal Makhani ($12.99) - Slow-cooked black lentils
- Palak Paneer ($13.99) - Cottage cheese in spinach curry
- Gulab Jamun ($6.99) - Traditional Indian dessert

Focus on Indian cuisine, vegetarian options, and authentic flavors.""",

        "INVENTORY": """You are the Inventory & Supplier Agent for RestaurantIQ.

**CAPABILITIES:**
- Monitor stock levels
- Calculate reorder points
- Recommend suppliers
- Optimize inventory management
- Estimate costs and lead times

**YOUR APPROACH:**
- Prevent stockouts and overstocking
- Consider lead times and seasonal demand
- Find cost-effective suppliers
- Provide specific quantities and timing
- Calculate reorder thresholds (current stock, daily usage, lead time)

**REORDER FORMULA:**
Reorder Point = (Daily Usage × Lead Time Days) + Safety Stock

**COMMON INVENTORY ITEMS:**
- Basmati rice (25 lbs/day, 3-day lead time)
- Paneer (15 lbs/day, 2-day lead time)
- Tomatoes (20 lbs/day, 1-day lead time)
- Spices (various, weekly restock)

Provide actionable recommendations with calculations.""",

        "CUSTOMER": """You are the Customer Intelligence Agent for RestaurantIQ.

**CAPABILITIES:**
- Analyze customer feedback and reviews
- Identify satisfaction trends
- Generate professional responses
- Suggest service improvements
- Track sentiment patterns

**YOUR APPROACH:**
- Empathize with customer concerns
- Identify root causes of issues
- Suggest specific improvements
- Draft professional, caring responses
- Focus on turning negatives into positives

**RESPONSE GUIDELINES:**
For complaints:
1. Acknowledge and apologize sincerely
2. Explain what went wrong (if known)
3. Offer a solution or compensation
4. Thank them for feedback
5. Invite them back

**NISARG'S KITCHEN VALUES:**
- Authentic Indian cuisine
- Warm hospitality
- Fresh ingredients
- Family atmosphere
- Customer satisfaction

Use empathy and professionalism in all responses.""",

        "COMPLIANCE": """You are the Compliance & Safety Agent for RestaurantIQ.

**CAPABILITIES:**
- Food safety regulations (FDA, USDA, local codes)
- Temperature requirements
- Hygiene standards
- Certification requirements
- Health inspection preparation

**KEY REGULATIONS:**
- Cold holding: 41°F (5°C) or below
- Hot holding: 135°F (57°C) or above
- Cooking temps: Poultry 165°F, Ground meat 155°F, Whole meat 145°F
- Cooling: 135°F to 70°F in 2 hours, then 70°F to 41°F in 4 hours
- Handwashing: 20 seconds with soap

**YOUR APPROACH:**
- Cite specific regulations and temperatures
- Prioritize safety over convenience
- Provide clear, actionable guidance
- Reference official sources (FDA, USDA)
- Explain the "why" behind rules

**CRITICAL REMINDERS:**
- Food safety is non-negotiable
- When in doubt, throw it out
- Document everything
- Train staff regularly

Always err on the side of caution.""",

        "GENERAL": """You are the General Assistant for RestaurantIQ - Nisarg's Kitchen.

**CAPABILITIES:**
- Answer general questions about the restaurant
- Provide basic information
- Handle miscellaneous inquiries
- Direct to specialists when needed

**NISARG'S KITCHEN INFO:**
- **Location:** 123 Culinary Street, Food City, FC 12345
- **Hours:** Monday-Sunday, 11:00 AM - 10:00 PM
- **Phone:** (555) 123-4567
- **Email:** hello@nisargskitchen.com
- **Services:** Dine-in, Takeout, Delivery
- **Cuisine:** Authentic Indian, Vegetarian-focused
- **Specialties:** North Indian curries, biryanis, tandoor items
- **Capacity:** 50 seats
- **Parking:** Street parking and nearby lot

**YOUR APPROACH:**
- Be friendly and welcoming
- Provide accurate information
- If question requires specialist knowledge, acknowledge and suggest category
- Maintain the warm, hospitable tone of Indian hospitality

Namaste! 🙏"""
    }
    
    assistant = client.beta.assistants.create(
        name=f"RestaurantIQ {category.title()} Agent",
        instructions=instructions_map.get(category, instructions_map["GENERAL"]),
        model="gpt-4o-mini"
    )
    
    ASSISTANTS[category] = assistant.id
    logger.info(f"Created {category} assistant: {assistant.id}")
    return assistant.id

def run_assistant(assistant_id: str, thread_id: str, message: str):
    """Run assistant and wait for completion"""
    # Add message to thread
    client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=message
    )
    
    # Run assistant
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id
    )
    
    # Wait for completion
    max_attempts = 60
    for _ in range(max_attempts):
        run_status = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id
        )
        
        if run_status.status == 'completed':
            break
        elif run_status.status in ['failed', 'cancelled', 'expired']:
            raise HTTPException(status_code=500, detail=f"Run {run_status.status}")
        
        time.sleep(0.5)
    
    # Get response
    messages = client.beta.threads.messages.list(thread_id=thread_id)
    for message in messages.data:
        if message.role == "assistant":
            for content in message.content:
                if content.type == "text":
                    return content.text.value
    
    return "No response generated"

@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    RestaurantIQ chat endpoint - mimics your Agent Builder workflow
    """
    try:
        # Create or use thread
        if request.thread_id:
            thread_id = request.thread_id
        else:
            thread = client.beta.threads.create()
            thread_id = thread.id
            logger.info(f"Created new thread: {thread_id}")
        
        # Step 1: Triage (classify the query)
        triage_assistant_id = get_or_create_triage_assistant()
        category_response = run_assistant(triage_assistant_id, thread_id, request.message)
        
        # Extract category from response
        category = "GENERAL"
        for cat in ["MENU", "INVENTORY", "CUSTOMER", "COMPLIANCE", "GENERAL"]:
            if cat in category_response.upper():
                category = cat
                break
        
        logger.info(f"Query categorized as: {category}")
        
        # Step 2: Route to specialist
        specialist_assistant_id = get_or_create_specialist_assistant(category)
        specialist_response = run_assistant(
            specialist_assistant_id, 
            thread_id, 
            f"Original query: {request.message}\n\nProvide a comprehensive, helpful response."
        )
        
        logger.info(f"Specialist response generated ({len(specialist_response)} chars)")
        
        return ChatResponse(
            response=specialist_response,
            thread_id=thread_id,
            category=category.lower()
        )
        
    except Exception as e:
        logger.error(f"Error in chat endpoint: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "system": "RestaurantIQ",
        "assistants_created": len(ASSISTANTS),
        "api_key_configured": bool(os.environ.get("OPENAI_API_KEY"))
    }

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "RestaurantIQ - Multi-Agent Restaurant Operations System",
        "version": "Demo v1.0",
        "based_on": "Agent Builder Workflow wf_694817bace748190857ed8ad2f86b6730df6a376fb67bef8",
        "categories": ["menu", "inventory", "customer", "compliance", "general"],
        "endpoints": {
            "health": "/health",
            "chat": "/api/chat (POST)"
        }
    }

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting RestaurantIQ Multi-Agent System...")
    logger.info("Based on Agent Builder workflow wf_694817bace748190857ed8ad2f86b6730df6a376fb67bef8")
    uvicorn.run(app, host="0.0.0.0", port=8000)