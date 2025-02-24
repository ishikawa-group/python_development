# Github Actions
* CI/CD tool provided by Github
* Can automate testing, formatting, and other processes

## Usage
* Place YAML files containing workflow processes in `./github/workflow/`
* Processes run automatically when specified events (push, pull request, etc.) occur
* Check process results and details on Github (browser)
* YAML templates available at https://github.com/marketplace?type=actions

## Hello world
```yaml
name: Hello world
on: push

jobs:
  build:
    name: Greeting
    runs-on: ubuntu-latest
    steps:
      - run: echo "Hello world"
```
* on: specifies the trigger
  + In this case, we wrote push to trigger on push events
* runs-on: specifies the execution environment
  + We wrote ubuntu-latest to run on the latest Ubuntu environment
* steps: lists the actions to execute
  + We wrote echo to display "Hello World!" on screen

## Format Check
```yaml
name: formatting check with flake8

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  command:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with:
          python-version: 3.11

      - name: Install dependencies
        run: pip install flake8
      - name: Run checking
        run: flake8 .
```
## Configuration Meanings
* jobs
  + Top-level unit of processing. One or more jobs are set with job IDs and run in parallel
* on
  + Specifies which events trigger the process execution
* runs-on
  + Specifies the OS (runner) for job execution
* uses
  + Can execute Actions created by third parties or GitHub. actions/checkout@v4 by GitHub is commonly used
* steps
  + Jobs consist of one or more steps, and steps contain one or more run commands
* run
  + Lists commands to execute. Can include a name describing the process, viewable on GitHub