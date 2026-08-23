# Student Budget Tracker

A simple Python-based budget tracking application designed to help students manage their monthly budget and track their expenses by category.

## Features

* Set and manage a monthly budget
* Add expenses with a name, category, and amount
* Organize expenses by categories
* View all recorded expenses
* Calculate total spending
* Calculate the remaining budget
* Save user data locally using JSON
* Load previously saved data when the program starts

## Technologies Used

* Python
* JSON
* File Handling

## Data Storage

The application stores user data locally in a `users.json` file.

The data is organized by user and expense category:

```json
{
    "Menna": {
        "budget": 1000,
        "expenses": {
            "skin care": {
                "cleanser": 150,
                "sun screen": 200
            },
            "food": {
                "coffee": 50
            }
        }
    }
}
```

## How to Run

1. Make sure Python is installed on your computer.
2. Clone the repository:

```bash
git clone https://github.com/your-username/student-budget-tracker.git
```

3. Navigate to the project folder:

```bash
cd student-budget-tracker
```

4. Run the program:

```bash
python budget_tracker.py
```

## Project Structure

```text
Student-Budget-Tracker/
│
├── budget_tracker.py
├── users.json
├── .gitignore
└── README.md
```

> **Note:** `users.json` contains local user data and should not be uploaded to a public repository.

## Future Improvements

* Edit and delete expenses
* Add expense dates
* Track spending by month
* Display spending summaries by category
* Add input validation and error handling
* Build a graphical user interface (GUI)

## Author

**Menna Yasser**
