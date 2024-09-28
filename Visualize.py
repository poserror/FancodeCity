import requests
import matplotlib.pyplot as plt
from fpdf import FPDF
from services.user_service import get_users

class TodoGraphService:
    def __init__(self, users):
        self.users = users

    def get_todo_completion_data(self):
        completion_data = []
        
        for user in self.users:
            todos = self.get_todos_by_user(user['id'])
            if not todos:
                continue
            
            completed_tasks = sum(1 for todo in todos if todo['completed'])
            total_tasks = len(todos)

            if total_tasks > 0:
                completion_percentage = (completed_tasks / total_tasks) * 100
                completion_data.append((user['name'], completion_percentage, total_tasks, completed_tasks))

        return completion_data

    def get_todos_by_user(self, user_id):
        try:
            response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={user_id}')
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred for user {user_id}: {err}")
            return []

    def create_completion_graphs(self, data):
        names = [item[0] for item in data]
        total_todos = [item[2] for item in data]
        completed_todos = [item[3] for item in data]

        # Pie Chart for Overall Completion
        plt.figure(figsize=(8, 8))
        total_completed = sum(completed_todos)
        total_not_completed = sum(total_todos) - total_completed
        plt.pie([total_completed, total_not_completed], labels=['Completed', 'Not Completed'], 
                autopct='%1.5f%%', startangle=140)
        plt.title('Overall Todo Completion')
        plt.savefig('overall_completion_pie_chart.png')
        plt.close()

        # Stacked Bar Chart for Individual User Completion
        plt.figure(figsize=(10, 6))
        bar_width = 0.4
        index = range(len(names))

        plt.bar(index, completed_todos, bar_width, label='Completed', color='g')
        plt.bar(index, [total - completed for total, completed in zip(total_todos, completed_todos)], 
                 bar_width, bottom=completed_todos, label='Not Completed', color='r')

        plt.xlabel('Users')
        plt.ylabel('Number of Todos')
        plt.title('Todo Completion by User')
        plt.xticks(index, names, rotation=45, ha='right')
        plt.legend()

        plt.tight_layout()
        plt.savefig('todo_completion_by_user.png')
        plt.close()

    def create_pdf_report(self):
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt="Todo Completion Report", ln=True, align='C')

        # Add Pie Chart
        pdf.image('overall_completion_pie_chart.png', x=10, y=30, w=90)
        pdf.cell(0, 10, '', ln=True)  # Line break

        # Add Stacked Bar Chart
        pdf.image('todo_completion_by_user.png', x=10, y=120, w=190)

        pdf.output("todo_completion_report.pdf")

    def generate_report(self):
        completion_data = self.get_todo_completion_data()
        if not completion_data:
            print("No data available to generate the report.")
            return

        self.create_completion_graphs(completion_data)
        self.create_pdf_report()
        print("PDF report generated: todo_completion_report.pdf")

# Example usage
if __name__ == "__main__":
    users = get_users()
    todo_graph_service = TodoGraphService(users)
    todo_graph_service.generate_report()
