# -*- coding: utf-8 -*-

from py2neo import Graph


class Nodes(object):
    """知识图谱数据接口"""

    def __init__(self):
        """初始化数据"""
        # 与neo4j服务器建立连接
        self.graph = Graph("http://139.224.129.150:7474/browser/", username="neo4j", password="BIT!smartteam")

    def post(self):
        """与前端交互"""
        # 前端传过来的数据
        # 取出所有节点数据
        nodes_data_all = self.graph.run("MATCH (n) RETURN n").data()
        # node名存储
        name_list = []
        for node in nodes_data_all:
            name = node['n']['name'] or node['n']['tag_name']
            name_list.append(name)
        return name_list

nodes = Nodes()
nodes_list = [str(i) for i in nodes.post()]
result = '\n'.join(nodes_list)
with open('nodes.txt', 'w', encoding='utf-8') as f:
    f.write(result)