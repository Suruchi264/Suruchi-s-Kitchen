# Architecture Diagram

## System Architecture

```mermaid
graph TB
    subgraph "Frontend (Port 3000)"
        A[HTML Website<br/>Nisarg's Kitchen]
        B[ChatKit Widget<br/>Embedded UI]
        C[chatkit-init.js<br/>Configuration]
    end
    
    subgraph "Backend (Port 8000)"
        D[FastAPI Server<br/>server.py]
        E[Session Endpoint<br/>/api/chatkit/session]
    end
    
    subgraph "OpenAI Platform"
        F[ChatKit Service]
        G[Agent Builder<br/>Workflow ID: wf_694817...]
        H[GPT-4 Model]
    end
    
    subgraph "Configuration"
        I[.env File<br/>API Key, Workflow ID]
    end
    
    A --> B
    B --> C
    C -->|HTTP POST| E
    E -->|Create Session| F
    D --> E
    D -->|Read Config| I
    F -->|Client Secret| C
    B -->|Messages| F
    F -->|Invoke| G
    G -->|Use| H
    H -->|Response| G
    G -->|Stream| F
    F -->|Display| B
    
    style A fill:#d4af37
    style B fill:#2d8cff
    style G fill:#10a37f
    style H fill:#10a37f
```

## Data Flow

```mermaid
sequenceDiagram
    participant User
    participant Browser
    participant ChatKit
    participant Backend
    participant OpenAI
    
    User->>Browser: Opens website (localhost:3000)
    Browser->>Browser: Loads HTML + ChatKit SDK
    Browser->>Backend: POST /api/chatkit/session
    Backend->>Backend: Read workflow ID from .env
    Backend->>OpenAI: Create ChatKit session
    OpenAI-->>Backend: Return client_secret
    Backend-->>Browser: Return client_secret
    Browser->>ChatKit: Initialize with client_secret
    ChatKit-->>Browser: Widget ready
    
    User->>ChatKit: Sends message
    ChatKit->>OpenAI: Forward message + context
    OpenAI->>OpenAI: Process via Agent Builder workflow
    OpenAI-->>ChatKit: Stream response
    ChatKit-->>User: Display response
```

## Deployment Options

```mermaid
graph LR
    subgraph "Local Development"
        A1[VS Code]
        A2[Python venv]
        A3[localhost:8000/3000]
    end
    
    subgraph "Production - Option 1"
        B1[Vercel Frontend]
        B2[Railway Backend]
    end
    
    subgraph "Production - Option 2"
        C1[AWS S3 + CloudFront]
        C2[AWS ECS/Fargate]
    end
    
    subgraph "Production - Option 3"
        D1[DigitalOcean App Platform<br/>Full Stack]
    end
    
    A1 --> A2
    A2 --> A3
    A3 -.->|Deploy| B1
    A3 -.->|Deploy| B2
    A3 -.->|Deploy| C1
    A3 -.->|Deploy| C2
    A3 -.->|Deploy| D1
```

## Component Breakdown

```mermaid
graph TD
    subgraph "Project Structure"
        A[nisargs-kitchen/]
        A --> B[server.py]
        A --> C[requirements.txt]
        A --> D[.env]
        A --> E[public/]
        E --> F[index.html]
        E --> G[chatkit-init.js]
        A --> H[README.md]
        A --> I[start.sh/bat]
    end
    
    style A fill:#d4af37
    style E fill:#2d8cff
```

---

To view these diagrams:
1. Use any Markdown viewer that supports Mermaid
2. GitHub automatically renders Mermaid diagrams
3. VS Code with Mermaid extension
4. Online tools like Mermaid Live Editor
