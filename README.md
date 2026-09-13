# measurement-data-analysis
Python program for statistical analysis of measurement results using the Wright criterion and confidence interval.

## About 

This project implements the processing of a series of repeated measurements. The program calculates the mean measurement value, deviations from the mean, the sum of squared deviations, and an approximate standard deviation. It also performs iterative filtering of measurement results using the Wright criterion and calculates a confidence interval for the final set of measurements.

The project was developed as part of university work during the second year of university.

## Key Variables

* izmerenia - list of measurement results;
* n - number of measurements;
* sort - flag controlling the completion of the filtering process;
* uslovie - flag indicating whether a measurement was removed;
* sum_pogr - sum of the measurement values;
* srednee_pogr - mean measurement value;
* tabl - table used to display calculation results;
* delta - deviations of measurements from the mean, scaled by `10^(-3)`;
* delta_2 - squared deviations, scaled by `10^(-6)`;
* sum_del - sum of squared deviations;
* sigma - approximate standard deviation;
* krit_rayta - deviation threshold according to the Wright criterion;
* filt_izm - measurement values removed during filtering;
* filt_del - deviations of filtered measurements;
* filt_del_2 - squared deviations of filtered measurements;
* eps - calculated confidence interval value.

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/dolzhkris/measurement-data-analysis.git
```

2. Install the required dependency:

```bash
pip install -r requirements.txt
```

3. Run the program with:

```bash
python main.py
```
