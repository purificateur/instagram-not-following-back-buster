# Instagram Not Following Back Buster

## Overview

This Python script identifies users who follow you on Instagram but are not following you back. It processes two input files containing HTML div elements from Instagram's website to extract usernames, then compares them to find the difference.

---

## Requirements

- Python 3
- Two input text files containing Instagram HTML divs in the same directory:
  - `followers.txt`: HTML divs for users who follow you.
  - `followeds.txt`: HTML divs for users you follow.

---

## How to Use

1. **Prepare Input Files**:
  - Copy HTML divs from Instagram's website into `followers.txt` and `followeds.txt`.
  - Example HTML div:
    ```html
    <div ... dir="auto"><span>username</span> ... </div>
    ```

2. **Run the Script**:
    ```bash
    python` instagram_not_following_back_buster.py
    ```

3. **Output**:
  The script will write users who are not following you back to `result.txt`
