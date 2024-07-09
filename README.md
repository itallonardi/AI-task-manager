# AI-task-manager

This project is an example of a LangChain agent for task management. The agent can add tasks, search for tasks based on their status, and delete tasks. This example does not use a real database, only simulated data for demonstration purposes.

## Setup

1. Clone the repository.
2. Create a `.env` file in the root directory with your OpenAI API key:
    ```
    OPENAI_API_KEY=your_openai_api_key_here
    ```
3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Run the FastAPI server:
    ```
    uvicorn app.main:app --reload
    ```

## Usage

The agent provides three main functions:
- `add_task`: Adds a new task with a description and due date.
- `search_tasks`: Searches for tasks with a specified status (e.g., pending, completed).
- `delete_task`: Deletes a task.

### Interacting with the Agent

Interaction with the agent is done through the `/chat` route. Send a POST request to this route with the following body:

```json
{
  "text": "Request content here"
}
```

#### Example Request with `curl`

To add a new task, you can send:

```bash
curl -X POST "http://localhost:8000/chat" -H "Content-Type: application/json" -d '{"text": "I need to buy bread tomorrow"}'
```

The agent's response will be returned in JSON format.

```json
{
  "status": "success",
  "operation": "add",
  "task_description": "I need to buy bread tomorrow",
  "due_date": "2024-07-15"
}
```

### Interaction Example

You can interact with the agent informally. For example, to add a task, you can send a text like:

```json
{
  "text": "I need to buy bread tomorrow"
}
```

Or to search for pending tasks, you can send:

```json
{
  "text": "What are my pending tasks?"
}
```

And to delete a task, you can send:

```json
{
  "text": "Delete the task to buy bread"
}
```

The agent will process the request and return the appropriate response.
