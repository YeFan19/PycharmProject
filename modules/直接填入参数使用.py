tag_node_CQL = '''
    CREATE (tag%d:Tag{id:%d, tag_name:"%s"})
    '''
# 设置为CQL查询标准语句，可以直接导入Neo4j建立节点、属性和关系等

final_CQL = ''
tag_dict = {}
tag_id = 1   # 设置初始值为1
relation_id = 1
# 设置初始值

for tag in result[1]:
    tag_dict[tag] = tag_id
    # tag_dict是个字典，此处是以tag_id给tag编号
    final_CQL += tag_node_CQL % (tag_id, tag_id, tag)
    # 把括号中的量给到tag_node_CQL对应位置，得到具体的cql语句
    relation_id += 1
    tag_id += 1
