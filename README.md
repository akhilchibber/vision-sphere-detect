# Welcome to your Lovable project

## Project info

**URL**: https://lovable.dev/projects/e6b41c86-cf25-4fcc-9847-c66bf614c1a6

## How can I edit this code?

There are several ways of editing your application.

**Use Lovable**

Simply visit the [Lovable Project](https://lovable.dev/projects/e6b41c86-cf25-4fcc-9847-c66bf614c1a6) and start prompting.

Changes made via Lovable will be committed automatically to this repo.

**Use your preferred IDE**

If you want to work locally using your own IDE, you can clone this repo and push changes. Pushed changes will also be reflected in Lovable.

The only requirement is having Node.js & npm installed - [install with nvm](https://github.com/nvm-sh/nvm#installing-and-updating)

Follow these steps:

```sh
# Step 1: Clone the repository using the project's Git URL.
git clone <YOUR_GIT_URL>

# Step 2: Navigate to the project directory.
cd <YOUR_PROJECT_NAME>

# Step 3: Install the necessary dependencies.
npm i

# Step 4: Start the development server with auto-reloading and an instant preview.
npm run dev
```

## Running the Full Application

This project now features a Python-based backend for object detection, replacing the previous mock implementation. To run the full application, you'll need to start both the backend server and the frontend development server.

**1. Backend Setup (Python/Flask)**

The backend is a Flask application that serves the object detection API.

*   **Navigate to the backend directory:**
    ```sh
    cd backend
    ```

*   **Create and activate a virtual environment:**
    It's recommended to use a virtual environment to manage Python dependencies.
    ```sh
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    
    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```
    You should see `(venv)` at the beginning of your command prompt.

*   **Install dependencies:**
    Install the required Python packages using the `requirements.txt` file.
    ```sh
    pip install -r requirements.txt
    ```
    This will install Flask, PyTorch, OpenCV, and other necessary libraries. *Note: PyTorch installation can sometimes be complex depending on your system and whether you have a CUDA-enabled GPU. The versions in `requirements.txt` are general; you might need to consult PyTorch's official website for specific installation commands if you encounter issues.*

*   **Run the Flask application:**
    Once dependencies are installed, start the Flask development server.
    ```sh
    python app.py
    ```
    By default, the backend will run on `http://localhost:5000`. You should see output indicating the server is running.

**2. Frontend Setup (React/Vite)**

The frontend is a React application built with Vite.

*   **Navigate to the project root directory (if you were in `backend`):**
    ```sh
    cd .. 
    ```

*   **Install dependencies (if you haven't already):**
    If this is your first time or if dependencies have changed:
    ```sh
    npm install
    ```

*   **Start the frontend development server:**
    ```sh
    npm run dev
    ```
    This will typically open the application in your browser, usually at `http://localhost:5173` (the port might vary). The frontend is configured to send API requests to the backend at `http://localhost:5000`.

With both backend and frontend running, you can now use the object detection feature in the web application, which will call the live Python backend.

**Edit a file directly in GitHub**

- Navigate to the desired file(s).
- Click the "Edit" button (pencil icon) at the top right of the file view.
- Make your changes and commit the changes.

**Use GitHub Codespaces**

- Navigate to the main page of your repository.
- Click on the "Code" button (green button) near the top right.
- Select the "Codespaces" tab.
- Click on "New codespace" to launch a new Codespace environment.
- Edit files directly within the Codespace and commit and push your changes once you're done.

## What technologies are used for this project?

This project is built with:

- Vite
- TypeScript
- React
- shadcn-ui
- Tailwind CSS
- Python (for backend)
- Flask (for backend API)
- PyTorch/YOLOv5 (for object detection)

## How can I deploy this project?

Simply open [Lovable](https://lovable.dev/projects/e6b41c86-cf25-4fcc-9847-c66bf614c1a6) and click on Share -> Publish.

## Can I connect a custom domain to my Lovable project?

Yes it is!

To connect a domain, navigate to Project > Settings > Domains and click Connect Domain.

Read more here: [Setting up a custom domain](https://docs.lovable.dev/tips-tricks/custom-domain#step-by-step-guide)
