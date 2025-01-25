from abc import ABC, abstractmethod


# Abstract Handler
class SupportHandler(ABC):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    @abstractmethod
    def handle_request(self, severity, issue):
        pass


# Concrete Handlers
class ChatbotHandler(SupportHandler):
    def handle_request(self, severity, issue):
        if severity == "low":
            print(f"Chatbot: Resolved the issue '{issue}'.")
        elif self.next_handler:
            self.next_handler.handle_request(severity, issue)
        else:
            print(f"Chatbot: Cannot handle the issue '{issue}'. Escalating.")


class AgentHandler(SupportHandler):
    def handle_request(self, severity, issue):
        if severity == "medium":
            print(f"Agent: Resolved the issue '{issue}'.")
        elif self.next_handler:
            self.next_handler.handle_request(severity, issue)
        else:
            print(f"Agent: Cannot handle the issue '{issue}'. Escalating.")


class TechnicalTeamHandler(SupportHandler):
    def handle_request(self, severity, issue):
        if severity == "high":
            print(f"Technical Team: Resolved the issue '{issue}'.")
        elif self.next_handler:
            self.next_handler.handle_request(severity, issue)
        else:
            print(f"Technical Team: Cannot handle the issue '{issue}'. Escalating.")


class ManagerHandler(SupportHandler):
    def handle_request(self, severity, issue):
        if severity == "critical":
            print(f"Manager: Resolved the critical issue '{issue}'.")
        elif self.next_handler:
            self.next_handler.handle_request(severity, issue)
        else:
            print(f"Manager: Cannot handle the issue '{issue}'. Logging as unresolved.")


# Client Code
if __name__ == "__main__":
    # Create the chain of responsibility
    manager_handler = ManagerHandler()
    tech_team_handler = TechnicalTeamHandler(manager_handler)
    agent_handler = AgentHandler(tech_team_handler)
    chatbot_handler = ChatbotHandler(agent_handler)

    # Example tickets
    tickets = [
        {"severity": "low", "issue": "Password reset"},
        {"severity": "medium", "issue": "Cannot connect to VPN"},
        {"severity": "high", "issue": "System crash on startup"},
        {"severity": "critical", "issue": "Data breach detected"},
        {"severity": "unknown", "issue": "Unusual error message"},
    ]

    # Process each ticket
    for ticket in tickets:
        print(f"\nProcessing ticket: {ticket['issue']} (Severity: {ticket['severity']})")
        chatbot_handler.handle_request(ticket["severity"], ticket["issue"])
