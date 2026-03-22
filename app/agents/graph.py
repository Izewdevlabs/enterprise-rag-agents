from typing import TypedDict, Any
from langgraph.graph import StateGraph, END
from app.agents.tools import tool_retrieve
from app.rag.generator import generate_answer
from app.agents.verifier import verify_answer


class State(TypedDict, total=False):
    question: str
    plan: str
    docs: Any
    answer: str
    verification: str


def planner_node(state: State) -> State:
    q = state["question"]
    state["plan"] = (
        f"Retrieve relevant chunks for: {q}. Generate a grounded answer. Verify the answer."
    )
    return state


def retrieve_node(state: State) -> State:
    print("DEBUG: graph retrieve_node")
    state["docs"] = tool_retrieve(state["question"])
    return state


def answer_node(state: State) -> State:
    print("DEBUG: graph answer_node")
    state["answer"] = generate_answer(state["question"], state["docs"])
    return state


def verify_node(state: State) -> State:
    print("DEBUG: graph verify_node")
    try:
        state["verification"] = verify_answer(state["answer"], state["docs"])
    except Exception as e:
        state["verification"] = (
            f'{{"supported": false, "reason": "Verifier failed: {str(e)}"}}'
        )
    return state


def decision_node(state: State) -> str:
    return "final"


def build_graph():
    g = StateGraph(State)
    g.add_node("plan", planner_node)
    g.add_node("retrieve", retrieve_node)
    g.add_node("answer", answer_node)
    g.add_node("verify", verify_node)

    g.set_entry_point("plan")
    g.add_edge("plan", "retrieve")
    g.add_edge("retrieve", "answer")
    g.add_edge("answer", "verify")
    g.add_conditional_edges("verify", decision_node, {"final": END})

    return g.compile()
