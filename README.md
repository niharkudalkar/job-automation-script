# Job Automation Script

Automated job application script that searches for latest job openings (posted within 24 hours) and applies to Product Manager, Director, Automation Expert, and Program Manager roles in India Remote.

## Features

✅ **Automated Job Search** - Searches for latest openings posted within 24 hours
✅ **Resume Upload** - Support for PDF, DOC, DOCX resume formats
✅ **Auto-Apply** - Automatically fills and submits job applications using Selenium WebDriver
✅ **Screening Questions** - Intelligently answers common screening questions from CV data
✅ **Form Auto-Filling** - Automatically fills application forms with candidate information
✅ **Manual Links Export** - Returns direct company application links when auto-apply fails
✅ **Results Export** - Exports results to JSON with statistics and links
✅ **Candidate Data** - Uses comprehensive CV information for all applications

## Target Job Roles

- Product Manager
- Senior Product Manager
- Lead Product Manager
- Project Manager
- Senior Project Manager
- Lead Project Manager
- Automation Expert
- Automation Manager
- Program Manager
- Delivery Manager
- Director

## Tech Stack

- **Language:** Python 3.8+
- **Web Automation:** Selenium WebDriver
- **HTTP Requests:** Requests Library
- **HTML Parsing:** BeautifulSoup4
- **Job Platforms:** Naukri.com
- **Data Management:** JSON

## Installation

### Prerequisites

- Python 3.8 or higher
- Google Chrome browser
- pip (Python package manager)

### Setup

1. **Clone the repository:**
```bash
git clone https://github.com/niharkudalkar/job-automation-script.git
cd job-automation-script
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Download ChromeDriver:**
```bash
# ChromeDriver is automatically managed by webdriver-manager
# No manual download needed
```

## Configuration

### Edit Candidate Information

Update `candidate_config.py` with your personal information:

```python
CANDIDATE = {
    'first_name': 'Your Name',
    'last_name': 'Your Surname',
    'email': 'your.email@example.com',
    'phone': '+91 XXXXXXXXXX',
    'linkedin': 'https://www.linkedin.com/in/yourprofile/',
    # ... other fields
}
```

### Update Work Experience

```python
WORK_EXPERIENCE = [
    {
        'company': 'Company Name',
        'designation': 'Your Designation',
        'location': 'City',
        'start_date': 'Month Year',
        'end_date': 'Present or Month Year',
        'duration_years': 'X years',
        'responsibilities': ['Task 1', 'Task 2', ...]
    },
    # ... more experiences
]
```

### Update Salary Information

```python
SALARY = {
    'current_ctc': 2100000,  # In rupees
    'current_ctc_display': '21',  # In Lacs
    'expected_ctc': 2800000,  # In rupees
    'expected_ctc_display': '28',  # In Lacs
    'notice_period': 'Serving Notice Period',
}
```

## Usage

### Basic Usage

```bash
python job_automation.py
```

### With Resume File

```bash
python job_automation.py resume.pdf
```

### With Custom Settings

```bash
python job_automation.py --resume resume.pdf --auto-apply --max-applications 20
```

## How It Works

### 1. Job Search Phase
- Searches Naukri.com for jobs matching specified roles
- Filters for jobs posted within last 24 hours
- Filters for Remote work mode only
- Collects job URLs and details

### 2. Application Phase
- Iterates through found jobs
- For each job:
  - Opens job application page using Selenium
  - Attempts to locate and fill application form
  - Auto-fills with candidate information from `candidate_config.py`
  - Answers screening questions intelligently
  - Submits application

### 3. Form Auto-Filling
The script automatically fills:
- Personal Information (Name, Email, Phone)
- Professional Details (Company, Designation, Experience)
- Skills and Competencies
- Salary Information (Current & Expected)
- Notice Period
- LinkedIn Profile
- Location and Address
- Screening Question Responses

### 4. Output Generation
- Tracks successful applications
- Records failed applications
- Collects direct company links for manual applications
- Exports results to `job_applications.json`
- Generates application summary report

## Output Files

### job_applications.json
Contains:
- Timestamp of execution
- Total jobs found
- Successfully applied jobs
- Jobs requiring manual application
- Direct company links
- Application details

**Example:**
```json
{
  "timestamp": "2025-01-01T10:30:45.123456",
  "jobs_found": 47,
  "jobs_applied": 10,
  "jobs_failed": 37,
  "applied_jobs": [
    {
      "title": "Product Manager",
      "company": "Company Name",
      "apply_url": "https://...",
      "status": "Applied"
    }
  ],
  "manual_apply_links": [
    {
      "title": "Senior Product Manager",
      "company": "Other Company",
      "apply_url": "https://...",
      "experience": "7-12 Years",
      "location": "Remote"
    }
  ]
}
```

## Screening Questions Handled

The script intelligently answers common questions:

- "How many years of experience do you have in Product Management?"
- "How many years of experience do you have in Project Management?"
- "How many years of experience do you have in Agile?"
- "How many years of experience do you have in Delivery Management?"
- "What is your current salary (CTC in Lacs per annum)?"
- "What is your expected salary (CTC in Lacs per annum)?"
- "What is your notice period?"
- "Which development technologies have you worked with?"
- "Do you have any AI exposure?"
- "Would you be open to working with a startup?"
- "LinkedIn Profile URL"
- Custom text input fields

## Error Handling

The script includes robust error handling for:
- Network timeouts
- Element not found errors
- Invalid resume file formats
- Failed form submissions
- Browser crashes
- Session timeouts

## Best Practices

1. **Resume Preparation:**
   - Use ATS-friendly resume format
   - Include all relevant keywords from job description
   - Keep formatting simple (PDF recommended)

2. **Candidate Profile:**
   - Update all fields in `candidate_config.py`
   - Ensure email and phone are correct
   - Update work experience regularly
   - Add new certifications as you get them

3. **Execution:**
   - Run script during off-peak hours for better performance
   - Monitor first few applications manually
   - Check `job_applications.json` for results
   - Use manual links for failed applications

4. **Results Review:**
   - Review applications submitted
   - Follow up on manual application links
   - Track application status in Naukri dashboard
   - Update profile based on feedback

## Limitations

- Works specifically with Naukri.com platform
- Requires stable internet connection
- Chrome browser must be installed
- Some job portals may have anti-bot protections
- Screening questions vary by job posting
- Resume upload may fail on some sites

## Troubleshooting

### Script hangs or crashes
```bash
# Increase timeout values in job_automation.py
WAIT_TIMEOUT = 15  # Increase from 10
```

### ChromeDriver errors
```bash
# Update webdriver-manager
pip install --upgrade webdriver-manager
```

### Resume not uploading
- Verify file is PDF, DOC, or DOCX
- Check file size (< 5MB recommended)
- Try manual upload first

### Form not filling correctly
- Update field mapping in `candidate_config.py`
- Check if website layout has changed
- Report issue with specific URL

## Future Enhancements

- [ ] Support for multiple job portals (LinkedIn, Indeed, Foundit)
- [ ] Email notifications for successful applications
- [ ] Database integration for application tracking
- [ ] Advanced screening question AI
- [ ] Cover letter generation
- [ ] Interview preparation materials
- [ ] Salary negotiation insights
- [ ] Web-based dashboard for monitoring

## Legal Disclaimer

This tool is designed for automating personal job applications. Users are responsible for:
- Complying with website terms of service
- Avoiding rapid submissions that may trigger anti-bot systems
- Providing accurate information in applications
- Respecting company application guidelines

## Support

For issues, questions, or suggestions:
1. Check existing GitHub issues
2. Create new issue with detailed description
3. Include error messages and console output
4. Provide candidate_config.py snippet (without sensitive data)

## License

MIT License - Feel free to use and modify for personal use

## Author

**Nihar Kudalkar**
- Email: Nihar.kudalkar@yahoo.com
- LinkedIn: https://www.linkedin.com/in/niharkudalkar/
- GitHub: https://github.com/niharkudalkar

## Disclaimer

This project is provided as-is for educational purposes. Users are responsible for ensuring their use complies with all applicable laws and website terms of service. The author is not liable for any misuse or damages.

---

**Last Updated:** December 30, 2025
**Version:** 1.0.0
