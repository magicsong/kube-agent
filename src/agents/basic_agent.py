import json
from typing import Annotated

from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain_core.messages import ToolMessage
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict
from langgraph.types import Command, interrupt
from ..tools.kubectl import KubeTool
from langgraph.prebuilt import ToolNode, tools_condition

from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()


class State(TypedDict):
    messages: Annotated[list, add_messages]


class ChatAgent:
    def __init__(self, model="deepseek-r1:70b", verbose=False, base_url=None):
        self.model = model
        self.verbose = verbose
        self.base_url = base_url
        self.memory = MemorySaver()
        
        # Initialize tools and graph
        self.tools, self.toolllm = self._create_agent()
        self.graph = self._build_graph()
    
    @staticmethod
    @tool
    def human_assistance(query: str) -> str:
        """Request assistance from a human."""
        human_response = interrupt({"query": query})
        return human_response["data"]
    
    def _create_agent(self):
        llm = ChatOllama(
            model=self.model,
            temperature=0.8,
            num_predict=8096,
            base_url=self.base_url,
        )
        
        kube_tool = KubeTool()
        tools = [kube_tool, self.human_assistance]
        
        toolllm = ChatOllama(
            model=self.model,
            temperature=0.8,
            num_predict=8096,
            base_url=self.base_url,
        ).bind_tools(tools)
        
        return tools, toolllm
    
    def _chatbot(self, state):
        message = self.toolllm.invoke(state["messages"])
        # Because we will be interrupting during tool execution,
        # we disable parallel tool calling to avoid repeating any
        # tool invocations when we resume.
        assert len(message.tool_calls) <= 1
        return {"messages": [message]}
    
    def _build_graph(self):
        graph_builder = StateGraph(State)
        
        # Add nodes
        graph_builder.add_node("chatbot", self._chatbot)
        tool_node = ToolNode(tools=self.tools)
        graph_builder.add_node("tools", tool_node)
        
        # Add edges
        graph_builder.add_conditional_edges(
            "chatbot",
            tools_condition,
        )
        graph_builder.add_edge("tools", "chatbot")
        
        # Set entry and finish points
        graph_builder.set_entry_point("chatbot")
        graph_builder.set_finish_point("chatbot")
        
        return graph_builder.compile(checkpointer=self.memory)
    
    def display_graph_in_terminal(self):
        """Display graph as an image in terminal if possible, otherwise save to file"""
        png_data = self.graph.get_graph().draw_mermaid_png()
        
        # Try using imgcat for iTerm2 users
        if os.environ.get("TERM_PROGRAM") == "iTerm.app":
            try:
                proc = subprocess.Popen(["imgcat"], stdin=subprocess.PIPE)
                proc.communicate(png_data)
                return
            except (FileNotFoundError, subprocess.SubprocessError):
                pass
        
        # Fallback: save to file
        with open("graph.png", "wb") as f:
            f.write(png_data)
        print("Graph visualization saved as 'graph.png'")
    
    def stream_graph_updates(self, user_input: str):
        config = {"configurable": {"thread_id": "1"}}
        for event in self.graph.stream(
            {"messages": [{"role": "user", "content": user_input}]},
            config=config,
            stream_mode="values",
        ):
            if "messages" in event:
                event["messages"][-1].pretty_print()
    
    def run(self):
        print("Welcome to the Basic Agent. Type 'exit' to quit.")
        
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                break
            self.stream_graph_updates(user_input)


class ChatAgent:
    def __init__(self, model="deepseek-r1:70b", verbose=False, base_url=None):
        self.model = model
        self.verbose = verbose
        self.base_url = base_url
        
        # Recreate the agent with the provided parameters
        global tools, toolllm
        tools, toolllm = create_agent(model_name=model, base_url=base_url)
        
        # Get the updated graph
        self.graph = graph

    def run(self):
        state = {"messages": []}
        print("Welcome to the Basic Agent. Type 'exit' to quit.")

        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                break
            stream_graph_updates(user_input)

            if self.verbose:
                print(f"Debug - Current state: {state}")
