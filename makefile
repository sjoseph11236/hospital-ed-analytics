install:
	pip3 install -r requirements.txt
# @ suppresses printing the command itself — only shows the output
# PYTHONPATH=. tells Python to look for modules in the current directory
dev:
	@PYTHONPATH=. python3 app.py