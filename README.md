![image](https://github.com/ZenithSuite/UDorkMaker/assets/139548576/8d4e7438-0eda-4e1a-989a-3a89d87f2be0)

Creating a comprehensive GitHub README.md file for your Python code and its executable version is an excellent way to provide documentation and usage instructions for your project. Below, I'll outline the structure and content you can include in your README.md file:

## Dork Generator

**Description:**

Dork Generator is a Python tool for crafting specialized search queries (dorks) used with search engines or security testing tools, primarily in the field of cybersecurity and ethical hacking. It enables users to generate custom search queries with various operators and symbols to discover specific information or vulnerabilities on the internet.

**Features:**

- Operator Selection
- Input Source (Text File)
- Quotes Option
- Symbol Selection
- Combination Generation
- Output to File
- Interactive Interface

## Table of Contents

1. [Getting Started](#getting-started)
   - [Windows Installation](#windows-installation)
   - [Linux Installation](#linux-installation)
2. [Usage Guide](#usage-guide)
   - [Operator Selection](#operator-selection)
   - [Input Source](#input-source)
   - [Quotes Option](#quotes-option)
   - [Symbol Selection](#symbol-selection)
   - [Combination Generation](#combination-generation)
   - [Output to File](#output-to-file)

## Getting Started

### Windows Installation
- Go to Releases section
- Download Exe
- Run it as you wish

### Linux Installation
- Required Python3
- Required Python libraries: termcolor

Clone the repository:
```shell
git clone https://github.com/ZenithSuite/UDorkMaker.git
cd UDorkMaker
pip install termcolor
```
Run code:
```shell
Python3 Dork.py
```





## Usage Guide

### Operator Selection

To choose an operator, run the tool and follow the prompts. You can select from a range of operators, including Boolean operators and advanced Google search operators.

### Input Source

it suggests to Specify a text file containing keywords or search terms that will be used in your dork combinations. The tool reads from this file for input.

### Quotes Option

Choose whether to include quotes around your input for precise search queries.

### Symbol Selection

Select symbols to modify your search queries. Symbols help refine search results.

### Combination Generation

The tool generates combinations of search queries by replacing placeholders in the template with input from the specified text file.

### Output to File

Generated dorks are saved to a file named "Dorks Made" within the "DORK MAKER" directory in "UT-ANF" Dir.
