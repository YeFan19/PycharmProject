# -*- coding: utf-8 -*-

from py2neo import Graph
import json
import re


class Neo4j(object):
    """知识图谱数据接口"""

    def __init__(self):
        """初始化数据"""
        # 与neo4j服务器建立连接
        self.graph = Graph("http://139.224.129.150:7474/browser/", username="neo4j", password="BIT!smartteam")
        self.nodes = []



    def get_all_nodes(self, nodes_data):
        """获取知识图谱中所有节点数据"""
        dict_node = {}
        for node in nodes_data:
            name = node['n']['name']
            tag = node['n']['tag_name']
            dict_node['name'] = name
            dict_node['tag'] = tag
            self.nodes.append(dict_node)
            dict_node = {}
        return self.nodes

        print(self.nodes)

neo4j = Neo4j()



with open('nodes.txt', 'w', encoding='utf-8') as f:
    f.write(neo4j.get_all_nodes())
