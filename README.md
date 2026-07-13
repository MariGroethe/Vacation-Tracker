# Vacation-Tracker
An object-oriented Python application designed to help users plan, manage, and budget upcoming trips. Users can organize multi-day itineraries, track travel arrangements, manag group sizes, and dynamically calculate trip costs per person.
## Features
* **Multi-day Itinerary Planning** Manage specific daily activities, lodging details, and dining options chronologically.
* **Dynamic Budgeting** Automatically tallies costs across all activities, transits, and accomodation, providing an overall total and per-person breakdown.
* **Data Persistence** Saves and loads trip configurations to local JSON files so no planning progress is lost between sessions. 
* **Clean OOP architecture** Built using clean Object-Oriented Programming models ('Adventure', 'Day', and 'Activity' classes) seperating data structure from user interface.

## Built With
* **Python 3** (standard library only - no external dependencies required)
  * 'json' for data serialization
  * 'datetime' for date and schedule tracking
  * 'unittest' for automated test-driven development

## How to Run
1. Clone the repository.
2. Open your terminal to the project directory
3. Run the application
```bash
python main.py
```