from langgraph.graph import StateGraph, START, END, MessagesState
from langchain_core.runnables.graph import MermaidDrawMethod

def node1(state: MessagesState) -> MessagesState:
    return state
def node2(state: MessagesState) -> MessagesState:
    return state
def node3(state: MessagesState) -> MessagesState:
    return state

subgraph = (
    StateGraph(MessagesState)
    .add_node(node1)
    .add_node(node2)
    .add_node(node3)
    .add_edge(START, "node1")
    .add_edge("node1", "node2")
    .add_edge("node1", "node3")
    .add_edge("node2", END)
    .add_edge("node3", END)
    .compile()
)
def node4(state: MessagesState) -> MessagesState:
    return state
def node5(state: MessagesState) -> MessagesState:
    return state
def node6(state: MessagesState) -> MessagesState:
    return state

graph = (
    StateGraph(MessagesState)
    .add_node(node4)
    .add_node(node5)
    .add_node(node6)
    .add_node("sgraph", subgraph)
    .add_edge(START, "node4")
    .add_edge("node4", "node5")
    .add_edge("node4", "sgraph")
    .add_edge("node5", "node6")
    .add_edge("sgraph", "node6")
    .add_edge("node6", END)
    .compile()
)

try:
    # graph.get_graph().draw_mermaid_png(output_file_path="test.png", draw_method=MermaidDrawMethod.PYPPETEER)
    print(graph.get_graph(xray=True).draw_mermaid())
except Exception as e:
    print(e)