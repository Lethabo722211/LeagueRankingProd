# League Ranking Project
League ranking is [python](https://www.python.org/) based CL application that produces a league table with teams and their attained points throgh played matches.

## Functional Requirements
- python3
- Sample well-formed data .txt file (i.e. [**input.txt**](input.txt) is our default file)


## Non - Functional Requirements
[Pytest](pytest.org) for unit testing. Refer to the test file [test_main.py](test_main.py) for the tests.


## Running The Application
Navigate to the artefacts folder and run
```
python3 main.py
```
for the application. You'll be prompted to provide your sample data file in a .txt format.
```
Enter your sample data text file with it's .txt extension: input.txt
```
The expected output should be : 
```
1. Tarantulas, 6 pts
2. Lions, 5 pts
3. FC Awesome, 1 pts
4. Snakes, 1 pts
5. Grouches, 0 pts
```

## Running functional tests
Navigate to the artefacts folder and run
```
pytest
```
or individually run
```
pytest test_main.py::test_get_league_log
pytest test_main.py::test_init
pytest test_main.py::test_get_input_data
```
