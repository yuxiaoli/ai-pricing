# AI Pricing Data Extraction

## Overview
This repository is an experimental project aiming to utilize LLMs to maintain real-time structured data from unstructured input sources. Specifically, it automates the extraction, transformation, and validation of AI service pricing information from various providers' web pages.

## Motivation
The project is driven by the need to continuously monitor and standardize AI service pricing across multiple providers. Since pricing information is often presented in unstructured formats (HTML, tables, PDFs, etc.), using LLMs for bi-directional conversion between structured and unstructured data provides an efficient and scalable approach.

## Workflow

1. **Input Data**: A list of AI provider pricing URLs is maintained in [`data/ai_providers.json`](data/ai_providers.json).
2. **Data Extraction**:
   - The HTML from each provider's pricing page is retrieved.
   - LLM processes the HTML content based on a predefined JSON schema to generate structured pricing data, stored in [`data/providers/`](data/providers/).
3. **Data Merging**:
   - All pricing JSON files are consolidated into a single list ([`data/ai_api_services.all.json`](data/ai_api_services.all.json)).
4. **Validation & Finalization**:
   - The merged dataset is validated against the schema using LLM-based review.
   - The final cleaned and verified pricing data is output to [`data/ai_api_services.json`](data/ai_api_services.json).

## Final Output
The processed and structured AI service pricing data is available in [`data/ai_api_services.json`](data/ai_api_services.json?raw=true). This file contains detailed pricing information, categorized by provider and service type.

### Example JSON Output:
```json
{
  "ai_providers": [
    {
      "name": "openai",
      "website": "https://openai.com",
      "pricing": "https://openai.com/pricing"
    },
    {
      "name": "google",
      "website": "https://cloud.google.com/gemini-api",
      "pricing": "https://cloud.google.com/gemini-api/pricing"
    }
  ],
  "AI_Types": [
    {
      "type": "LLM",
      "description": "Large Language Models (LLMs) for text generation, conversation, and reasoning.",
      "example_providers": ["openai", "google", "anthropic"]
    }
  ],
  "AI_API_Services": [
    {
      "company": "openai",
      "products": [
        {
          "name": "GPT-4o",
          "type": "LLM",
          "pricing": { "input_per_1K_tokens": 0.003, "output_per_1K_tokens": 0.015, "currency": "USD" },
          "api_endpoint": "https://api.openai.com/v1/chat/completions"
        }
      ]
    }
  ]
}
```

## Why Structured JSON Data Matters?
Structured JSON data is essential for ensuring consistency, reusability, and interoperability across various applications and analytical workflows. By transforming unstructured pricing information into JSON format, we achieve:
- **Automated Processing**: Enables seamless data integration into dashboards, pricing calculators, and AI-powered analytics.
- **Schema Enforcement**: Ensures uniformity and validation of extracted pricing data, reducing errors and inconsistencies.
- **Scalability**: Structured data can be efficiently aggregated and compared across multiple providers, making it easier to track trends and pricing changes over time.
- **API Integration**: Well-structured JSON data can be directly consumed by APIs, improving the efficiency of downstream applications and automation tools.

## How It Works
This project leverages:
- **LLM-powered text extraction**: Parsing unstructured HTML content and transforming it into structured JSON.
- **Schema-based validation**: Ensuring extracted data adheres to a predefined format.
- **Automated merging and cleaning**: Consolidating data from multiple sources to maintain a comprehensive dataset.

## LLM-Driven Automation
This workflow is largely automated by LLMs, significantly reducing the need for manual intervention:
- **Generating JSON Schemas**: The LLM defines the structure and schema for extracted pricing data, ensuring standardized formatting.
- **Data Extraction & Transformation**: LLMs analyze raw HTML and generate structured JSON representations without manual parsing.
- **Merging & Validation**: The final merging script, written with LLM assistance, consolidates and validates the extracted data to ensure completeness and accuracy.

## Potential Use Cases
- **Market analysis**: Comparing AI API pricing across providers.
- **Competitive intelligence**: Monitoring pricing trends and changes.
- **Automation of cost estimation tools**: Feeding structured pricing data into AI service cost calculators.

## Future Enhancements
- Automate HTML retrieval and processing via web scraping.
- Extend support to additional AI services beyond pricing (e.g., feature comparison, rate limits).
- Introduce visualization tools for pricing trends.

## Contributions
Contributions and feedback are welcome! If you encounter any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

