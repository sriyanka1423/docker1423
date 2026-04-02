# docker1423

# Docker Text File Processing Project

This project builds a lightweight Docker container that automatically reads text files, processes them, writes the results to an output file, and prints the output to the console before exiting.

## Objective

The goal of this project is to create an end-to-end Docker container that:

- Reads two text files from `/home/data`
- Counts words in each file
- Calculates the total word count across both files
- Finds the top 3 most frequent words in `IF-1.txt`
- Handles contractions in `AlwaysRememberUsThisWay-1.txt` by splitting them into individual words, then finds the top 3 most frequent words
- Determines the IP address of the machine running the container
- Writes all results to `/home/data/output/result.txt`
- Prints the content of `result.txt` to the console and exits automatically

## Project Requirements

- Docker Desktop installed on personal machine
- Lightweight Docker image
- Python script for automated processing
- Output written to `/home/data/output/result.txt`
- Final Docker image optimized to stay under 200MB
- Final image exported as a `.tar` file for submission

## Project Structure

```bash
project-folder/
│
├── Dockerfile
├── script.py
├── IF-1.txt
├── AlwaysRememberUsThisWay-1.txt
├── README.md
└── output/
    └── result.txt
