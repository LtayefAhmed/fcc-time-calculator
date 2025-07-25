# Time Calculator - freeCodeCamp Certification Project

This repository contains my solution for the "Time Calculator" project, a requirement for the freeCodeCamp "Scientific Computing with Python" certification.

## Project Overview

The core of this project is a single Python function, `add_time`, designed to add a given duration to a start time in a 12-hour clock format. The function is built to handle a wide array of scenarios, including changes in period (AM/PM), transitions across multiple days, and the optional calculation of the resulting day of the week.

This project is a fundamental exercise in robust logic, precise string manipulation, and meticulous handling of edge cases.

---

## Key Features & Skills Demonstrated

### 1. Core Time Logic
*   **24-Hour Conversion:** The initial 12-hour time is converted to a 24-hour format to simplify all arithmetic operations.
*   **Minute and Hour Calculation:** Correctly handles minute overflows that carry over into hours.
*   **Multi-Day Calculation:** Accurately calculates the number of days that have passed, displaying "(next day)" or "(n days later)" as required.

### 2. Edge Case Management
This project's main challenge lies in correctly managing numerous edge cases, including:
*   Transitions from PM to AM (crossing midnight).
*   Calculations landing exactly on 12:00 AM or 12:00 PM.
*   Durations that span multiple full days (e.g., more than 24, 48, or 72 hours).

### 3. String Formatting & Manipulation
*   The final output is meticulously formatted to match the required specifications.
*   This includes ensuring minutes are zero-padded (e.g., `05` instead of `5`) and that all spacing is precise.

### 4. Optional Parameter Handling
*   The function correctly processes an optional `start_day` parameter.
*   It performs case-insensitive matching for the input day and calculates the resulting day of the week, correctly handling the 7-day cycle using modular arithmetic.

---


