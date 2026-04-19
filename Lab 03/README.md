# Lab 03 — Building ERDs

Entity Relationship Diagram (ERD) lab for **CS355/CE373 Database Systems** at **Habib University**. This lab focuses on designing a correct data model for a business scenario by identifying entities, attributes, keys, relationships, and cardinalities.

## Overview

In this lab, the task is to build an ERD in **DB Designer** for the given scenario and export the final design as a PDF. The main graded scenario in the manual is **Scenario 1: Cricket Tournament**. The lab is about data modeling, not coding. The final ERD should clearly show:

- entities
- attributes with data types
- null / not null constraints
- primary keys and foreign keys
- relationships
- cardinalities such as **1–1** and **1–M** fileciteturn2file0L70-L78

## Objective

The objective of this lab is to help students build data design skills and develop a data model for a business system, with special focus on identifying the correct **entities, relationships, and cardinalities**. fileciteturn2file0L13-L21

## Tools Used

- **DB Designer** for creating the ERD
- **MS SQL Server** selected as the schema type inside DB Designer fileciteturn2file0L35-L47

## Lab Scenario

The graded scenario is a **Cricket Tournament** system. According to the lab manual, the system needs to keep track of:

- 8 participating countries
- 12 players nominated by each country
- stadiums, their cities, and capacities
- umpires from different countries
- match schedule including date, time, teams, umpires, city, stadium, winning team, and man of the match
- per-match player performance including total runs scored and wickets taken fileciteturn2file0L79-L89

## ERD Included in This Repository

This repository includes the final ERD exported as a PDF/image for the cricket tournament scenario. The ERD shown in the uploaded design includes the following main entities:

- **Teams**
- **Players**
- **Matches**
- **Match_Stats**
- **Umpires**
- **Stadiums**
- **City** fileciteturn2file1L1-L1

From the final ERD image, the schema models:

- teams and their country information
- players belonging to teams
- matches between two countries
- match-level statistics for each player
- stadiums connected to cities
- umpires assigned to matches
- winning team and man of the match stored in the match record fileciteturn2file1L1-L1

## Main Entities and Attributes

Based on the submitted ERD image, the design contains these tables and attributes:

### Teams
- `Country_Code` (PK)
- `Country_Name`

### Players
- `Player_ID` (PK)
- `Player_Name`
- `Country_Code` (FK)

### Matches
- `Match_ID` (PK)
- `Date`
- `Time`
- `Country1` (FK)
- `Country2` (FK)
- `City_Code` (FK)
- `Stadium_ID` (FK)
- `WinningTeam_ID` (FK)
- `ManOfTheMatch_ID` (FK)
- `Umpire1_ID` (FK)
- `Umpire2_ID` (FK)

### Match_Stats
- `Match_ID` (FK / composite key part)
- `Player_ID` (FK / composite key part)
- `Runs_Scored`
- `Wickets_Taken`

### Umpires
- `Umpire_ID` (PK)
- `Umpire_Name`
- `Country_Code`

### Stadiums
- `Stadium_ID` (PK)
- `Stadium_Name`
- `City_Code` (FK)
- `Capacity`

### City
- `City_Code` (PK)
- `City_Name` fileciteturn2file1L1-L1

## Relationships Modeled

The final ERD models several important relationships, including:

- one team can have many players
- one city can have many stadiums
- one match is played in one stadium
- one match has two participating teams
- one match has two selected umpires
- one player can appear in many match statistics records
- one match can have many player statistics records
- one player can become man of the match in a match
- one team can be recorded as the winner of a match fileciteturn2file1L1-L1

## Rubric Focus

The lab manual evaluates the ERD using the following criteria:

- entities correctly identified
- all attributes mentioned
- relationships drawn and resolved correctly
- correct cardinalities
- PK and FK identified correctly and placed in the appropriate tables fileciteturn2file0L79-L83

## How to Recreate the ERD

1. Open **DB Designer**.
2. Create a new project.
3. Choose **MS SQL Server** as the schema type.
4. Add the required tables.
5. Add attributes with appropriate data types.
6. mark primary keys and foreign keys
7. define the relationships between the tables
8. verify the cardinalities
9. export the final ERD as a PDF for submission fileciteturn2file0L22-L69

## Submission Notes

According to the manual:

- the lab contributes **1%** toward the final grade
- submission is through **CANVAS**
- the required submission is a **PDF** containing the final ERD
- the required filename format is `Lab 03 aa1234.pdf`
- late submission is allowed only until **11:59 PM on the same day** with a **20% penalty** fileciteturn2file0L3-L12

## Repository Structure

```bash
.
├── Lab03_Manual.pdf      # Official lab manual
├── Lab03.pdf             # Final exported ERD
└── README.md             # Project overview
```

## Notes

The lab manual explicitly states that the use of AI-based tools for doing the lab is prohibited and may be considered plagiarism. This README is only a repository description of the uploaded work and lab context, not a replacement for the original student submission. fileciteturn2file0L13-L18
