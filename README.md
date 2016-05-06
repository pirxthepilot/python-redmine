# Redmine Module

## Description

This python package provides the `Redmine` class for use to query the Redmine API. This class largely depends on the `requests` module.

As of the moment, only supports the following functions:

- get_issue
- create_issue

To install, git clone this repo as `redmine`.


## Prerequisites

   ```
   # yum install gcc python-devel python-pip python-requests libffi-devel
   # pip install -r requirements.txt 
   ```


### Example

```python
from redmine import Redmine
import json

# Start
redmine = Redmine('https://redmine.example.com',
                  '<api key>')

# Get details about an issue
print redmine.get_issue('12345')

# Create an issue
description = "h3. @Test@"
issue = {
         "issue": {
             "project_id": 1,
             "subject": "Test",
             "assigned_to_id": 12,
             "priority_id": 3,
             "description": description
         }
        }
print redmine.create_issue(json.dumps(issue))
```
