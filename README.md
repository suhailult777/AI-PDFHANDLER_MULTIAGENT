# Langflow AI Project

This project is a Langflow-based AI solution that integrates Datastax, AWS, multi-agent architecture, a vector database, and Streamlit for building intelligent workflows and interfaces. The project demonstrates a chatbot that can respond to queries using Langflow's APIs and runs within a Streamlit interface for enhanced interactivity.

## Features

- **Multi-Agent System**: Utilizes multiple agents to handle distinct tasks.
- **Vector Database**: Employs Datastax AstraDB for efficient vector storage and retrieval.
- **AWS Integration**: Leverages AWS for scalability and reliability.
- **Streamlit Interface**: Provides a user-friendly web interface for interacting with the AI chatbot.
- **API Communication**: Communicates with Langflow APIs to process and execute workflows.

---

## Installation

### Prerequisites
- Python 3.12 or higher
- pip (Python package manager)

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/langflow-ai-project.git
   cd langflow-ai-project
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv .venv
   source .venv/bin/activate # On Windows: .venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the environment variables:
   - Create a `.env` file in the root directory.
   - Add your Datastax, Langflow, and AWS credentials, along with the application token, as shown below:
     ```env
     APP_TOKEN=<your_application_token>
     ```

5. Run the Streamlit interface:
   ```bash
   streamlit run main.py
   ```

---

## Usage

1. Open the Streamlit app in your browser at `http://localhost:8501`.
2. Input your query in the chat interface.
3. The chatbot will process your input and return responses based on the Langflow workflow.

---

## Code Overview

### Key Files

- `main.py`: The main script that integrates Langflow API, Datastax vector database, AWS, and Streamlit interface.
- `requirements.txt`: Lists all the dependencies needed for the project.
- `.env`: Stores environment variables for secure access to credentials.

### Main Components

1. **Langflow API Integration**:
   The `run_flow` function in `main.py` sends queries to Langflow and retrieves responses.
   ```python
   def run_flow(message: str) -> dict:
       api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"

       payload = {
           "input_value": message,
           "output_type": "chat",
           "input_type": "chat",
       }
       headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
       response = requests.post(api_url, json=payload, headers=headers)
       return response.json()
   ```

2. **Streamlit Interface**:
   The Streamlit app allows users to input messages and view responses in a web interface.

3. **Environment Variables**:
   Environment variables ensure sensitive information, like API keys, are securely managed.

---

## Dependencies

- `requests`: For making HTTP requests to Langflow's API.
- `python-dotenv`: For loading environment variables.
- `streamlit`: For creating a user-friendly web interface.
- `datastax-astra`: For vector database operations.
- `boto3`: For AWS integrations.

Install these via the `requirements.txt` file.

---

## Contributing

Feel free to submit issues or pull requests to improve this project. Contributions are always welcome!

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgements

- [Langflow](https://langflow.astra.datastax.com)
- [Streamlit](https://streamlit.io)
- [Datastax AstraDB](https://www.datastax.com/astra)
- [AWS](https://aws.amazon.com)

