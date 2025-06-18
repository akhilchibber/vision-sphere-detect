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

## Running locally with object detection

After cloning the repository, install the JavaScript and Python dependencies and
start both the frontend and backend servers:

```bash
# Step 1: Clone the repository
git clone https://github.com/akhilchibber/vision-sphere-detect.git
cd vision-sphere-detect

# Step 2: Set up the Python backend
python -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt
python backend/app.py  # Starts Flask server on http://localhost:8000

# Step 3: Set up the frontend
npm install
npm run dev  # Starts Vite dev server on http://localhost:5173
```

Open <http://localhost:8080> in your browser and upload an image to see detected
objects.

## How can I deploy this project?

Simply open [Lovable](https://lovable.dev/projects/e6b41c86-cf25-4fcc-9847-c66bf614c1a6) and click on Share -> Publish.

## Can I connect a custom domain to my Lovable project?

Yes it is!

To connect a domain, navigate to Project > Settings > Domains and click Connect Domain.

Read more here: [Setting up a custom domain](https://docs.lovable.dev/tips-tricks/custom-domain#step-by-step-guide)
