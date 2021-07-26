# SLP Tracker
A simple script in Python used to print in the terminal the claimable slp in a list of accounts using the API api.lunaciarover.com.

## Installation 

Use pip to install requests and colorama

```bash
pip install requests
pip install colorama
```

## Usage

Edit the config.py changing the TOTAL_DESIRED for the total slp required to your schoolars and add to ACCOUNTS a tuple with the string identifing a account and ronin account (0x...)  

Example:

```python

ACCOUNTS = [
    ("ME" ,"0x0000000000000000000000000000000000000000"),      
    ("MOM","0x0000000000000000000000000000000000000001"),
    #...
]

TOTAL_DESIRED = 1650
```
And finaly:
```bash
  python main.py
```




