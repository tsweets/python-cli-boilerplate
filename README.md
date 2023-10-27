#### Python Dev Setup
- Python3

Add requirements
```
python -m pip install -r requirements.txt
```
#### Tests
```(venv) ➜  python-cli-boilerplate python -m typercli -v ```


#### Virutal Environment
Probably need to recreate the venv when checkout
```
python -m venv ./venv
source venv/bin/activate
```

#### Running
example: 
```python -m typercli add Get some milk -p 1```
```python -m typercli list```
```python -m typercli complete 1```
```python -m typercli remove 1```
```python -m typercli clear```