import boto3, json, os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize AWS Bedrock client
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
MODEL_ID = os.getenv("BEDROCK_MODEL_ID", "anthropic.claude-3-haiku-20240307-v1:0")

# Create bedrock client with explicit credentials if provided
bedrock_config = {
    "service_name": "bedrock-runtime",
    "region_name": AWS_REGION
}

if AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY:
    bedrock_config["aws_access_key_id"] = AWS_ACCESS_KEY_ID
    bedrock_config["aws_secret_access_key"] = AWS_SECRET_ACCESS_KEY

bedrock = boto3.client(**bedrock_config)

def extract_sql_from_response(text: str) -> str:
    """
    Extract SQL query from LLM response.
    Handles cases where SQL is wrapped in markdown code blocks or has explanatory text.
    """
    # Remove markdown code blocks if present
    if "```sql" in text:
        # Extract content between ```sql and ```
        start = text.find("```sql") + 6
        end = text.find("```", start)
        if end != -1:
            text = text[start:end]
    elif "```" in text:
        # Extract content between ``` and ```
        start = text.find("```") + 3
        end = text.find("```", start)
        if end != -1:
            text = text[start:end]
    
    # Clean up the query
    text = text.strip()
    
    # If there are multiple lines and some are not SQL, try to find the SELECT statement
    lines = text.split('\n')
    sql_lines = []
    in_query = False
    
    for line in lines:
        line_stripped = line.strip()
        # Start capturing when we see SELECT
        if line_stripped.upper().startswith('SELECT'):
            in_query = True
        
        # Add SQL lines
        if in_query:
            sql_lines.append(line)
            # Stop if we hit a semicolon at the end
            if line_stripped.endswith(';'):
                break
    
    if sql_lines:
        result = '\n'.join(sql_lines).strip()
        # Remove trailing semicolon if present (SQLAlchemy doesn't need it)
        if result.endswith(';'):
            result = result[:-1].strip()
        return result
    
    # If no SELECT found, return the cleaned text
    return text

def nl_to_sql(prompt: str, schema_hint: str) -> str:
    """
    Convert natural language prompt to SQL query using AWS Bedrock.
    """
    system_prompt = """You are a SQL expert. Convert natural language questions to SQL queries.
Rules:
1. Return ONLY the SQL query, nothing else
2. No explanations, no markdown formatting, no code blocks
3. Use only SELECT statements (read-only queries)
4. Reference only the tables and columns provided in the schema
5. Write clean, efficient PostgreSQL queries"""

    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 512,
        "messages": [
            {
                "role": "user",
                "content": f"""{system_prompt}

Schema: {schema_hint}

Question: {prompt}

SQL Query:"""
            }
        ]
    }
    
    resp = bedrock.invoke_model(body=json.dumps(body), modelId=MODEL_ID)
    out = json.loads(resp["body"].read())
    text = out["content"][0]["text"]
    
    # Extract and clean the SQL
    sql = extract_sql_from_response(text)
    return sql