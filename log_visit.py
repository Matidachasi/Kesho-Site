#!/usr/bin/env python3
from datetime import datetime
import os
import json
import socket

# Configuration
LOG_FILE = "/var/www/html/env-news/kesho_visits.log"
JSON_LOG = "/var/www/html/env-news/kesho_visits.json"

def log_visit():
    """
    Log website visit with timestamp, page info, and visitor IP
    Returns: Status message
    """
    # Get current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Get hostname for identification
    hostname = socket.gethostname()
    
    # Extract environment variables that might be available
    page = os.environ.get('HTTP_REFERER', 'direct')
    visitor_ip = os.environ.get('REMOTE_ADDR', 'unknown')
    user_agent = os.environ.get('HTTP_USER_AGENT', 'unknown')
    
    # Create log entry text
    log_entry = f"[{timestamp}] IP: {visitor_ip} | Page: {page} | Agent: {user_agent}\n"
    
    # Write to text log file
    try:
        with open(LOG_FILE, "a") as log:
            log.write(log_entry)
    except Exception as e:
        return f"Error writing to log file: {str(e)}"
    
    # Create JSON record
    visit_data = {
        "timestamp": timestamp,
        "hostname": hostname,
        "page": page,
        "visitor_ip": visitor_ip,
        "user_agent": user_agent
    }
    
    # Update JSON log file
    try:
        # If JSON file exists, read it first
        if os.path.exists(JSON_LOG):
            try:
                with open(JSON_LOG, 'r') as f:
                    data = json.load(f)
                    # Make sure it has the expected structure
                    if not isinstance(data, dict) or "visits" not in data:
                        data = {"visits": []}
            except (json.JSONDecodeError, FileNotFoundError):
                # If file is corrupted or can't be read, start fresh
                data = {"visits": []}
        else:
            # Create new data structure
            data = {"visits": []}
        
        # Add new visit
        data["visits"].append(visit_data)
        
        # Write updated data back to file
        with open(JSON_LOG, 'w') as f:
            json.dump(data, f, indent=2)
            
        return "Visit logged successfully"
    except Exception as e:
        return f"Error updating JSON log: {str(e)}"

# Create a simple function to get visit statistics
def get_visit_stats():
    """
    Get basic statistics about site visits
    Returns: Dictionary with visit statistics
    """
    try:
        if os.path.exists(JSON_LOG):
            with open(JSON_LOG, 'r') as f:
                data = json.load(f)
                visits = data.get("visits", [])
                
                # Count total visits
                total_visits = len(visits)
                
                # Get unique IPs
                unique_ips = len(set(v["visitor_ip"] for v in visits if v["visitor_ip"] != "unknown"))
                
                # Get most recent visit
                most_recent = visits[-1]["timestamp"] if visits else "No visits yet"
                
                return {
                    "total_visits": total_visits,
                    "unique_visitors": unique_ips,
                    "most_recent": most_recent
                }
        else:
            return {
                "total_visits": 0,
                "unique_visitors": 0,
                "most_recent": "No visits yet"
            }
    except Exception as e:
        return {
            "error": str(e),
            "total_visits": 0,
            "unique_visitors": 0,
            "most_recent": "Error retrieving data"
        }

if __name__ == "__main__":
    # If script is run directly, log a visit
    result = log_visit()
    print("Content-Type: text/plain")
    print()
    print(result)