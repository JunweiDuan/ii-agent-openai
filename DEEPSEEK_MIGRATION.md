# DeepSeek Migration Guide

This document describes the changes made to migrate from Anthropic API to DeepSeek API.

## Overview

The system has been migrated to use DeepSeek's OpenAI-compatible API instead of Anthropic's proprietary API. This simplifies the codebase and provides access to DeepSeek's powerful reasoning models.

## Key Changes

### 1. Environment Variables

Update your `.env` file:

```bash
# Add DeepSeek API configuration
DEEPSEEK_API_KEY=your_deepseek_api_key

# Optional: Override the base URL (defaults to https://api.deepseek.com/v1)
#DEEPSEEK_BASE_URL=https://api.deepseek.com/v1

# Remove Anthropic configuration
# ANTHROPIC_API_KEY=  # No longer needed
```

### 2. Default Model

The default model has been changed from `claude-3-7-sonnet@20250219` to `deepseek-reasoner` (DeepSeek R1).

You can also use `deepseek-chat` for general chat tasks by updating `DEFAULT_MODEL` in `src/ii_agent/utils/constants.py`.

### 3. Client Implementation

- Removed `src/ii_agent/llm/anthropic.py`
- Enhanced `src/ii_agent/llm/openai.py` to support DeepSeek models
- All client initialization now uses the unified OpenAI-compatible client

### 4. Command Line Arguments

Removed the following arguments that were specific to Google Vertex/Anthropic:
- `--project-id`
- `--region`

### 5. Usage

The usage remains the same:

**CLI:**
```bash
python cli.py
```

**WebSocket Server:**
```bash
python ws_server.py --port 8000
```

## Feature Differences

### Thinking Tokens
- DeepSeek R1 supports reasoning through prompting rather than explicit parameters
- The system automatically adds reasoning prompts when `thinking_tokens > 0`

### Caching
- DeepSeek provides automatic caching based on request content
- No manual cache control is available (unlike Anthropic's cache-control headers)

### Temperature
- For DeepSeek R1, the system uses a default temperature of 0.6 for better reasoning
- This can be overridden by passing a different temperature value

## Model Selection

The system auto-detects DeepSeek models based on the model name:
- Models containing "deepseek" use DeepSeek API configuration
- Models containing "deepseek-r1" or "o1" are treated as CoT (Chain of Thought) models

## Troubleshooting

1. **API Key Issues**: Ensure `DEEPSEEK_API_KEY` is set in your `.env` file
2. **Model Not Found**: Check that you're using a valid DeepSeek model name (e.g., `deepseek-reasoner`, `deepseek-chat`)
3. **Rate Limits**: DeepSeek has different rate limits than Anthropic - adjust concurrency if needed

## Benefits of Migration

1. **Simplified Codebase**: Single OpenAI-compatible client for all models
2. **Cost Efficiency**: DeepSeek offers competitive pricing
3. **Strong Reasoning**: DeepSeek R1 provides excellent reasoning capabilities
4. **Open Standards**: Uses OpenAI-compatible API format 