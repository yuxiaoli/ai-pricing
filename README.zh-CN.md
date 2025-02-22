# AI定价数据提取

## 概述
本存储库是一个实验性项目，旨在利用LLM（大语言模型）从非结构化输入数据源维护实时结构化数据。具体而言，它自动化了从各个提供商网页提取、转换和验证AI服务定价信息的流程。

## 动机
本项目的目标是持续监测和标准化多个提供商的AI服务定价信息。由于定价信息通常以非结构化格式（HTML、表格、PDF等）呈现，使用LLM在结构化和非结构化数据之间进行双向转换提供了一种高效且可扩展的方法。

## 工作流程

1. **输入数据**：维护一个AI提供商定价URL列表，存储在 [`data/ai_providers.json`](data/ai_providers.json)。
2. **数据提取**：
   - 获取每个提供商定价页面的HTML。
   - LLM基于预定义的JSON模式处理HTML内容，生成结构化定价数据，并存储在 [`data/providers/`](data/providers/)。
3. **数据合并**：
   - 所有定价JSON文件合并为一个列表，存储在 [`data/ai_api_services.all.json`](data/ai_api_services.all.json)。
4. **验证与最终处理**：
   - 使用LLM对合并数据集进行模式验证。
   - 最终清理并验证的数据输出到 [`data/ai_api_services.json`](data/ai_api_services.json)。

## 最终输出
处理后的结构化AI服务定价数据存储在 [`data/ai_api_services.json`](data/ai_api_services.json?raw=true)。此文件包含详细的定价信息，并按提供商和服务类型分类。

### JSON示例输出：
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
      "description": "用于文本生成、对话和推理的大型语言模型（LLM）。",
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

## 为什么结构化JSON数据很重要？
结构化JSON数据对于确保一致性、可重用性和跨各种应用程序及分析工作流的互操作性至关重要。通过将非结构化的定价信息转换为JSON格式，我们能够实现：
- **自动化处理**：可将数据无缝集成到仪表板、定价计算器和AI驱动的分析工具中。
- **模式强制执行**：确保提取的数据符合预定义格式，减少错误和不一致性。
- **可扩展性**：结构化数据可以高效地聚合和比较多个提供商的数据，便于跟踪趋势和定价变化。
- **API集成**：良好结构化的JSON数据可以直接供API消费，提高下游应用程序和自动化工具的效率。

## 工作原理
本项目利用：
- **LLM驱动的文本提取**：解析非结构化HTML内容并将其转换为结构化JSON。
- **基于模式的验证**：确保提取的数据符合预定义格式。
- **自动合并与清理**：从多个来源整合数据，维护全面的数据集。

## LLM自动化工作流
本工作流主要由LLM自动完成，大幅减少人工干预：
- **生成JSON模式**：LLM定义提取的定价数据结构和模式，确保标准化格式。
- **数据提取与转换**：LLM分析原始HTML，并自动生成结构化的JSON表示。
- **数据合并与验证**：最终合并脚本由LLM辅助编写，确保提取数据的完整性和准确性。

## 潜在应用场景
- **市场分析**：比较不同AI API提供商的定价。
- **竞争情报**：监测定价趋势和变更。
- **自动化成本估算工具**：将结构化定价数据集成到AI服务成本计算器中。

## 未来改进方向
- 自动化HTML抓取和处理。
- 扩展支持范围，涵盖AI服务的其他方面（如功能对比、速率限制等）。
- 引入定价趋势可视化工具。

## 贡献
欢迎贡献和反馈！如果您遇到任何问题或有改进建议，请随时提交Issue或Pull Request。

## 许可证
本项目遵循MIT许可证。

