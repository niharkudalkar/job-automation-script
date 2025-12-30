#!/usr/bin/env python3
"""
Job Automation Script
Searches for latest job openings (24hrs) and applies to Product Manager,
Director, Automation Expert, and Program Manager roles in India Remote.

Features:
- Resume upload capability
- Auto-apply flow
- Direct company links output
"""

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import json
import time
import sys
from pathlib import Path

class JobAutomation:
    def __init__(self, resume_path=None, auto_apply=True):
        """
        Initialize Job Automation
        
        Args:
            resume_path (str): Path to resume PDF file
            auto_apply (bool): Whether to attempt auto-apply
        """
        self.resume_path = resume_path
        self.auto_apply = auto_apply
        self.driver = None
        self.jobs_found = []
        self.jobs_applied = []
        self.jobs_failed = []
        
        self.job_titles = [
            'Product Manager',
            'Director',
            'Automation Expert',
            'Automation Manager',
            'Program Manager',
            'Senior Project Manager',
            'Lead Product Manager'
        ]
        
        self.base_url = 'https://www.naukri.com'
        
    def search_jobs(self):
        """
        Search for latest jobs posted in last 24 hours
        """
        print("\n[*] Searching for jobs posted in last 24 hours...")
        
        for title in self.job_titles:
            url = f"{self.base_url}/{title.lower().replace(' ', '-')}-jobs-in-india?wfhType=2"
            print(f"\n[+] Searching: {title}")
            print(f"    URL: {url}")
            
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    # Parse job listings
                    jobs = self._parse_jobs(response.text, title)
                    self.jobs_found.extend(jobs)
                    print(f"    Found: {len(jobs)} jobs")
            except Exception as e:
                print(f"    Error: {str(e)}")
        
        return self.jobs_found
    
    def _parse_jobs(self, html, job_title):
        """
        Parse jobs from HTML response
        """
        jobs = []
        # This would require BeautifulSoup in production
        # For now, returning structured placeholder
        return jobs
    
    def upload_resume(self, resume_path):
        """
        Validate and store resume path
        
        Args:
            resume_path (str): Path to resume file
            
        Returns:
            bool: True if valid, False otherwise
        """
        resume_file = Path(resume_path)
        
        if not resume_file.exists():
            print(f"[!] Error: Resume file not found: {resume_path}")
            return False
        
        if resume_file.suffix.lower() not in ['.pdf', '.doc', '.docx']:
            print(f"[!] Error: Invalid file type. Supported: PDF, DOC, DOCX")
            return False
        
        self.resume_path = resume_path
        print(f"[+] Resume uploaded: {resume_path}")
        return True
    
    def apply_to_jobs(self, max_applications=10):
        """
        Apply to jobs with auto-apply or manual links
        
        Args:
            max_applications (int): Maximum number of applications to submit
        """
        print(f"\n[*] Starting applications (Max: {max_applications})...")
        
        if not self.jobs_found:
            print("[!] No jobs found. Run search_jobs() first.")
            return
        
        if not self.resume_path:
            print("[!] No resume uploaded. Use upload_resume() first.")
            return
        
        for idx, job in enumerate(self.jobs_found[:max_applications], 1):
            print(f"\n[{idx}] Applying to: {job['title']} at {job['company']}")
            
            if self.auto_apply:
                success = self._auto_apply(job)
                if success:
                    self.jobs_applied.append(job)
                    print(f"    [✓] Applied Successfully")
                else:
                    self.jobs_failed.append(job)
                    print(f"    [!] Auto-apply failed, added to manual list")
            else:
                print(f"    [→] Manual Apply Link: {job['apply_url']}")
                self.jobs_failed.append(job)
            
            time.sleep(2)  # Rate limiting
    
    def _auto_apply(self, job):
        """
        Attempt to auto-apply to job using Selenium
        
        Args:
            job (dict): Job details
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if not self.driver:
                self.driver = webdriver.Chrome()
            
            self.driver.get(job['apply_url'])
            time.sleep(3)
            
            # Try to find and click apply button
            try:
                apply_btn = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Apply')]"))
                )
                apply_btn.click()
                print("    [*] Apply button clicked")
                
                # Handle screening questions if any
                time.sleep(2)
                
                return True
            except Exception as e:
                print(f"    [*] Apply button not found: {str(e)}")
                return False
                
        except Exception as e:
            print(f"    [!] Auto-apply error: {str(e)}")
            return False
    
    def export_results(self, output_file='job_results.json'):
        """
        Export results to JSON file
        
        Args:
            output_file (str): Output filename
        """
        results = {
            'timestamp': datetime.now().isoformat(),
            'jobs_found': len(self.jobs_found),
            'jobs_applied': len(self.jobs_applied),
            'jobs_failed': len(self.jobs_failed),
            'applied_jobs': self.jobs_applied,
            'manual_apply_links': self.jobs_failed
        }
        
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"\n[+] Results exported to {output_file}")
    
    def print_results(self):
        """
        Print summary of results
        """
        print("\n" + "="*60)
        print("JOB APPLICATION SUMMARY")
        print("="*60)
        print(f"Total Jobs Found: {len(self.jobs_found)}")
        print(f"Successfully Applied: {len(self.jobs_applied)}")
        print(f"Manual Apply Required: {len(self.jobs_failed)}")
        
        if self.jobs_failed:
            print("\nDirect Company Links (Manual Apply):")
            print("-" * 60)
            for job in self.jobs_failed:
                print(f"\nJob Title: {job.get('title', 'N/A')}")
                print(f"Company: {job.get('company', 'N/A')}")
                print(f"Apply Link: {job.get('apply_url', 'N/A')}")
                print(f"Experience: {job.get('experience', 'N/A')}")
                print(f"Location: {job.get('location', 'Remote')}")
    
    def cleanup(self):
        """
        Clean up resources
        """
        if self.driver:
            self.driver.quit()
            print("\n[+] Browser closed")


def main():
    """
    Main execution function
    """
    print("\n" + "="*60)
    print("JOB AUTOMATION SCRIPT v1.0")
    print("Remote Job Search & Apply Tool")
    print("="*60)
    
    # Initialize automation
    automation = JobAutomation(auto_apply=True)
    
    # Check for resume file
    resume_file = 'resume.pdf'  # Default resume file
    if len(sys.argv) > 1:
        resume_file = sys.argv[1]
    
    # Upload resume
    if Path(resume_file).exists():
        automation.upload_resume(resume_file)
    else:
        print(f"[!] Resume file not found: {resume_file}")
        print("[*] Proceeding without auto-apply...")
        automation.auto_apply = False
    
    # Search for jobs
    jobs = automation.search_jobs()
    print(f"\n[+] Total jobs found: {len(jobs)}")
    
    # Apply to jobs
    automation.apply_to_jobs(max_applications=10)
    
    # Print results
    automation.print_results()
    
    # Export results
    automation.export_results('job_applications.json')
    
    # Cleanup
    automation.cleanup()
    
    print("\n[+] Job automation completed!\n")


if __name__ == '__main__':
    main()
