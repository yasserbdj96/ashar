#   |                                                          |
# --+----------------------------------------------------------+--
#   |   Code by : yasserbdj96                                  |
#   |   Email   : yasser.bdj96@gmail.com                       |
#   |   Github  : https://github.com/yasserbdj96               |
#   |   BTC     : bc1q2dks8w8uurca5xmfwv4jwl7upehyjjakr3xga9   |
# --+----------------------------------------------------------+--  
#   |        all posts #yasserbdj96 ,all views my own.         |
# --+----------------------------------------------------------+--
#   |                                                          |

#make run con="<encode/decode>" pass="<PASSWORD>" text="<TEXT>"

#START{
VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

RUN = run.py $(con) $(pass) $(text)

run: $(VENV)/bin/activate
	$(PYTHON) $(RUN)

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r ./requirements.txt
	$(PIP) install -r ./requirements-pypi.txt

clean:
	rm -rf ashar/__pycache__
	rm -rf $(VENV)
#}END.