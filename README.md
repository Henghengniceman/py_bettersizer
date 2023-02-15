# py_bettersizer
Import, visualize and export the content of Bettersizer .xls output files.

## Dependencies
* pandas
* numpy
* matplotlib
* pathlib
* re

## Quick start
1. Fist download/clone this project to your local computer.
2. Navigate to the base directory and start python.
3. Run `import py_bettersizer` which makes the most basic functions available for you

### The main functions explained:
The user functions always relate to the path of the .xls bettersizer output file.

* py_bettersizer.read_bettersizer_data(path):
    Returns a tuple of (metadata, analysis_data, sd_data)
* py_bettersizer.plot_sd(path):
    Generates a figure comparable to the one in the bettersizer output files.
    
The function `read_bettersizer_data()` is a wrapper for the functions `read_metadata()`, `read_analysis_data()`, `read_sd_data()` and `read_system_status()` which can also be called independently.

## Code Style
The style of this code should follow

* PEP8 (Style Guide for Python Code)
* PEP20 (The Zen of Python)
* NumPy docstring guide, NumPy docstring style example


## License

py_bettersizer, a python project to work with data from the Bettersizer instrument.

Copyright (C) 2021 agm-software-tools

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

A copy of the GNU Affero General Public License  can be found in the LICENSE file
that comes along with this program, or see <https://www.gnu.org/licenses/>.
