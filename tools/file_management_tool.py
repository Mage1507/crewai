from langchain_community.agent_toolkits import FileManagementToolkit


class FileManager:
    def __init__(self, selected_tools):
        self.tools = FileManagementToolkit(selected_tools=selected_tools).get_tools()

    def get_tool(self, index):
        return self.tools[index]
