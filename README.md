# OpenStreetMap Data Wrangling

This project is a part of the [Data Analyst Nanodegree](https://www.udacity.com/course/data-analyst-nanodegree--nd002) at [Udacity](https://www.udacity.com/)

-- Project Status: Completed

## Project Introduction

Applying the Data Wrangling techniques to clean an area of the [OpenStreetMap](https://www.openstreetmap.org/). I have chosen my own city Cairo, Egypt data to work with.

## Methods Used

- Data Wrangling
- Exploratory Data Analysis
- Data Parsing

## Technologies

- Python 2.7
- XML
- MongoDB

## Project Description

TThe goal of this project is to apply Data Wrangling techniques to clean an area of the OpenStreetMap. I started by choosing the area of interest(Cairo) and download its [map file](https://github.com/eng-dtarek/OpenStreetMap_Data_Wrangling/blob/master/sample.osm). Then I got an overview of the users' contributions and the existing tags. After that, I revealed the problems encountered in the map by auditing postal codes and street names of nodes and ways. Some of the problems were non-standardized formats and inconsistency. Finally, I solved some of the encountered problems by cleaning the data.

I used MongoDB to get some useful information from this map file like the top 10 amenities, top 3 ways, and top 5 cuisines. (for more details of the wrangling process see this [document](https://github.com/eng-dtarek/OpenStreetMap_Data_Wrangling/blob/master/data%20wrangling%20process.pdf)).

## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/en/articles/cloning-a-repository)).
2. Install the above technologies.
3. Each file in the code folder handles part of the wrangling process. for example "audit_postal_codes" audits postal codes to reaveal its problems. >> cd code >> python audit_postal_codes.py

## References

See this file [references](https://github.com/eng-dtarek/OpenStreetMap_Data_Wrangling/blob/master/references.txt)
