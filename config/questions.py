'''
Author:     Sai Vignesh Golla
LinkedIn:   https://www.linkedin.com/in/saivigneshgolla/

Copyright (C) 2024 Sai Vignesh Golla

License:    GNU Affero General Public License
            https://www.gnu.org/licenses/agpl-3.0.en.html
            
GitHub:     https://github.com/GodsScion/Auto_job_applier_linkedIn

version:    24.12.29.12.30
'''


###################################################### APPLICATION INPUTS ######################################################


# >>>>>>>>>>> Easy Apply Questions & Inputs <<<<<<<<<<<

# Give a relative path of your default resume to be uploaded. If file is not found, will continue using your previously uploaded resume in LinkedIn.
default_resume_path = "all resumes/default/resume.pdf"      # (In Development)

# What do you want to answer for questions that ask about years of experience you have, this is different from current_experience? 
years_of_experience = "2"          # A number in quotes Eg: "0","1","2","3","4", etc.

# Do you need visa sponsorship now or in future?
require_visa = "No"               # "Yes" or "No"

# What is the link to your portfolio website, leave it empty as "", if you want to leave this question unanswered
website = "https://github.com/gzhang33"                        # "www.example.bio" or "" and so on....

# Please provide the link to your LinkedIn profile.
linkedIn = "https://www.linkedin.com/in/gianni-zhang-313398307/"       # "https://www.linkedin.com/in/example" or "" and so on...

# What is the status of your citizenship? # If left empty as "", tool will not answer the question. However, note that some companies make it compulsory to be answered
# Valid options are: "U.S. Citizen/Permanent Resident", "Non-citizen allowed to work for any employer", "Non-citizen allowed to work for current employer", "Non-citizen seeking work authorization", "Canadian Citizen/Permanent Resident" or "Other"
us_citizenship = "Non-citizen allowed to work for any employer"

## SOME ANNOYING QUESTIONS BY COMPANIES 🫠 ##

# What to enter in your desired salary question (American and European), What is your expected CTC (South Asian and others)?, only enter in numbers as some companies only allow numbers,
desired_salary = 27000          # 80000, 90000, 100000 or 120000 and so on... Do NOT use quotes
'''
Note: If question has the word "lakhs" in it (Example: What is your expected CTC in lakhs), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
And if asked in months, then it will divide by 12 and answer. Examples:
* 2400000 will be answered as "200000"
* 850000 will be answered as "70833"
'''

# What is your current CTC? Some companies make it compulsory to be answered in numbers...
current_ctc = 0            # 800000, 900000, 1000000 or 1200000 and so on... Do NOT use quotes
'''
Note: If question has the word "lakhs" in it (Example: What is your current CTC in lakhs), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
# And if asked in months, then it will divide by 12 and answer. Examples:
# * 2400000 will be answered as "200000"
# * 850000 will be answered as "70833"
'''

# Currency of salaries you mentioned. Companies that allow string inputs will add this tag to the end of numbers. Eg: 
currency = "GBP"                 # "USD", "INR", "EUR", "GBP", etc.

# What is your notice period in days?
notice_period = 0                   # Any number >= 0 without quotes. Eg: 0, 7, 15, 30, 45, etc.
'''
Note: If question has 'month' or 'week' in it (Example: What is your notice period in months), 
then it will divide by 30 or 7 and answer respectively. Examples:
* For notice_period = 66:
  - "66" OR "2" if asked in months OR "9" if asked in weeks
* For notice_period = 15:"
  - "15" OR "0" if asked in months OR "2" if asked in weeks
* For notice_period = 0:
  - "0" OR "0" if asked in months OR "0" if asked in weeks
'''

# Your LinkedIn headline in quotes Eg: "Software Engineer @ Google, Masters in Computer Science", "Recent Grad Student @ MIT, Computer Science"
linkedin_headline = "MENG Electrical and Electronic Engineering Graduate | Embedded Systems | Full-Stack Development" # "Headline" or "" to leave this question unanswered

# Your summary in quotes, use \n to add line breaks if using single quotes "Summary".You can skip \n if using triple quotes """Summary"""
linkedin_summary = """Electrical & Electronic engineer transitioning into roles where product thinking meets hands-on engineering. Experienced in full-stack development (React, PHP, MySQL), embedded systems (Arduino, Mbed OS), and IoT platforms. Passionate about building connected systems from circuit to user experience."""

'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
''' 

# Your cover letter in quotes, use \n to add line breaks if using single quotes "Cover Letter".You can skip \n if using triple quotes """Cover Letter""" (This question makes sense though)
cover_letter = """
Gianni Zhang
33 Rockingham St | Sheffield S1 4WF
07719614213 | gzhang1819298200@gmail.com 
LinkedIn: www.linkedin.com/in/gianni-zhang-313398307 | GitHub: https://github.com/gzhang33

Dear Hiring Manager,
I’m an Electrical & Electronic engineer transitioning into roles where product thinking meets hands-on engineering. Curiosity is my engine: the first time I piloted a phone-controlled drone, I didn’t just enjoy it—I wanted to understand the decisions that made it feel effortless. Since then I’ve gravitated to problems that connect hardware, software, and users, and I’m excited to bring that builder’s mindset to product work across Product Management, Embedded/IoT, or Full-stack settings.
----------------------------------------------------------------------------------------------------------------
Project Experiences:
EV Rental and Tracking Platform					Oct. 2024 - May 2025
In the end year of the University, I got the project to design and implement a comprehensive EV rental and tracking platform that spans from device hardware to the user-facing web interface. On the embedded side, I integrated an AT6668 GNSS module with an Arduino Uno R4 WiFi, parsed raw NMEA data into structured JSON, and transmitted telemetry via HTTP to a cloud backend built with a PHP REST API and MariaDB. On the front end, I created a real-time web application using HTML/CSS/JavaScript/PHP and Leaflet.js with OpenStreetMap to provide live vehicle maps, booking flows, and trip playback. I structured the overall system using a four-layer IoT model (Sensing, Networking, Service, Interface), which helped keep responsibilities clear and the design maintainable across the full stack.
B2B E-commerce Platform 						Aug. 2025 - Sept. 2025
In roughly two weeks, I independently built a modular B2B e-commerce platform using React with TypeScript on the front end and a PHP REST API backed by MySQL on the server side. The application offers a responsive, easy-to-use customer-facing interface and a fully responsive, intuitive admin panel that enables non-technical staff to independently add, update, delete, and search product information without relying on technical administrators. To ensure that these features evolved smoothly and aligned with real user needs, I worked in short Agile-style iterations, maintaining a small backlog, delivering increments of functionality, and refining the product based on feedback. To harden the platform, I implemented prepared SQL statements, session and CSRF protection, data encryption, and TOTP-based two-factor authentication (2FA) with recovery codes and trusted device support, ensuring that business customers could rely on the system for secure transactions.
Investigation of Hardware Attacks in Approximate Computing Systems Oct. 2023 - May 2024
In my third year research project on hardware attacks in approximate computing systems, I investigated how hardware Trojans can affect the quality and precision of image processing pipelines. Using MATLAB, I modelled the integration and activation of Trojans within a Sobel-based edge detection filter and quantified their effects on image accuracy and overall system performance, including image quality degradation and computation speed. Throughout the project, I relied on MATLAB both for numerical analysis and for generating clear graphical outputs, which helped me interpret and communicate subtle behavioural changes under different Trojan scenarios.
Microcontroller-Based Password Lock System			Oct. 2022 - Jan. 2023
In a microcontroller-based password lock project, I designed and implemented a secure door access system that combined custom hardware and firmware. On the hardware side, I worked in KiCad to integrate the microcontroller, keypad, segment LCD used to display password input and system status, and status LEDs. On the software side, I used Mbed OS to implement the core logic for administrator functions such as managing user passwords, changing the admin password, and restoring default settings stored in flash memory. I also developed robust incorrect-password handling with dynamic attempt limits, progressive lockout wait times, and clear visual feedback, giving me practical experience in tying hardware behaviour and embedded software together into a cohesive, security-focused system.
----------------------------------------------------------------------------------------------------------------

Beyond project work, my engineering foundation has been shaped by a broad set of academic and team-based experiences at the University of Sheffield. I’ve collaborated in multidisciplinary groups—receiving the Professional Behaviours Team Award in the Global Engineering Challenge.  I’ve also contributed as a Student Ambassador, EEE Summer Camp Ambassador, and Women in Control ambassador, roles that strengthened communication skills and my ability to translate technical concepts for diverse audiences. These experiences, combined with hands-on work in industrial problem-solving scenarios and manufacturing tasks, have broadened the practical and collaborative perspective I bring to engineering and product work.

What I bring to a team is the ability to connect the how to the why: to translate complex systems into clear priorities, pragmatic specs, and measurable outcomes; to partner well with engineering and design because I’ve shipped across the stack; and to stay grounded in user benefit and business impact. I’m excited to contribute that blend of curiosity, execution depth, and product judgment to a team where it will matter most.
Thank you for your time. I’d welcome a conversation about where my background could be most useful—whether in Product Management, Embedded/IoT, or Full-stack—and how I can help your team ship the right things, faster and with confidence.
										Warm regards
										Gianni Zhang

"""
##> ------ Dheeraj Deshwal : dheeraj9811 Email:dheeraj20194@iiitd.ac.in/dheerajdeshwal9811@gmail.com - Feature ------

# Your user_information_all letter in quotes, use \n to add line breaks if using single quotes "user_information_all".You can skip \n if using triple quotes """user_information_all""" (This question makes sense though)
# We use this to pass to AI to generate answer from information , Assuing Information contians eg: resume  all the information like name, experience, skills, Country, any illness etc. 
user_information_all ="""
PERSONAL INFORMATION:
Name: Gianni Zhang
Address: 33 Rockingham St, Sheffield S1 4WF, UK
Phone: 07719614213
Email: gzhang1819298200@gmail.com
LinkedIn: https://www.linkedin.com/in/gianni-zhang-313398307/
GitHub: https://github.com/gzhang33
Portfolio Website: https://github.com/gzhang33

EDUCATION:
Degree: Master of Engineering (MENG) in Electrical and Electronic Engineering
University: University of Sheffield
Status: Graduate

WORK EXPERIENCE:
Years of Experience: 0 years
Most Recent Employer: Not Applicable
Notice Period: 0 days (immediately available)

CITIZENSHIP & VISA:
Nationality: Chinese (Chinese passport holder)
Residency Status: Italian Permanent Resident
UK Visa Status: UK Post-Study Work (PSW) visa holder
Citizenship Status: Non-citizen allowed to work for any employer
Work Authorization: Authorized to work for any employer in the UK under PSW visa
Visa Sponsorship Required: No

SALARY EXPECTATIONS:
Desired Salary: 30000 GBP
Current CTC: 0 GBP
Currency: GBP

PROFESSIONAL SUMMARY:
Electrical & Electronic engineer transitioning into roles where product thinking meets hands-on engineering. Experienced in full-stack development (React, PHP, MySQL), embedded systems (Arduino, Mbed OS), and IoT platforms. Passionate about building connected systems from circuit to user experience.

TECHNICAL SKILLS:
- Full-Stack Development: React, TypeScript, PHP, MySQL, HTML, CSS, JavaScript
- Embedded Systems: Arduino, Mbed OS, Microcontrollers
- IoT Platforms: Device integration, telemetry systems
- Hardware Design: KiCad (PCB design)
- Data Analysis: MATLAB
- Web Mapping: Leaflet.js, OpenStreetMap
- Security: TOTP-based 2FA, CSRF protection, data encryption, prepared SQL statements
- Development Practices: Agile methodology, REST API design

PROJECT EXPERIENCES:

1. EV Rental and Tracking Platform (October 2024 - May 2025)
   - Designed and implemented a comprehensive EV rental and tracking platform spanning from device hardware to user-facing web interface
   - Integrated AT6668 GNSS module with Arduino Uno R4 WiFi
   - Parsed raw NMEA data into structured JSON and transmitted telemetry via HTTP to cloud backend
   - Built backend with PHP REST API and MariaDB
   - Created real-time web application using HTML/CSS/JavaScript/PHP and Leaflet.js with OpenStreetMap
   - Implemented live vehicle maps, booking flows, and trip playback
   - Structured system using four-layer IoT model (Sensing, Networking, Service, Interface)

2. B2B E-commerce Platform (August 2025 - September 2025)
   - Independently built modular B2B e-commerce platform in approximately two weeks
   - Frontend: React with TypeScript
   - Backend: PHP REST API with MySQL
   - Features: Responsive customer-facing interface and fully responsive admin panel
   - Enabled non-technical staff to independently manage product information
   - Implemented security measures: prepared SQL statements, session and CSRF protection, data encryption, TOTP-based 2FA with recovery codes and trusted device support
   - Worked in Agile-style iterations with short development cycles

3. Investigation of Hardware Attacks in Approximate Computing Systems (October 2023 - May 2024)
   - Third-year research project investigating hardware Trojans in approximate computing systems
   - Used MATLAB to model integration and activation of Trojans within Sobel-based edge detection filter
   - Quantified effects on image accuracy and system performance
   - Analyzed image quality degradation and computation speed impacts
   - Generated graphical outputs for behavioral analysis under different Trojan scenarios

4. Microcontroller-Based Password Lock System (October 2022 - January 2023)
   - Designed and implemented secure door access system combining custom hardware and firmware
   - Hardware: Used KiCad to integrate microcontroller, keypad, segment LCD, and status LEDs
   - Software: Implemented core logic using Mbed OS
   - Features: Administrator functions for managing user passwords, changing admin password, restoring default settings stored in flash memory
   - Security: Implemented robust incorrect-password handling with dynamic attempt limits, progressive lockout wait times, and clear visual feedback

ADDITIONAL EXPERIENCES:
- Received Professional Behaviours Team Award in Global Engineering Challenge
- Student Ambassador at University of Sheffield
- EEE Summer Camp Ambassador
- Women in Control Ambassador
- Experience in industrial problem-solving scenarios and manufacturing tasks
- Strong communication skills and ability to translate technical concepts for diverse audiences

CONFIDENCE LEVEL:
Experience building web or mobile applications: 6/10 (on a scale of 1-10)

HEALTH INFORMATION:
No known illnesses or health conditions that would affect work ability.
"""
##<
'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
''' 

# Name of your most recent employer
recent_employer = "Not Applicable" # "", "Lala Company", "Google", "Snowflake", "Databricks"

# Example question: "On a scale of 1-10 how much experience do you have building web or mobile applications? 1 being very little or only in school, 10 being that you have built and launched applications to real users"
confidence_level = "6"             # Any number between "1" to "10" including 1 and 10, put it in quotes ""
##



# >>>>>>>>>>> RELATED SETTINGS <<<<<<<<<<<

## Allow Manual Inputs
# Should the tool pause before every submit application during easy apply to let you check the information?
pause_before_submit = False         # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''

# Should the tool pause if it needs help in answering questions during easy apply?
# Note: If set as False will answer randomly...
pause_at_failed_question = False    # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''
##

# Do you want to overwrite previous answers?
overwrite_previous_answers = False # True or False, Note: True or False are case-sensitive







############################################################################################################
'''
THANK YOU for using my tool 😊! Wishing you the best in your job hunt 🙌🏻!

Sharing is caring! If you found this tool helpful, please share it with your peers 🥺. Your support keeps this project alive.

Support my work on <PATREON_LINK>. Together, we can help more job seekers.

As an independent developer, I pour my heart and soul into creating tools like this, driven by the genuine desire to make a positive impact.

Your support, whether through donations big or small or simply spreading the word, means the world to me and helps keep this project alive and thriving.

Gratefully yours 🙏🏻,
Sai Vignesh Golla
'''
############################################################################################################