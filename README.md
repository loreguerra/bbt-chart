# BBT Chart

[Body Basal Temperature](https://en.wikipedia.org/wiki/Basal_body_temperature) must be taken at the same time every day and graphed for months in advance to prove as useful data for tracking ovulation. **BBT Chart** data can be entered through the command line into a database of the user's choosing and then graphed using the Python library for [Plotly](https://plot.ly/python).

## Usage

Clone the repository and in your virtualenv install the requirements in requirements.txt

```
pip install -r requirements.txt
```

BBT Chart was created to enter information into a local PostgreSQL database by default. Create a database and enter your settings into a settings.py file.

```python
db_info = {'database': 'your_database', 'user': 'your_username', 'password': 'your_password'}
```

Obtain a Plotly username and API Key and enter those into a file called credentials.py. Use the Plotly function for creating its credentials file.

```python
import plotly

def set_credentials():
    plotly.tools.set_credentials_file(username='your_username', api_key='your_api_key')
```

Run create_table.py in the command line.

```
python create_table.py
```

Add your data from command line with add_data.py. The two arguments consist of the date (ex: 2016-12-14) and temperature to two decimal places (ex: 97.21). Previous data can be added in this way as well; all dates get sorted before being graphed.

```
python add_data.py YYYY-MM-DD ##.##
```

Graph your chart from command line with run.py.

```
python run.py
```

## Features to add
- Marker for day one of cycles
- Marker for positive LH test
- Add LH/cycle column code to create_table and add_data
- Create edit files for LH/cycle
- Overlaid graph of average temperature
- Pretty print entries
- Add "help" function to list functions and args
- Add argparse for options input from command line
- Check if table has already been created
- Allow creating/graphing of multiple tables with options
- Integrate with Twitter to pull latest tweet to BBT Chart twitter account from app user and add to database
- Integrate with Twitter Streaming API to automatically add latest tweet from app user to database
- Post Plotly chart to Twitter and mention app user
- Create as Python Package


## License
MIT License
