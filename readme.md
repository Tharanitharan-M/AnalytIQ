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
