# Gaia.

## About.
Gaia is a Claude-infused bot that informs users about the state of the earth. Currently, her feature set revolves around information about natural events/disasters of a certain magnitude and their visualization.

The goal is to build a tool that allows Geo and Environmental scientists/ enthusiasts of different sorts to work with public data sets or their own and explore more about this place we call Earth.

## Installation Instructions

Follow these steps to get the app running on your local machine:

### 1. Clone the Repository
To clone the repository, open your terminal and run the following command:

```bash
git clone https://github.com/Onlyartist9/TheDeep.git
```
or use the GitHub Desktop app.

### 2. Change Directory
Change into the directory of the cloned repository:

```bash
cd TheDeep
```

### 3. Configure the API Key
You need to add your Claude API key to your system's PATH environment variable. This allows the application to access the key as needed.

#### For Windows:
Open the Start Search, type in "env", and choose "Edit the system environment variables". In the Environment Variables window, under the "System variables" section, click on "New" and enter the following details:
- Variable name: `ANTHROPIC_API_KEY`
- Variable value: `your_claude_api_key`

Click OK and apply the changes. You may need to restart your command prompt or IDE for the changes to take effect.

#### For macOS/Linux:
Open a terminal and run the following command:
```bash
echo 'export ANTHROPIC_API_KEY="your_claude_api_key"' >> ~/.bash_profile
```
Can be ~/.bashrc depending on your system. 

### 4. Install Required Packages
```bash
pip install -r requirements.txt
```

### 5. Run the Flask App
```bash
flask --app backend.py run --debug
```

### 6. Navigate to the link directed in your terminal(eg. http://127.0.0.1:5000/)



