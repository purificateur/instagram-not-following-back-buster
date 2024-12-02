# Instagram Not Following Back Buster

## Overview

This Python script identifies users who follow you on Instagram but are not following you back. It processes two input files containing HTML div elements from Instagram's website to extract usernames, then compares them to find the difference.


## Requirements

- Python 3
- Two input text files containing Instagram HTML divs in the same directory:
  - `followers.txt`: HTML div that wraps list of users who follow you.
  - `followeds.txt`: HTML div that wraps list of users you follow.


## How to Use

1. **Prepare Input Files**:
  - Open your Instagram followers and following pages in a web browser.
  - Scroll through the list of followers and followings to make sure all users are fully loaded. Instagram may load users dynamically as you scroll, so ensure the entire list is visible before copying the HTML divs.
  - Copy the HTML divs containing the users from the web page into `followers.txt` and `followeds.txt`.

2. **Run the Script**:
    ```bash
    python instagram_not_following_back_buster.py
    ```

3. **Output**:
  - The script will write users who are not following you back to `result.txt`.
