# AI定价数据提取
[English](README.md) | [中文](README.zh-CN.md)

## 概述
本存储库是一个实验性项目，旨在利用LLM来维护从非结构化输入源获取的实时结构化数据。具体而言，它自动提取、转换和验证来自各种提供商网页的AI服务定价信息。

## 动机
该项目的驱动力是需要持续监测和标准化多个提供商的AI服务定价。由于定价信息通常以非结构化格式呈现（HTML、表格、PDF等），使用LLM进行结构化和非结构化数据的双向转换提供了一种高效且可扩展的方法。

随着AI服务的快速扩展，定价格局变得越来越分散。每个AI提供商都有自己的定价模式，使得直接比较变得困难。有些按token收费，而另一些按小时、按实例或采用混合定价结构。这种多样性正是需要结构化数据表示的完美案例。通过利用JSON，我们可以在不同的提供商之间规范化定价数据，从而实现自动化、分析和实时监控，减少人工干预。结构化格式确保定价模式的变化以标准化方式捕获，从而促进透明度，并为开发人员、企业和研究人员提供有价值的决策支持。

## 工作流程

1. **输入数据**：AI提供商定价URL列表存储在 [`data/ai_providers.json`](data/ai_providers.json) 中。
2. **数据提取**：
   - 获取每个提供商定价页面的HTML内容。
   - LLM根据预定义的JSON模式处理HTML内容，以生成结构化定价数据，并存储在 [`data/providers/`](data/providers/)。
3. **数据合并**：
   - 所有定价JSON文件合并到一个列表中（[`data/ai_api_services.all.json`](data/ai_api_services.all.json)）。
4. **验证和最终确认**：
   - 使用LLM进行模式验证，以确保数据的完整性和准确性。
   - 最终清理和验证后的定价数据输出到 [`data/ai_api_services.json`](data/ai_api_services.json)。

## 最终输出
处理和结构化后的AI服务定价数据可在 [`data/ai_api_services.json`](data/ai_api_services.json?raw=true) 获取。该文件包含按提供商和服务类型分类的详细定价信息。

### 示例JSON输出：
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
      "description": "大型语言模型（LLM），用于文本生成、对话和推理。",
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
结构化JSON数据对于确保一致性、可重用性和跨各种应用程序和分析工作流的互操作性至关重要。将非结构化定价信息转换为JSON格式，可以实现：
- **自动化处理**：无缝集成到仪表板、定价计算器和AI驱动的分析系统中。
- **模式约束**：确保提取的定价数据符合统一标准，减少错误和不一致性。
- **可扩展性**：可高效地聚合和比较多个提供商的数据，更容易跟踪定价趋势和变化。
- **API集成**：结构化JSON数据可直接供API使用，提高下游应用程序和自动化工具的效率。

## 工作原理
该项目利用以下技术：
- **基于LLM的文本提取**：解析非结构化HTML内容并转换为结构化JSON。
- **基于模式的验证**：确保提取数据符合预定义格式。
- **自动合并和清理**：从多个来源整合数据，以维护完整的数据集。

## LLM驱动的自动化
该工作流主要由LLM自动执行，显著减少了人工干预的需求：
- **生成JSON模式**：LLM定义提取定价数据的结构和模式，确保标准化格式。
- **数据提取与转换**：LLM分析原始HTML并生成结构化JSON，无需手动解析。
- **合并与验证**：最终合并脚本由LLM协助编写，以整合和验证提取数据，确保完整性和准确性。

## 潜在应用场景
- **市场分析**：比较不同提供商的AI API定价。
- **竞争情报**：监测定价趋势和变化。
- **自动化成本估算工具**：将结构化定价数据输入AI服务成本计算器。

## 未来增强功能
- 通过网络爬虫自动化HTML检索和处理。
- 扩展对定价之外的AI服务支持（例如功能比较、速率限制）。
- 引入定价趋势可视化工具。

## 贡献
欢迎贡献和反馈！如果您遇到任何问题或有改进建议，请随时提交issue或pull request。

## 许可协议
本项目采用MIT许可证。

