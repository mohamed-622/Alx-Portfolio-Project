# PitchBooking
<p align="center">
<img src="https://i.imgur.com/fQzuyNG.png"></img>
</p>

[PitchBooking](https://pitchbooking.globalmohamed.tech) is a web application that allows users to book time slots for a local stadium. It simplifies the process of reserving slots for sports or events.

## Table of Contents
- [The Story](#how-it-started)
- [The Story In Slides](#project-presentation)
- [Features](#features)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## How It Started
#### Inspiration

The idea for PitchBooking emerged from the daily struggles of needing to physically be present or inquire through messaging apps for available time slots at local stadiums. The frustration sparked the vision for a user-friendly platform that streamlines the booking process, making it more accessible and efficient for sports enthusiasts.
This web application aims to simplify the process of booking local stadiums, providing a convenient platform for users to check availability, make reservations, and manage their bookings effortlessly.

#### Technical Challenges

While not the most technically complex application, PitchBooking presented unique challenges. Implementing features like a date picker (flatpickr) and handling available time slots required thoughtful consideration. The README dives into the details of the chosen algorithms, technologies (Flask, SQLAlchemy, SQLite), and the decision-making process behind the architecture.

#### Next Iteration

###### Catering to the Urban Community
Looking ahead, there's so much more to add to PitchBooking. I envision features that cater to the urban community of our city, making the platform an indispensable tool for anyone looking to book sports facilities.


## Project Presentation

For a more in-depth walkthrough of PitchBooking project, check out our presentation slides.

- [PitchBooking Presentation](https://docs.google.com/presentation/d/1Ha-_6ky-etrXSaXxd1cyQOcZsSF6AURCxhPzyFQvQwM/edit?usp=sharing)

## Features

- User authentication for secure bookings
- Booking system with date and time slots
- Availability checker to see open slots
- Responsive design for various devices

## Getting Started

### Prerequisites

- Python (version 3.x)
- Flask web framework
- SQLite

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mohamed-622/Alx-Portfolio.git
   ```

2. Change into the project directory:

   ```bash
   cd PitchBooking
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```


### Using a Virtual Environment

To ensure a clean and isolated environment for your project, it's recommended to use a virtual environment. Follow these steps to set up and activate a virtual environment:

1. Open a terminal and navigate to your project's root directory.

2. Create a virtual environment using the following command:

    ```bash
    python3 -m venv venv
    ```

    If you are using Python 3, you might need to use `python3` instead.

3. Activate the virtual environment:

    - On Windows:

    ```bash
    .\venv\Scripts\activate
    ```

    - On macOS and Linux:

    ```bash
    source venv/bin/activate
    ```

4. Once the virtual environment is activated, you should see `(venv)` in your terminal prompt.

5. Install the required dependencies from the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

Now, your project is set up within a virtual environment, and you can run it with the isolated dependencies.



## Usage

1. Run the application:

   ```bash
   python3 main.py
   ```

2. Open your web browser and go to [http://localhost:5000](http://localhost:5000).

3. Explore the application, sign up, log in, and start booking your slots!

## Contributing

Your contributions to PitchBooking are highly valued! Whether it's fixing a bug, adding a new feature, or improving documentation, every bit helps make the project better.
If you'd like to contribute, please fork the repository and create a new branch. Pull requests are welcome.
#####Contributions Welcome:
- Bug Fixes: Help identify and fix bugs.
- New Features: Have an idea for a feature? Feel free to add it or suggest it.
- Documentation: Improvements or clarifications? Great!

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

- Author: Mohamed Ezghoudi
- GitHub: [My GitHub](https://github.com/mohamed-622)
- Email: mohamedezghoudi@gmail.com
