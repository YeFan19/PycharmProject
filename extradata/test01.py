# -*- coding: utf-8 -*-

from py2neo import Graph, Node, Relationship, NodeSelector
graph = Graph("http://139.224.129.150:7474/browser/", username="neo4j", password="BIT!smartteam")

# 用CQL进行查询，返回的结果是list
data1 = graph.data('MATCH(p:Tag) return p')
print("data1 = ", data1, type(data1))

# 用find_one()方法进行node查找，返回的是查找node的第一个node
data2 = graph.find_one(label='Form')
print("data2 = ", data2, type(data2))

# 用find()方法进行node查找,需要遍历输出，类似于mongodb
data3 = graph.find(label='Form')
for data in data3:
    print("data3 = ", data)

# Relationship查询
relationship = graph.match_one(rel_type='Sub')
print(relationship, type(relationship))
