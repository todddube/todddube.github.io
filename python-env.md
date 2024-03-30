# python env how-to short version

- org article: https://medium.com/@asheshnathmishra/how-to-create-a-virtual-environment-in-python-on-a-windows-11-system-2023-80cd37c14db3

1. Now coming to the steps, first navigate to a folder where you want to create the venv.
2. create a folder “venv” inside Downloads
3. navigate to "venv" folder and type at cmd: "python -m venv venv_name"
   1. Simply give your venv any name. Once you do this, you will see a folder is created in that path.
4. navigate to Scripts folder inside your venv created and type the command “activate” to go inside your venv.
5. You will observe that the name of your venv now shows in the beginning of the path inside command prompt.
- Now you have successfully created a virtual environment in python.
- You can go ahead and install any library in here using pip command.
6. To exit the virtual environment simply type the following command: deactivate

# pip requirements
- Make: pip freeze > requirements.txt
- Use: pip install -r requirements.txt
