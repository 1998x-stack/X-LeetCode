import pandas as pd
def classify_nodes(df):
    all_ids = set(df['id'])
    parent_ids = set(df['p_id'].dropna())
    
    root_ids = set(df['id'][df['p_id'].isnull()]) # 根节点的id
    
    leaf_ids = all_ids - parent_ids # 叶子节点的id
    inner_ids = all_ids - root_ids - leaf_ids # 内部节点的id
    
    # 创建结果DataFrame
    result = []
    for node_id in root_ids:
        result.append({'id': node_id, 'node_type': 'Root'})
    for node_id in leaf_ids:
        result.append({'id': node_id, 'node_type': 'Leaf'})
    for node_id in inner_ids:
        result.append({'id': node_id, 'node_type': 'Inner'})
    
    return pd.DataFrame(result)

# 构建模拟的数据表
data = {'id': [1, 2, 3, 4, 5, 6],
        'p_id': [None, 1, 1, 2, 2, 3]}
df = pd.DataFrame(data)
# 运行分类函数
result_df = classify_nodes(df)
print(result_df)