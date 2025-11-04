# AnalytIQ

AnalytIQ is an AI-powered data assistant that helps teams query, explore, and visualize their company data using natural language — no SQL required.
It connects to databases like PostgreSQL or CSVs, automatically builds a data catalog, and uses generative AI to turn plain English questions into SQL queries and visual insights.

## Tech Stack

- Frontend: Next.js 14 (App Router) + React + TypeScript + Tailwind CSS

- Backend: FastAPI (Python) + SQLAlchemy + Pydantic

- Database: PostgreSQL (AWS RDS) + pgvector for semantic search

- AI/LLM: AWS Bedrock (Claude 3 / Mistral) for natural-language → SQL generation

- Caching & Messaging: Redis (ElastiCache)

- Infrastructure: AWS ECS Fargate + S3 + CloudFront + Terraform (IaC)

- CI/CD & Monitoring: GitHub Actions + OpenTelemetry + Grafana Cloud + Sentry

## Setup

### Prerequisites
- Python 3.13+
- Node.js 18+
- Docker & Docker Compose
- AWS Account with Bedrock access

### Backend Setup

1. **Start PostgreSQL database:**
   ```bash
   docker-compose up -d
   ```

2. **Create virtual environment and install dependencies:**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure AWS Credentials:**
   
   Create a `.env` file in the `backend/` directory (use `env.example` as template):
   ```bash
   cp env.example .env
   ```
   
   Then edit `.env` with your AWS credentials:
   ```
   AWS_ACCESS_KEY_ID=your_access_key_here
   AWS_SECRET_ACCESS_KEY=your_secret_key_here
   AWS_REGION=us-east-1
   BEDROCK_MODEL_ID=anthropic.claude-3-haiku-20240307-v1:0
   DATABASE_URL=postgresql://analytiq:analytiq@localhost:5432/analytiq
   ```
   
   **How to get AWS credentials:**
   - Log in to AWS Console
   - Go to IAM → Users → Your User → Security Credentials
   - Create Access Key → Application running outside AWS
   - Save the Access Key ID and Secret Access Key
   - Ensure your IAM user has `AmazonBedrockFullAccess` policy attached

4. **Run database migrations:**
   ```bash
   alembic upgrade head
   ```

5. **Seed sample data (optional):**
   ```bash
   python scripts/seed_orders.py
   ```

6. **Start the backend server:**
   ```bash
   uvicorn app.main:app --reload
   ```
   
   The API will be available at `http://localhost:8000`

### Frontend Setup

1. **Install dependencies:**
   ```bash
   cd frontend
   npm install
   ```

2. **Start the development server:**
   ```bash
   npm run dev
   ```
   
   The frontend will be available at `http://localhost:3000`

## Usage

1. Navigate to `http://localhost:3000`
2. Go to the Query page at `http://localhost:3000/query`
3. Enter a natural language question about your data (e.g., "Show me all orders from the last 30 days")
4. The system will generate SQL and execute it against your database
