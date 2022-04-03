# Election_Analysis (Python project)

## Overview of Project

In this project, we were working on a election result data-set using Python to automate tasks and conduct data analysis.
Python handles large data files and performs complex calculations quickly and helps to access, process, manipulate and store data.

### Purpose

The main purpose of this project was to conduct a election audit on the tabulated results for a US congressional
precinct using python to get a summary of the election results. Various parameters were calculated to analyse the election
results:
- Total votes,
- Votes cast for each candidate
- Percentage of votes cast for each canditate
- Winning canditate and winning vote-count

## Election-Audit Results

### Total votes cast in congressional election

We used the following logic to compute the total votes:

```
Initialize a total vote counter to 0

Loop through rows of data
    Increment total vote counter by 1
Loop End
```
Using above logic, we determined that the total number of votes cast in the election were **369,711** as shown in the image below:

![Total_votes](Images_analysis/Total_votes.png)

### Breakdown of the number of votes and the percentage of total votes for each county in the precinct

We used the following logic to compute the number of votes and percentage of votes for each county in precinct: 

```
Initialize a dictionary with `county name` as the key and `number of votes` as the value

Loop through rows of data
    Extract the `county name` from each row
    Increment the `number of votes` saved in the dictionary with `county name` keyby 1 if the current
    row holds data for `county name`
Loop End
``` 
Using above logic, we determined number of votes and percentage for each county in the election as shown in the image below:

![County_votes](Images_analysis/County_votes.png)

### county with largest number of votes

To get the county with highest number of votes, we have used the following logic:

```
Initialize `highest votes` to 0
Initializ `winning county` to empty string
Loop through rows of data
    Extract `vote count` from each row
    if `vote count` >= `highest votes`
        `highest votes` = `vote count`
        store the county name corresponding to `vote count` in `winning county`
Loop End
```
Using above logic, we determined that the county with the highest number of votes was **Denver** as shown in
the below image: 

![Largest_county_votes](Images_analysis/Largest_county_votes.png)

### Breakdown of the number of votes and the percentage of the total votes for each candidate

```
Initialize a dictionary with `candidate name` as the key and `number of votes` as the value

Loop through rows of data
    Extract the `candidate name` from each row
    Increment the `number of votes` saved in the dictionary with `candidate name` key by 1 if the current row holds data for
    `candidate name`
Loop End
``` 
Using above logic, we determined the number of votes and percentage for each candidate in the election as shown in the image below:

![Candidate_votes](Images_analysis/Candidate_votes.png)

### Candidate won the election, their vote count and their percentage of the total votes

