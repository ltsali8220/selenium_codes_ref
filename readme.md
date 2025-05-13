# Selenium Codes Repository

This repository contains various Selenium automation scripts for web testing and interaction. It includes sample codes to demonstrate different functionalities, such as interacting with input fields, handling buttons, and managing browser windows and tabs using Selenium WebDriver.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Secret Sauce Test](#secret-sauce-test)
  - [Multiple Tab Handling](#multiple-tab-handling)
- [Contributing](#contributing)
- [License](#license)

## Overview

This repository provides Selenium automation scripts for interacting with the **Techstep Academy Training Ground** website. 

1. **Secret Sauce Test**: A script that fills an input field with a specific text and checks if the text is correctly entered.
2. **Multiple Tab Handling**: A script that opens multiple tabs in the browser, all navigating to the same URL.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.x** installed on your local machine.
- **Selenium** library installed. You can install it using pip:
  ```bash
  pip install selenium
ChromeDriver installed and available in your system's PATH (or specify its path in the script).

Installation
Clone this repository to your local machine:

bash
Copy
Edit
git clone https://github.com/ltsali8220/selenium_codes_ref.git
Install the required Python packages:

bash
Copy
Edit
pip install -r requirements.txt
Ensure ChromeDriver is installed and available for Selenium to interact with the Chrome browser. You can download it from here.

Usage
Secret Sauce Test
The secret_sauce.py script interacts with a text input field on the Techstep Academy training ground page. It verifies if the text entered into the field is correctly retrieved.

Steps:
Clone this repository.

Navigate to the script file location and run:

bash
Copy
Edit
python secret_sauce.py
The script will enter the text "it worked" into the input field, verify it, and print a success message if the test passes.

Multiple Tab Handling
The multiple_tabs.py script opens multiple tabs in Chrome, all navigating to the Techstep Academy training ground page.

Steps:
Clone this repository.

Navigate to the script file location and run:

bash
Copy
Edit
python multiple_tabs.py
The script will open 5 tabs (the main tab and 4 additional ones), each visiting the training ground page.

Contributing
Contributions are welcome! If you would like to contribute to this repository, please fork it and create a pull request with your proposed changes.

Fork the repository.

Create a new branch.

Make your changes.

Submit a pull request.

License
This repository is open-source and available under the MIT License.

markdown
Copy
Edit

### Key Points:
- **Project Overview**: Explains what the repository is for and what scripts it contains.
- **Prerequisites**: Lists the necessary software dependencies (Python, Selenium, and ChromeDriver).
- **Installation**: Provides steps to clone the repository and install dependencies.
- **Usage**: Provides detailed instructions on how to run the different scripts in your repository.
- **Contributing**: Encourages others to contribute to the project.
- **License**: Specifies that the project is open-source under the MIT License.

This `README.md` now contains all the information in a clean, professional format, and it includes the code blocks as requested! Let me know if you need further modifications.


