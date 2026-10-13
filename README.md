# 竞品舆情监控分析（模拟评论）

用 **模板生成的中文评论** 演示 CRM 竞品口碑分析流程：SnowNLP 情感分、jieba 关键词、词云、月度正面率趋势，以及一张「竞争力雷达图」。

> **数据说明**：`data/reviews.csv` 由 `generate_data.py` 按正/负模板随机拼出来（默认各 600 条，产品名仅为演示）。**不是**应用商店或真实用户评论。雷达图六个维度分数在 `analysis.py` 里写死，**没有**从评论文本自动算出，面试时请主动说明。

## 要解决什么问题

产品/运营想快速对比自家 CRM 与竞品的口碑结构时，常见做法是人工读评论。本仓库把「情感分布 → 趋势 → 词频/词云 → 结论卡片」串成可复现脚本，方便展示 NLP 分析链路；真实落地需要接公开评论源或内部工单，并换更强的情感模型。

## 实际做了什么

| 模块 | 实现 | 局限 |
|------|------|------|
| 情感 | SnowNLP `sentiments`，按阈值划正/中/负 | 对行业术语弱，分数受模板措辞影响大 |
| 趋势 | 按月聚合正面占比 | 模拟日期均匀随机，趋势无真实事件含义 |
| 关键词/词云 | jieba 分词 + 词频；WordCloud（缺字体时退化为词列表） | 停用词表很短，噪声词会进来 |
| 雷达图 | 手写 `own_scores` / `comp_scores` | **不是**从评论统计出的维度分 |

## 项目结构

```
competitor-sentiment-analysis/
├── generate_data.py   # 合成 reviews.csv
├── analysis.py        # 情感/词频/出图
├── requirements.txt
├── data/
│   └── reviews.csv
└── output/
    └── competitor_report.png
```

## 环境与运行

需要 Python 3.10+。Linux/macOS 上若无中文字体，词云可能退化成文字列表，其余图仍可出。

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python generate_data.py
python analysis.py
```

## 样例结论怎么读

终端会打印各产品正面/负面占比与情感均分；`output/competitor_report.png` 汇总图表。因为数据是模板合成、雷达分是写死的，**不要把图中「策略建议」当成真实市场结论**，只适合讲清方法和代码结构。

## 面试可讲的点

- 先说明数据是合成的，再讲管道：清洗 → 情感 → 聚合 → 可视化。
- SnowNLP vs 业务词典 / 微调 BERT：准确率与部署成本怎么权衡。
- 雷达图若要严肃：应用户评论做主题分类或方面级情感，再聚合到维度，而不是手填分数。
- 生产监控：定时拉取公开评论、报警规则、人工抽检。

## 技术栈

Python · Pandas · NumPy · SnowNLP · jieba · WordCloud · Matplotlib

## License

MIT（演示代码；合成数据可自由改模板重跑）。
