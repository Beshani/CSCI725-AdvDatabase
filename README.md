# CSCI725-AdvDatabase
Serverless Key-Value Database Using AWS Lambda

## Project Overview

- This repository contains the implementation of an experimental serverless key–value database built using AWS Lambda, S3, and Step Functions. The system supports basic CRUD operations and uses a resolver–dispatcher–worker architecture to enable parallel query execution across data partitions.

- This project was developed and tested using a temporary, limited-time AWS account provided for academic purposes. Due to access constraints, all infrastructure, benchmarking, and evaluations were completed within a fixed time window and under AWS Free Tier limitations. As a result, some large-scale experiments and extended testing were not feasible.

- The goal of this project was to explore the feasibility, performance trade-offs, and architectural challenges of building a database system entirely on serverless cloud functions, and to compare it against managed NoSQL solutions such as DynamoDB.
