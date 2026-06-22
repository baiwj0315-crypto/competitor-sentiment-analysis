"""
模拟两款 CRM 产品的用户评论数据
自家产品：销帮帮CRM  竞品：纷享销客
"""
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

random.seed(42)
np.random.seed(42)

# 自家产品评论模板
own_positive = [
    "界面简洁好用，上手很快，销售团队都很喜欢",
    "数据报表功能很强大，老板看了很满意",
    "客服响应速度快，问题都能及时解决",
    "移动端体验不错，出差也能随时跟进客户",
    "价格合理，中小企业完全够用",
    "导入数据很方便，从Excel迁移过来很顺畅",
    "自定义字段灵活，可以根据业务需求调整",
    "权限管理做得好，数据安全有保障",
    "邮件提醒功能很贴心，不会错过跟进节点",
    "和企业微信打通了，用起来很顺手",
]
own_negative = [
    "加载速度有点慢，高峰期经常卡顿",
    "报表导出格式太少，希望支持更多格式",
    "手机APP功能不如网页版完整",
    "高级功能需要额外付费，有点贵",
    "搜索功能比较弱，客户多了不好找",
    "没有自动化工作流，很多操作还是要手动",
    "数据备份功能缺失，有点担心数据安全",
    "和其他系统对接麻烦，API文档不够详细",
    "批量操作功能不完善，数据量大很痛苦",
    "UI更新后反而有些功能找不到了",
]

# 竞品评论模板
comp_positive = [
    "功能很全面，基本满足企业级需求",
    "大数据分析能力强，报告很专业",
    "品牌知名度高，合作伙伴认可度好",
    "系统稳定性好，很少出现故障",
    "集成第三方工具方便，生态丰富",
    "销售预测功能很准，帮助团队做计划",
    "培训资源丰富，新员工上手快",
    "定制化程度高，可以深度定制流程",
]
comp_negative = [
    "价格太贵了，中小企业很难承受",
    "界面复杂，新员工学习成本很高",
    "客服态度差，问题要等很久才处理",
    "销售顾问很强硬，买了之后就不管了",
    "合同绑定期太长，灵活性差",
    "功能多但很多用不上，感觉在为功能付费",
    "移动端体验很差，APP经常崩溃",
    "部署周期太长，花了三个月才上线",
    "数据迁移很麻烦，导出格式限制多",
    "强制捆绑销售培训服务，不需要也要买",
    "更新太频繁，每次更新都要重新学",
    "私有化部署费用高得离谱",
]

def make_reviews(positives, negatives, n, product, start_score_bias=0):
    reviews = []
    for _ in range(n):
        is_positive = random.random() < (0.55 + start_score_bias)
        template = random.choice(positives if is_positive else negatives)
        # 加一些随机变化
        prefixes = ["", "总体来说，", "用了半年了，", "强烈推荐！", "踩坑了，", "对比了很多家，"]
        suffixes = ["", "。", "！", "，希望继续改进。", "，性价比不错。", "，不太推荐。"]
        text = random.choice(prefixes) + template + random.choice(suffixes)
        score = random.randint(4, 5) if is_positive else random.randint(1, 3)
        date = datetime(2024, 1, 1) + timedelta(days=random.randint(0, 364))
        reviews.append({
            'product': product,
            'date': date.strftime('%Y-%m-%d'),
            'score': score,
            'review': text,
            'is_positive': int(is_positive),
        })
    return reviews

own_reviews  = make_reviews(own_positive, own_negative, 600, '销帮帮CRM', start_score_bias=0.05)
comp_reviews = make_reviews(comp_positive, comp_negative, 600, '纷享销客', start_score_bias=-0.05)

df = pd.DataFrame(own_reviews + comp_reviews)
df = df.sample(frac=1, random_state=42).reset_index(drop=True)
df.to_csv('data/reviews.csv', index=False, encoding='utf-8-sig')
print(f"数据生成完成：{len(df)} 条评论")
print(df.groupby(['product', 'is_positive']).size().unstack())
