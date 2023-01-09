# Date Conversion

This is a Python module for converting dates between the Ethiopian and Gregorian calendars.

## Installation

To install the module, clone the repository and run `pip install .` from the root directory.

## Usage

The module provides two functions:

### `eth_to_greg(eth_year, eth_month, eth_day)`

This function converts an Ethiopian date to a Gregorian date. The `eth_year` parameter should be an integer representing the year in the Ethiopian calendar. The `eth_month` parameter should be an integer representing the month in the Ethiopian calendar (1-based index). The `eth_day` parameter should be an integer representing the day in the Ethiopian calendar.

The function returns a tuple containing the equivalent Gregorian year, month, and day.

### `greg_to_eth(greg_year, greg_month, greg_day)`

This function converts a Gregorian date to an Ethiopian date. The `greg_year` parameter should be an integer representing the year in the Gregorian calendar. The `greg_month` parameter should be an integer representing the month in the Gregorian calendar (1-based index). The `greg_day` parameter should be an integer representing the day in the Gregorian calendar.

The function returns a tuple containing the equivalent Ethiopian year, month, and day.

## Examples

```python
>>> from date_conversion import eth_to_greg, greg_to_eth
>>> eth_to_greg(2011, 12, 21)
(2019, 4, 9)
>>> greg_to_eth(2019, 4, 9)
(2011, 12, 21)
