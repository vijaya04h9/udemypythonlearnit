# Setup Instructions

To use this setup:

1. Save the HTML code to a file named `index.html`.
2. Save the Python server code to a file named `server.py`.
3. Install Flask and Flask-CORS if you haven't already:
   ```
   pip install flask flask-cors
   ```
4. Run the Python server:
   ```
   python server.py
   ```
5. Open the `index.html` file in your web browser.

Now you can type Python code in the editor, click "Run Code", and see the output displayed in the "Output" section below.

## Please note:

- This setup runs a local server, which executes Python code sent from the browser. Be cautious about the code you run, as it has the same access as any Python script you'd run on your machine.
- The server uses your default Python interpreter to execute the code.
- For demonstration purposes, this server doesn't have any security measures. In a production environment, you'd want to add authentication and code execution limits.