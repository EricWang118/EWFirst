from __future__ import annotations

import tkinter as tk
from dataclasses import dataclass, field
from tkinter import ttk
from typing import Dict, List


@dataclass
class EventItem:
    title: str
    category: str
    status: str
    date_text: str
    priority: str
    audience: str
    server_scope: str
    summary: str
    rewards: List[str] = field(default_factory=list)
    highlights: List[str] = field(default_factory=list)
    strategy: List[str] = field(default_factory=list)
    tips: str = ""


EVENTS = [
    EventItem(
        title="\u6625\u65e5\u6a31\u82b1\u5b63 / \u5e9f\u571f\u6625\u65e5",
        category="\u4e3b\u6d3b\u52a8",
        status="\u8fdb\u884c\u4e2d",
        date_text="03/18 \u7ecf\u5178\u670d\u5f00\u542f\uff0c03/19 \u7b80\u5355\u751f\u5b58\u4e13\u670d\u5f00\u542f",
        priority="\u6700\u9ad8",
        audience="\u767d\u5ad6\u3001\u56de\u5751\u3001\u65b0\u670d\u73a9\u5bb6",
        server_scope="\u7ecf\u5178\u670d / \u7b80\u5355\u751f\u5b58\u4e13\u670d / \u65b0\u670d\u8054\u52a8",
        summary="\u5f53\u524d\u7248\u672c\u7684\u5934\u53f7\u4e3b\u6d3b\u52a8\uff0c\u6574\u5408\u4e86\u6625\u65e5\u798f\u5229\u3001\u6d3b\u8dc3\u4efb\u52a1\u4e0e\u65b0\u670d\u52a0\u7801\u5185\u5bb9\u3002",
        rewards=[
            "\u767b\u5f55\u798f\u5229",
            "\u9884\u7ea6\u5956\u52b1",
            "\u91c7\u96c6\u6389\u843d",
            "\u6625\u65e5\u4e3b\u9898\u9053\u5177",
            "\u65b0\u670d\u52a0\u7801",
        ],
        highlights=[
            "\u662f\u9996\u9875\u5e94\u8be5\u9876\u5728\u6700\u524d\u9762\u7684\u5185\u5bb9\u3002",
            "\u4e0d\u662f\u5355\u4e00\u73a9\u6cd5\uff0c\u800c\u662f\u4e00\u6574\u5305\u6625\u65e5\u798f\u5229\u5408\u96c6\u3002",
            "\u5bf9\u767d\u5ad6\u548c\u56de\u5751\u73a9\u5bb6\u7279\u522b\u6709\u4ef7\u503c\u3002",
        ],
        strategy=[
            "\u5148\u628a\u767b\u5f55\u3001\u9884\u7ea6\u3001\u6d3b\u8dc3\u4efb\u52a1\u6e05\u6389\u3002",
            "\u518d\u8865\u91c7\u96c6\u3001\u6253\u602a\u3001\u9493\u9c7c\u8fd9\u7c7b\u80fd\u987a\u624b\u505a\u7684\u9879\u76ee\u3002",
            "\u65b0\u670d\u73a9\u5bb6\u4f18\u5148\u5403\u6ee1\u7ed1\u5b9a\u5956\u52b1\u3002",
        ],
        tips="\u63a8\u8350\u4f5c\u4e3a\u9996\u9875\u7f6e\u9876\u5361\u7247\u3002",
    ),
    EventItem(
        title="\u7279\u6218\u5dc5\u5cf0\u8d5b\u6d4b\u8bd5",
        category="\u7ade\u6280",
        status="\u6700\u540e\u4e00\u5929",
        date_text="03/20 - 03/22",
        priority="\u9ad8",
        audience="PVP \u73a9\u5bb6\u3001\u7ec4\u961f\u73a9\u5bb6",
        server_scope="\u8d5b\u4e8b\u6d4b\u8bd5",
        summary="\u7ade\u6280\u5411\u6d4b\u8bd5\u6d3b\u52a8\uff0c\u76f8\u5173\u53cd\u9988\u4f1a\u5f71\u54cd 2026 \u6b63\u5f0f\u8d5b\u4e8b\u89c4\u5219\u3002",
        rewards=["\u53c2\u4e0e\u4f53\u9a8c", "\u7ec4\u961f\u5bf9\u6297", "\u6d77\u9009 / \u5c0f\u7ec4 / \u6dd8\u6c70\u9636\u6bb5"],
        highlights=[
            "\u4eca\u5929\u662f\u6700\u540e\u7a97\u53e3\u671f\uff0c\u5e94\u8be5\u5728\u9996\u9875\u663e\u8457\u63d0\u9192\u3002",
            "\u4e0d\u5e94\u53ea\u5f53\u6210\u65b0\u95fb\uff0c\u800c\u662f\u8981\u505a\u6210\u53ef\u4ee5\u70b9\u8fdb\u53bb\u770b\u7684\u7ade\u6280\u5165\u53e3\u3002",
            "\u9002\u5408\u5c55\u793a\u8d5b\u7a0b\u3001\u62a5\u540d\u65b9\u5f0f\u3001\u7ec4\u961f\u8981\u6c42\u3002",
        ],
        strategy=[
            "PVP \u73a9\u5bb6\u4f18\u5148\u67e5\u770b\u3002",
            "\u666e\u901a\u73a9\u5bb6\u53ef\u4ee5\u653e\u5728\u6625\u65e5\u798f\u5229\u4e4b\u540e\u518d\u770b\u3002",
            "\u9996\u9875\u5e94\u8be5\u5e26\u6709\u5f3a\u70c8\u7684\u65f6\u6548\u63d0\u793a\u3002",
        ],
        tips="\u540e\u7eed\u53ef\u4ee5\u6269\u5c55\u6210\u52a8\u6001\u5012\u8ba1\u65f6\u3002",
    ),
    EventItem(
        title="\u9752\u677e\u5b63\u51cf\u8d1f",
        category="\u7248\u672c\u4f18\u5316",
        status="\u63a8\u8350\u5173\u6ce8",
        date_text="03 \u6708\u7248\u672c\u4f18\u5316\u4e13\u9898",
        priority="\u9ad8",
        audience="\u8001\u73a9\u5bb6\u3001\u56de\u5751\u515a\u3001\u517b\u8001\u515a",
        server_scope="\u5168\u670d\u5411",
        summary="\u56f4\u7ed5\u5e84\u56ed\u3001\u517b\u6210\u3001\u65e5\u5e38\u7cfb\u7edf\u7684\u51cf\u8d1f\u4f18\u5316\uff0c\u5c5e\u4e8e\u65f6\u95f4\u4ef7\u503c\u578b\u5185\u5bb9\u3002",
        rewards=["\u66f4\u7701\u65f6\u7684\u65e5\u5e38", "\u66f4\u8f7b\u7684\u517b\u6210\u6d41\u7a0b", "\u56de\u5751\u4f53\u9a8c\u6539\u5584"],
        highlights=[
            "\u4e0d\u662f\u9886\u5956\u6d3b\u52a8\uff0c\u4f46\u5bf9\u957f\u671f\u4f53\u9a8c\u975e\u5e38\u91cd\u8981\u3002",
            "\u5f88\u591a\u73a9\u5bb6\u4f1a\u5148\u95ee\u73b0\u5728\u8fd8\u809d\u4e0d\u809d\u3002",
            "\u9002\u5408\u5355\u72ec\u505a\u6210\u201c\u672c\u5468\u51cf\u8d1f / \u7248\u672c\u4f18\u5316\u201d\u680f\u76ee\u3002",
        ],
        strategy=[
            "\u56de\u5751\u73a9\u5bb6\u5148\u770b\u8fd9\u4e00\u680f\uff0c\u518d\u51b3\u5b9a\u662f\u5426\u56de\u5f52\u3002",
            "\u4f11\u95f2\u73a9\u5bb6\u4f18\u5148\u770b\u65e5\u5e38\u548c\u5e84\u56ed\u76f8\u5173\u4f18\u5316\u3002",
            "\u53ef\u4ee5\u628a\u8fd9\u4e00\u680f\u7684\u6838\u5fc3\u5356\u70b9\u5199\u6210\u201c\u7701\u65f6\u95f4\u201d\u3002",
        ],
        tips="\u8fd9\u4e2a\u680f\u76ee\u80fd\u8ba9\u8f6f\u4ef6\u4e0d\u53ea\u662f\u770b\u5956\u6c60\u3002",
    ),
    EventItem(
        title="\u6625\u82d1\u60e0\u9009\u00b7\u7eff\u91ce\u4ed9\u8e2a",
        category="\u5956\u6c60",
        status="\u4e0a\u65b0",
        date_text="03/19 \u4e0a\u7ebf",
        priority="\u4e2d\u9ad8",
        audience="\u5e84\u56ed\u515a\u3001\u5efa\u7b51\u515a\u3001\u62cd\u7167\u515a",
        server_scope="\u5bb6\u5177\u6c60",
        summary="\u4ea4\u4e92\u6027\u5f88\u5f3a\u7684\u7ae5\u8bdd\u98ce\u5bb6\u5177\u5956\u6c60\uff0c\u5f88\u9002\u5408\u5355\u72ec\u505a\u8be6\u60c5\u9875\u3002",
        rewards=["\u53d8\u5c0f\u9b54\u6cd5\u5bb6\u5177", "\u4ed9\u8e2a\u843d\u5730\u949f", "\u5947\u5e7b\u8336\u676f", "\u6811\u6d1e\u5e8a", "\u85e4\u8513\u8eba\u6905"],
        highlights=[
            "\u5efa\u7b51\u515a\u548c\u5e84\u56ed\u73a9\u5bb6\u4f1a\u5f88\u5728\u610f\u8fd9\u4e2a\u6c60\u5b50\u3002",
            "\u9002\u5408\u6253\u4e0a\u4ea4\u4e92\u5bb6\u5177\u3001\u6625\u5b63\u4e3b\u9898\u3001\u89c6\u89c9\u5411\u6807\u7b7e\u3002",
            "\u5e94\u8be5\u6709\u201c\u9002\u5408\u8c01\u62bd\u201d\u8fd9\u79cd\u5224\u65ad\u8bf4\u660e\u3002",
        ],
        strategy=[
            "\u5efa\u7b51\u515a\u5148\u770b\u4ea4\u4e92\u4ef6\u548c\u6c1b\u56f4\u4ef6\u3002",
            "\u6218\u529b\u73a9\u5bb6\u53ef\u4ee5\u653e\u5728\u798f\u5229\u548c\u6838\u82af\u540e\u518d\u8003\u8651\u3002",
            "\u8be6\u60c5\u9875\u5e94\u8be5\u7a81\u51fa\u4ea4\u4e92\u4ef7\u503c\u3002",
        ],
        tips="\u9002\u5408\u505a\u6210\u56fe\u9274\u611f\u5f88\u5f3a\u7684\u680f\u76ee\u3002",
    ),
    EventItem(
        title="\u65b0\u6838\u82af\u00b7\u84c4\u52bf\u5bd2\u950b",
        category="\u6218\u6597\u517b\u6210",
        status="\u4e0a\u65b0",
        date_text="03/21 \u4e0a\u7ebf",
        priority="\u9ad8",
        audience="\u6b66\u58eb\u3001\u8fd1\u6218\u6d41\u3001PVP/PVE \u53cc\u4fee",
        server_scope="\u6218\u6597\u7cfb\u7edf",
        summary="\u504f\u8fd1\u6218\u7684\u65b0\u6838\u82af\uff0c\u517c\u987e\u4f24\u5bb3\u3001\u6297\u4f24\u548c\u5f62\u6001\u5207\u6362\u3002",
        rewards=["\u706b\u529b\u63d0\u5347", "\u4f24\u5bb3\u6297\u6027", "\u5bd2\u950b\u5f62\u6001", "\u84c4\u529b\u91cd\u65a9", "\u5feb\u901f\u8fde\u65a9"],
        highlights=[
            "\u5bf9\u8fd1\u6218\u548c PVP \u73a9\u5bb6\u7279\u522b\u91cd\u8981\u3002",
            "\u661f\u7ea7\u63d0\u5347\u540e\u7684\u6218\u529b\u53d8\u5316\u5f88\u660e\u663e\u3002",
            "\u5f88\u9002\u5408\u540e\u7eed\u6269\u5c55\u6210\u653b\u7565\u9875\u3002",
        ],
        strategy=[
            "\u6218\u529b\u73a9\u5bb6\u5e94\u8be5\u5148\u770b\u673a\u5236\u548c\u517b\u6210\u4f18\u5148\u7ea7\u3002",
            "\u53ef\u4ee5\u5355\u72ec\u5199\u201c\u9002\u5408\u804c\u4e1a\u201d\u3002",
            "\u540e\u7eed\u8fd8\u80fd\u8ffd\u52a0\u8fde\u62db\u4e0e\u642d\u914d\u601d\u8def\u3002",
        ],
        tips="\u662f\u5f53\u524d\u6700\u503c\u5f97\u6df1\u6316\u7684\u6218\u6597\u680f\u76ee\u4e4b\u4e00\u3002",
    ),
    EventItem(
        title="\u5e9f\u571f\u5f88\u5fd9",
        category="\u8fd1\u671f\u5916\u89c2",
        status="\u4e0a\u65b0",
        date_text="03/19 \u4e0a\u7ebf",
        priority="\u4e2d",
        audience="\u65f6\u88c5\u515a\u3001\u6536\u85cf\u515a",
        server_scope="\u65f6\u88c5\u6c60",
        summary="\u897f\u90e8\u725b\u4ed4\u4e0e\u5e9f\u571f\u98ce\u683c\u7ed3\u5408\u7684\u5916\u89c2\u5185\u5bb9\uff0c\u66f4\u504f\u6d88\u8d39\u578b\u3002",
        rewards=["\u65b0\u65f6\u88c5\u5916\u89c2", "\u5e9f\u571f\u4e3b\u9898\u98ce\u683c"],
        highlights=[
            "\u9002\u5408\u653e\u5728\u65b0\u65f6\u88c5\u680f\u76ee\uff0c\u4e0d\u8981\u538b\u8fc7\u4e3b\u6d3b\u52a8\u3002",
            "\u89c6\u89c9\u98ce\u683c\u9c9c\u660e\uff0c\u4f46\u529f\u80fd\u4ef7\u503c\u4e0d\u9ad8\u3002",
        ],
        strategy=[
            "\u66f4\u9002\u5408\u505a\u56fe\u9274\u5c55\u793a\u3002",
            "\u53ef\u4e0e\u5176\u4ed6\u8fd1\u671f\u5916\u89c2\u4e00\u8d77\u6bd4\u8f83\u3002",
        ],
        tips="\u4f5c\u4e3a\u8865\u5145\u680f\u76ee\u5f88\u5408\u9002\u3002",
    ),
    EventItem(
        title="\u6a31\u7075\u72d0\u68a6",
        category="\u8fd1\u671f\u5916\u89c2",
        status="\u672c\u6708\u70ed\u95e8",
        date_text="03/12 \u4e0a\u7ebf",
        priority="\u4e2d",
        audience="\u6625\u65e5\u5916\u89c2\u515a\u3001\u52a8\u4f5c\u6536\u96c6\u515a",
        server_scope="\u65f6\u88c5\u6d3b\u52a8",
        summary="\u5177\u6709\u6625\u65e5\u611f\u7684\u5916\u89c2\u5185\u5bb9\uff0c\u5305\u542b\u52a8\u4f5c\u3001\u5934\u9970\u7b49\u9650\u5b9a\u8981\u7d20\u3002",
        rewards=["\u5934\u9970", "\u80cc\u5305", "\u52a8\u4f5c", "\u9650\u5b9a\u5916\u89c2"],
        highlights=[
            "\u9002\u5408\u653e\u5728\u672c\u6708\u70ed\u95e8\u5916\u89c2\u533a\u57df\u3002",
            "\u5c55\u793a\u4ef7\u503c\u9ad8\uff0c\u4f46\u4f18\u5148\u7ea7\u4f4e\u4e8e\u4e3b\u6d3b\u52a8\u3002",
        ],
        strategy=[
            "\u9002\u5408\u653e\u5728\u7b2c\u4e8c\u5c4f\u6216\u8fd1\u671f\u4e0a\u65b0\u9875\u3002",
            "\u53ef\u4ee5\u4e0e\u5bb6\u5177\u6c60\u4e00\u8d77\u505a\u89c6\u89c9\u4e3b\u9898\u63a8\u8350\u3002",
        ],
        tips="\u540e\u7eed\u52a0\u5165\u622a\u56fe\u4f1a\u66f4\u597d\u770b\u3002",
    ),
    EventItem(
        title="3 \u6708\u4e0a\u65ec\u798f\u5229\u5408\u96c6",
        category="\u8fd1\u671f\u56de\u987e",
        status="\u5df2\u8fc7\u534a",
        date_text="03/04 \u8d77\u9646\u7eed\u4e0a\u7ebf",
        priority="\u4e2d",
        audience="\u8865\u8bfe\u73a9\u5bb6\u3001\u56de\u987e\u515a",
        server_scope="\u7ecf\u5178\u670d / \u7b80\u5355\u751f\u5b58\u4e13\u670d",
        summary="\u6536\u7eb3\u4e86 3 \u6708\u4e0a\u534a\u6708\u7684\u798f\u5229\u3001\u767b\u5f55\u5956\u52b1\u548c\u4e00\u4e9b\u4fbf\u5229\u6027\u66f4\u65b0\u3002",
        rewards=["\u5bb6\u5177\u81ea\u9009\u7bb1", "1 \u5143\u6708\u5361", "\u767b\u5f55\u5956\u52b1", "\u529f\u80fd\u4f18\u5316"],
        highlights=[
            "\u9002\u5408\u505a\u6210\u65f6\u95f4\u7ebf\u6216\u672c\u6708\u56de\u987e\u3002",
            "\u80fd\u8ba9\u73a9\u5bb6\u533a\u5206\u73b0\u5728\u505a\u4ec0\u4e48\u3001\u4e4b\u524d\u51fa\u8fc7\u4ec0\u4e48\u3002",
        ],
        strategy=[
            "\u9002\u5408\u7ed9\u9519\u8fc7\u524d\u534a\u6708\u5185\u5bb9\u7684\u73a9\u5bb6\u8865\u8bfe\u3002",
            "\u53ef\u4ee5\u540e\u7eed\u7ee7\u7eed\u8ffd\u52a0\u6bcf\u6708\u6863\u6848\u3002",
        ],
        tips="\u662f\u8f6f\u4ef6\u505a\u957f\u671f\u4fe1\u606f\u6574\u7406\u7684\u597d\u8d77\u70b9\u3002",
    ),
    EventItem(
        title="\u4eba\u5076\u5951\u7ea6",
        category="\u5386\u53f2\u4e0b\u67b6",
        status="\u5df2\u4e0b\u67b6",
        date_text="03/12 03:00 \u4e0b\u67b6",
        priority="\u8bb0\u5f55",
        audience="\u56fe\u9274\u515a\u3001\u8fd4\u573a\u5173\u6ce8\u73a9\u5bb6",
        server_scope="\u5386\u53f2\u6863\u6848",
        summary="\u5df2\u7ecf\u4e0b\u67b6\uff0c\u66f4\u9002\u5408\u653e\u5165\u201c\u6700\u8fd1\u4e0b\u67b6 / \u9519\u8fc7\u63d0\u9192\u201d\u5206\u533a\u3002",
        rewards=["\u5386\u53f2\u5916\u89c2\u6863\u6848", "\u8fd4\u573a\u53c2\u8003\u8bb0\u5f55"],
        highlights=[
            "\u4e0d\u518d\u5c5e\u4e8e\u5f53\u524d\u6d3b\u52a8\uff0c\u4f46\u5386\u53f2\u68c0\u7d22\u4ef7\u503c\u5f88\u9ad8\u3002",
            "\u540e\u7eed\u53ef\u4ee5\u6269\u5c55\u6210\u8fd4\u573a\u8ffd\u8e2a\u3002",
        ],
        strategy=[
            "\u5efa\u8bae\u72ec\u7acb\u653e\u8fdb\u5386\u53f2\u5206\u533a\u3002",
            "\u4fbf\u4e8e\u4e4b\u540e\u67e5\u201c\u4ec0\u4e48\u65f6\u5019\u4e0a\u8fc7\u201d\u3002",
        ],
        tips="\u5386\u53f2\u680f\u4f1a\u8ba9\u8fd9\u4e2a\u8f6f\u4ef6\u66f4\u8010\u7528\u3002",
    ),
]


AUDIENCE_GUIDES: Dict[str, List[str]] = {
    "\u767d\u5ad6 / \u5e73\u6c11": [
        "\u4f18\u5148\u987a\u5e8f\uff1a\u6625\u65e5\u4e3b\u6d3b\u52a8 > \u767b\u5f55/\u9884\u7ea6\u5956\u52b1 > \u9752\u677e\u5b63\u51cf\u8d1f > \u65b0\u670d\u798f\u5229 > \u7ade\u6280\u6d4b\u8bd5 > \u5916\u89c2\u6c60",
        "\u5148\u62ff\u7a33\u5b9a\u8d44\u6e90\u548c\u6548\u7387\uff0c\u518d\u8003\u8651\u7eaf\u5c55\u793a\u5411\u5185\u5bb9\u3002",
    ],
    "\u56de\u5751\u73a9\u5bb6": [
        "\u5148\u770b\u9752\u677e\u5b63\u51cf\u8d1f\uff0c\u518d\u770b\u6625\u65e5\u798f\u5229\u548c\u65b0\u670d\u4fe1\u606f\u3002",
        "\u6838\u5fc3\u662f\u5224\u65ad\u73b0\u5728\u56de\u5751\u503c\u4e0d\u503c\u5f97\u3002",
    ],
    "\u5e84\u56ed / \u5efa\u7b51\u515a": [
        "\u91cd\u70b9\u770b\u7eff\u91ce\u4ed9\u8e2a\u5bb6\u5177\u6c60\u3001\u6625\u65e5\u6c1b\u56f4\u5185\u5bb9\u548c\u672c\u6708\u65f6\u88c5\u3002",
        "\u8fd9\u6ce2\u89c6\u89c9\u4e3b\u9898\u5f88\u7edf\u4e00\uff0c\u5f88\u9002\u5408\u5c55\u793a\u3002",
    ],
    "\u6218\u529b / PVP": [
        "\u5148\u770b\u7279\u6218\u5dc5\u5cf0\u8d5b\uff0c\u518d\u770b\u84c4\u52bf\u5bd2\u950b\u3002",
        "\u4e00\u4e2a\u5f71\u54cd\u53c2\u8d5b\u65f6\u673a\uff0c\u4e00\u4e2a\u5f71\u54cd\u5b9e\u6218\u642d\u914d\u3002",
    ],
}


class DetailWindow(tk.Toplevel):
    def __init__(self, master: tk.Misc, item: EventItem) -> None:
        super().__init__(master)
        self.title(item.title)
        self.configure(bg="#F3F6FF")
        self.geometry("420x720")
        self.minsize(380, 600)

        outer = tk.Frame(self, bg="#F3F6FF", padx=16, pady=16)
        outer.pack(fill="both", expand=True)

        tk.Label(
            outer,
            text=item.title,
            font=("Microsoft YaHei UI", 18, "bold"),
            fg="#20304A",
            bg="#F3F6FF",
            anchor="w",
            justify="left",
        ).pack(fill="x")

        tk.Label(
            outer,
            text=f"{item.category} | {item.status}\n{item.date_text}\n\u9002\u5408\uff1a{item.audience} | \u8303\u56f4\uff1a{item.server_scope}",
            font=("Microsoft YaHei UI", 10),
            fg="#6E7D96",
            bg="#F3F6FF",
            anchor="w",
            justify="left",
        ).pack(fill="x", pady=(8, 12))

        text = tk.Text(
            outer,
            wrap="word",
            font=("Microsoft YaHei UI", 10),
            bg="#FCFDFF",
            fg="#20304A",
            relief="flat",
            padx=14,
            pady=14,
        )
        text.pack(fill="both", expand=True)

        def add_block(title_text: str, lines: List[str]) -> None:
            text.insert("end", f"{title_text}\n", ("heading",))
            for line in lines:
                text.insert("end", f"\u2022 {line}\n")
            text.insert("end", "\n")

        add_block("\u73a9\u6cd5\u6458\u8981", [item.summary])
        add_block("\u6838\u5fc3\u4eae\u70b9", item.highlights)
        add_block("\u53ef\u5173\u6ce8\u5956\u52b1", item.rewards)
        add_block("\u63a8\u8350\u987a\u5e8f", item.strategy)
        add_block("\u5b9e\u6218\u5efa\u8bae", [item.tips])

        text.tag_configure("heading", font=("Microsoft YaHei UI", 11, "bold"), foreground="#3E6FDD")
        text.config(state="disabled")

        tk.Button(
            outer,
            text="\u5173\u95ed\u8be6\u60c5",
            command=self.destroy,
            bg="#5D8CFF",
            fg="white",
            activebackground="#3E6FDD",
            activeforeground="white",
            relief="flat",
            font=("Microsoft YaHei UI", 10, "bold"),
            pady=10,
        ).pack(fill="x", pady=(12, 0))


class LifeAfterEventApp:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("\u660e\u65e5\u4e4b\u540e\u6d3b\u52a8\u6574\u5408\u5668")
        self.root.geometry("430x860")
        self.root.minsize(390, 700)
        self.root.configure(bg="#F3F6FF")

        self.current_category = "\u5168\u90e8"
        self.current_audience = "\u767d\u5ad6 / \u5e73\u6c11"
        self.category_buttons: Dict[str, tk.Button] = {}
        self.audience_buttons: Dict[str, tk.Button] = {}
        self.canvas_window = None

        self._setup_style()
        self._build_ui()
        self.refresh_events()
        self.refresh_guide()

    def _setup_style(self) -> None:
        style = ttk.Style()
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass
        style.configure("Viewer.Vertical.TScrollbar", troughcolor="#EDF3FF", background="#9CB8FF")

    def _build_ui(self) -> None:
        page = tk.Frame(self.root, bg="#F3F6FF")
        page.pack(fill="both", expand=True)

        hero = tk.Frame(page, bg="#EAF0FF", height=190)
        hero.pack(fill="x", padx=16, pady=(16, 10))
        hero.pack_propagate(False)

        tk.Label(
            hero,
            text="2026-03-22 \u516c\u5f00\u4fe1\u606f\u6574\u5408",
            font=("Microsoft YaHei UI", 9, "bold"),
            fg="#3E6FDD",
            bg="#DCE8FF",
            padx=12,
            pady=6,
        ).pack(anchor="w", padx=16, pady=(16, 10))

        tk.Label(
            hero,
            text="\u660e\u65e5\u4e4b\u540e\n\u6d3b\u52a8 / \u5956\u6c60 / \u653b\u7565\u67e5\u770b\u5668",
            font=("Microsoft YaHei UI", 21, "bold"),
            fg="#20304A",
            bg="#EAF0FF",
            justify="left",
            anchor="w",
        ).pack(fill="x", padx=16)

        tk.Label(
            hero,
            text="\u9996\u9875\u5148\u770b\u4e3b\u6d3b\u52a8\uff0c\u518d\u6309\u5206\u7c7b\u548c\u73a9\u6cd5\u5b9a\u4f4d\u81ea\u5df1\u6700\u8be5\u770b\u7684\u680f\u76ee\u3002",
            font=("Microsoft YaHei UI", 10),
            fg="#6E7D96",
            bg="#EAF0FF",
            justify="left",
            anchor="w",
        ).pack(fill="x", padx=16, pady=(8, 0))

        self.featured_label = tk.Label(
            hero,
            text="",
            font=("Microsoft YaHei UI", 10, "bold"),
            fg="#3E6FDD",
            bg="#EAF0FF",
            justify="left",
            anchor="w",
        )
        self.featured_label.pack(fill="x", padx=16, pady=(10, 0))

        category_wrap = tk.Frame(page, bg="#F3F6FF")
        category_wrap.pack(fill="x", padx=16)

        self.category_map = {
            "\u5168\u90e8": None,
            "\u4e3b\u6d3b\u52a8": "\u4e3b\u6d3b\u52a8",
            "\u7ade\u6280": "\u7ade\u6280",
            "\u7248\u672c\u4f18\u5316": "\u7248\u672c\u4f18\u5316",
            "\u5956\u6c60": "\u5956\u6c60",
            "\u6218\u6597\u517b\u6210": "\u6218\u6597\u517b\u6210",
            "\u8fd1\u671f\u5916\u89c2": "\u8fd1\u671f\u5916\u89c2",
            "\u8fd1\u671f\u56de\u987e": "\u8fd1\u671f\u56de\u987e",
            "\u5386\u53f2\u4e0b\u67b6": "\u5386\u53f2\u4e0b\u67b6",
        }

        for name in self.category_map:
            btn = tk.Button(
                category_wrap,
                text=name,
                command=lambda value=name: self.set_category(value),
                relief="flat",
                padx=10,
                pady=8,
                font=("Microsoft YaHei UI", 9, "bold"),
            )
            btn.pack(side="left", padx=(0, 6), pady=(0, 10))
            self.category_buttons[name] = btn

        content = tk.Frame(page, bg="#F3F6FF")
        content.pack(fill="both", expand=True, padx=16)

        self.canvas = tk.Canvas(content, bg="#F3F6FF", highlightthickness=0)
        scrollbar = ttk.Scrollbar(content, orient="vertical", command=self.canvas.yview, style="Viewer.Vertical.TScrollbar")
        self.cards_frame = tk.Frame(self.canvas, bg="#F3F6FF")
        self.cards_frame.bind("<Configure>", lambda _event: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas_window = self.canvas.create_window((0, 0), window=self.cards_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        self.canvas.bind("<Configure>", self._resize_canvas_window)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        footer = tk.Frame(page, bg="#FCFDFF", highlightbackground="#D6E0F5", highlightthickness=1)
        footer.pack(fill="x", padx=16, pady=(10, 16))

        audience_bar = tk.Frame(footer, bg="#FCFDFF")
        audience_bar.pack(fill="x", padx=10, pady=(10, 6))

        for name in AUDIENCE_GUIDES:
            btn = tk.Button(
                audience_bar,
                text=name,
                command=lambda value=name: self.set_audience(value),
                relief="flat",
                padx=10,
                pady=6,
                font=("Microsoft YaHei UI", 9, "bold"),
            )
            btn.pack(side="left", padx=(0, 6))
            self.audience_buttons[name] = btn

        self.guide_title = tk.Label(
            footer,
            text="",
            font=("Microsoft YaHei UI", 12, "bold"),
            fg="#20304A",
            bg="#FCFDFF",
            anchor="w",
            justify="left",
        )
        self.guide_title.pack(fill="x", padx=14, pady=(4, 4))

        self.guide_text = tk.Label(
            footer,
            text="",
            font=("Microsoft YaHei UI", 10),
            fg="#6E7D96",
            bg="#FCFDFF",
            anchor="w",
            justify="left",
        )
        self.guide_text.pack(fill="x", padx=14, pady=(0, 12))

    def _resize_canvas_window(self, event: tk.Event) -> None:
        if self.canvas_window is not None:
            self.canvas.itemconfigure(self.canvas_window, width=event.width)

    def _on_mousewheel(self, event: tk.Event) -> None:
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def set_category(self, category: str) -> None:
        self.current_category = category
        self.refresh_events()

    def set_audience(self, audience: str) -> None:
        self.current_audience = audience
        self.refresh_guide()

    def filtered_events(self) -> List[EventItem]:
        mapped = self.category_map[self.current_category]
        if mapped is None:
            return EVENTS
        return [item for item in EVENTS if item.category == mapped]

    def refresh_events(self) -> None:
        for name, button in self.category_buttons.items():
            if name == self.current_category:
                button.configure(bg="#5D8CFF", fg="white", activebackground="#3E6FDD", activeforeground="white")
            else:
                button.configure(bg="#FCFDFF", fg="#20304A", activebackground="#EEF3FF", activeforeground="#20304A")

        for child in self.cards_frame.winfo_children():
            child.destroy()

        items = self.filtered_events()
        featured = items[0]
        self.featured_label.configure(text=f"\u5f53\u524d\u63a8\u8350\uff1a{featured.title} | {featured.date_text}\n\u9002\u5408\uff1a{featured.audience}")

        for item in items:
            self._add_event_card(item)

    def refresh_guide(self) -> None:
        for name, button in self.audience_buttons.items():
            if name == self.current_audience:
                button.configure(bg="#5D8CFF", fg="white", activebackground="#3E6FDD", activeforeground="white")
            else:
                button.configure(bg="#EEF3FF", fg="#20304A", activebackground="#DCE8FF", activeforeground="#20304A")

        self.guide_title.configure(text=f"{self.current_audience} \u73b0\u5728\u5148\u505a\u4ec0\u4e48")
        self.guide_text.configure(text="\n".join(AUDIENCE_GUIDES[self.current_audience]))

    def _add_event_card(self, item: EventItem) -> None:
        card = tk.Frame(self.cards_frame, bg="#FCFDFF", highlightbackground="#D6E0F5", highlightthickness=1, padx=14, pady=12)
        card.pack(fill="x", pady=(0, 12))

        top = tk.Frame(card, bg="#FCFDFF")
        top.pack(fill="x")

        tk.Label(
            top,
            text=item.category,
            font=("Microsoft YaHei UI", 9, "bold"),
            fg="#3E6FDD",
            bg="#EAF0FF",
            padx=10,
            pady=4,
        ).pack(side="left")

        tk.Label(
            top,
            text=item.status,
            font=("Microsoft YaHei UI", 9, "bold"),
            fg="#6E7D96",
            bg="#EEF3FF",
            padx=10,
            pady=4,
        ).pack(side="left", padx=(8, 0))

        tk.Label(
            card,
            text=item.title,
            font=("Microsoft YaHei UI", 14, "bold"),
            fg="#20304A",
            bg="#FCFDFF",
            anchor="w",
            justify="left",
        ).pack(fill="x", pady=(12, 6))

        tk.Label(
            card,
            text=item.summary,
            font=("Microsoft YaHei UI", 10),
            fg="#6E7D96",
            bg="#FCFDFF",
            anchor="w",
            justify="left",
            wraplength=340,
        ).pack(fill="x")

        tk.Label(
            card,
            text=f"{item.date_text}\n\u4f18\u5148\u7ea7\uff1a{item.priority} | \u9002\u5408\uff1a{item.audience}",
            font=("Microsoft YaHei UI", 10),
            fg="#20304A",
            bg="#FCFDFF",
            anchor="w",
            justify="left",
        ).pack(fill="x", pady=(10, 10))

        tk.Button(
            card,
            text="\u67e5\u770b\u8be6\u60c5",
            command=lambda selected=item: self.open_detail(selected),
            relief="flat",
            bg="#5D8CFF",
            fg="white",
            activebackground="#3E6FDD",
            activeforeground="white",
            font=("Microsoft YaHei UI", 10, "bold"),
            pady=8,
        ).pack(fill="x")

    def open_detail(self, item: EventItem) -> None:
        DetailWindow(self.root, item)

    def run(self) -> None:
        self.root.mainloop()


if __name__ == "__main__":
    LifeAfterEventApp().run()
