# BBT Chart

[Body Basal Temperature](https://en.wikipedia.org/wiki/Basal_body_temperature) must be taken at the same time every day and graphed for months in advance to prove as useful data for tracking ovulation. Typically, your BBT gets slightly higher after ovulation (detected 24-48 hours in advance by at-home [LH tests](https://www.fda.gov/MedicalDevices/ProductsandMedicalProcedures/InVitroDiagnostics/HomeUseTests/ucm126065.htm)) and drops when you begin menstruating. In this way, tracking your BBT is useful in confirming ovulation. BBT is also useful in detecting pregnancy, as your temperatures will stay high until you menstruate or get a positive pregnancy test. For these reasons, I have found it very helpful to visualize BBT data alongside markers for the first day of my cycle (begin menstruating) and positive LH tests.  

BBT data, as well as cycle day and LH test markers, can be entered through the command line into a database of the user's choosing and then graphed using the Python library for [Plotly](https://plot.ly/python).

## Usage

Clone the repository and in your virtualenv install the requirements in requirements.txt

```
pip install -r requirements.txt
```

BBT Chart was created to enter information into a local PostgreSQL database by default. Create a database and enter your settings into a ```settings.py``` file.

```python
db_info = {'database': 'your_database', 'user': 'your_username', 'password': 'your_password'}
```

Obtain a Plotly username and API Key and enter those into a file called ```credentials.py```. Use the Plotly function for creating its credentials file.

```python
import plotly

def set_credentials():
    plotly.tools.set_credentials_file(username='your_username', api_key='your_api_key')
```

Run create_table.py in the command line.

```
python create_table.py
```

Add your data from command line with ```add_data.py```. The four arguments consist of the date (ex: 2016-12-14), temperature to two decimal places (ex: 97.21), a marker for the first day of your cycle (ex: cd1), and a marker for a positive LH test (ex: +). When not entering data for cycle days or LH tests, substitute with "-" (or character of your choice) to show a null value. Previous data can be added in this way as well; all dates get sorted before being graphed.

```
python add_data.py YYYY-MM-DD ##.## - -

python add_data.py 2016-12-14 97.21 cd1 +
```

Graph your chart from command line with ```run.py```.

```
python run.py
```

Example chart:

![chart](http://i.imgur.com/indEAsN.jpg)  


## More options  

To view all of the previously entered data, use ```print_data.py```.

```
python print_data.py
```

Example output in terminal:  

![output](http://i.imgur.com/T3LGbtw.png)  


To delete an entry, use ```delete_entry.py``` and add the date to delete.

```
python delete_entry.py 2016-12-14
```

To edit the date, temperature, cycle day, and LH data, use the following files like so:

```
python edit_date.py 2016-12-14 2016-12-13

python edit_temp.py 2016-12-13 96.72

python edit_cd.py 2016-12-13 cd1

python edit_lh.py 2016-11-27 +
```

## Features to add
- Overlaid graph of average temperature
- Set up cron job to grab latest tweet to bbt_chart account from user every day at specific time and add to database
- Tweet from bbt_chart to confirm data added
- Weekly post Plotly chart to Twitter and mention app user
- Add argparse for options input from command line
- Create as Python Package

## License
MIT License
