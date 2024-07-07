# DMCA-ADGSTUDIOS-LIST

<img src="https://github.com/adgsenpai/DMCA-ADGSTUDIOS-LIST/assets/45560312/d9eb6380-4c09-4cb6-8c09-b363691e7984" width="250px">

## Overview
This repository hosts a list of URLs from the `adgstudios.co.za` domain that have been subject to DMCA takedown requests. The purpose of this repository is to maintain transparency and efficiency in handling DMCA requests and ensuring compliance.

## Fetching the DMCA List
To view the current list of DMCAed URLs, you can use the following `curl` command:
```bash
curl https://raw.githubusercontent.com/adgsenpai/DMCA-ADGSTUDIOS-LIST/main/static/db/list.txt
```

## Submitting a DMCA Takedown Request
If you wish to submit a DMCA takedown request for a page hosted under the `adgstudios.co.za` domain, please follow these steps:

1. **Fork the Repository**: Fork the `DMCA-ADGSTUDIOS-LIST` repository to your own GitHub account.

2. **Create a Pull Request**: Add the URL of the page you are requesting to be taken down to the `list.txt` file. Then, create a pull request to the original repository with your changes.

3. **Include Proof**: In your pull request, provide clear proof of the DMCA violation. This should include documentation proving ownership of the content or other legal justifications for the takedown request.

4. **Wait for Review**: Once submitted, your request will be reviewed. If the request is deemed valid, it will be approved and merged into the main list.

## Automated DMCA Link Updates

We have implemented a robust automation process using GitHub Actions to handle DMCA link updates efficiently. Here's a detailed look at how we manage these updates:

### Workflow Overview

1. **Setup**: The workflow begins by setting up the necessary environment. This includes checking out the repository and installing required packages.
2. **Script Execution**: The `download_unzip_cleanup.sh` script is made executable and then run to handle necessary cleanup operations.
3. **Dependencies Installation**: Python dependencies listed in `requirements.txt` are installed.
4. **Ingress Script Execution**: The `ingress.py` script is executed to perform ingress operations.
5. **Update Script Execution**: The `update.py` script is run to update the `list.txt` file with new DMCA links.
6. **Commit and Push Changes**: Any changes made to the repository are committed and pushed back to the main branch.

### Detailed Workflow Steps

#### `download_unzip_cleanup.sh`

This script handles the downloading, unzipping, and cleanup of necessary files.

#### `ingress.py`

This script performs ingress operations as part of our automation process.

#### `update.py`

The `update.py` script updates the `list.txt` file with new URLs from `filtered_urls.csv`. Here’s a step-by-step breakdown of what the script does:

- **Read Existing list.txt**: Reads the current list of URLs from `list.txt`.
- **Read New URLs from filtered_urls.csv**: Reads new URLs from `filtered_urls.csv`, removes the `https://` prefix, and excludes the domain `anime.adgstudios.co.za/`.
- **Check for Duplicates and Add Unique URLs**: Compares the new URLs against the existing list and adds only the unique ones.
- **Write Updated List Back to list.txt**: Appends the unique new URLs to `list.txt`, ensuring no empty lines at the end.
- **Generate and Send an Email Report**: Sends an email report with the list of newly added URLs.

### GitHub Actions Configuration

The GitHub Actions workflow file (`.github/workflows/ingress-workflow.yml`) runs the entire process at midnight every day and on any push to the main branch.

```yaml
name: Ingress Workflow

on:
  schedule:
    - cron: "0 0 * * *" # Runs at midnight every day
  push:
    branches:
      - main

jobs:
  setup:
    runs-on: self-hosted
    name: Setup
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Install unzip
        run: sudo apt-get install -y unzip

  script:
    runs-on: self-hosted
    name: Script Execution
    needs: setup
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Make script executable
        run: chmod +x download_unzip_cleanup.sh

      - name: Run download_unzip_cleanup.sh
        run: ./download_unzip_cleanup.sh

  install:
    runs-on: self-hosted
    name: Install Dependencies
    needs: script
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Install Python requirements
        run: |
          python3 -m venv venv
          . venv/bin/activate
          pip install -r requirements.txt

  run_ingress:
    runs-on: self-hosted
    name: Run Ingress
    needs: install
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Run ingress.py
        run: |
          . venv/bin/activate
          python ingress.py

  run_update:
    runs-on: self-hosted
    name: Run Update
    needs: run_ingress
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Run update.py
        run: |
          . venv/bin/activate
          python update.py
        env:
          EMAIL_PASSWORD: ${{ secrets.EMAIL_PASSWORD }}

  commit_and_push:
    runs-on: self-hosted
    name: Commit and Push
    needs: run_update
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Commit and push changes
        run: |
          git config --global user.name 'github-actions[bot]'
          git config --global user.email 'github-actions[bot]@users.noreply.github.com'
          git add .
          git commit -m "Update from GitHub Actions"
          git push
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

## Contact
For any queries or further assistance, please reach out via [email link](mailto:adg@adgstudios.co.za).

## License
[MIT License](LICENSE)