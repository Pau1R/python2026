#!/usr/bin/env python3
"""
SIMULATED VIRUS FOR TESTING ANTIVIRUS SYSTEMS
This is a harmless demonstration that mimics virus behaviors for educational purposes only.
DO NOT use for malicious purposes.
"""

import os
import time
import random
import json
from datetime import datetime

class SimulatedVirus:
    """A simulated virus that demonstrates common malware behaviors safely."""
    
    def __init__(self):
        self.infected_files = []
        self.signature = "VIRUS_SIM_DEMO_2024"
        self.start_time = datetime.now()
        
    def replicate(self, target_dir="test_infected"):
        """Simulate file replication - creates harmless test files."""
        print(f"[VIRUS] Starting replication in {target_dir}")
        
        # Create target directory if it doesn't exist
        os.makedirs(target_dir, exist_ok=True)
        
        # Create multiple copies with different names
        for i in range(5):
            filename = f"infected_{i}_{random.randint(1000, 9999)}.txt"
            filepath = os.path.join(target_dir, filename)
            
            with open(filepath, 'w') as f:
                f.write(f"This is a simulated infected file.\n")
                f.write(f"Signature: {self.signature}\n")
                f.write(f"Created: {datetime.now()}\n")
                f.write(f"Payload: DEMO_PAYLOAD_{i}\n")
            
            self.infected_files.append(filepath)
            print(f"[VIRUS] Created: {filename}")
            time.sleep(0.1)  # Small delay to simulate real behavior
    
    def modify_system_files(self, test_dir="test_system"):
        """Simulate modification of system files (creates test files only)."""
        print(f"[VIRUS] Simulating system file modification in {test_dir}")
        
        os.makedirs(test_dir, exist_ok=True)
        
        # Simulate modifying "system" files
        system_files = ["system32.dll", "kernel.sys", "boot.ini", "hosts.txt"]
        
        for filename in system_files:
            filepath = os.path.join(test_dir, filename)
            with open(filepath, 'w') as f:
                f.write(f"# Modified by simulated virus\n")
                f.write(f"# Original backed up at {datetime.now()}\n")
                f.write(f"# Signature: {self.signature}\n")
                # Add some malicious-looking content
                f.write("redirect http://malicious-site.com\n")
            
            print(f"[VIRUS] Modified: {filename}")
    
    def create_backdoor(self, backdoor_dir="test_backdoor"):
        """Simulate creating a backdoor - creates a harmless test script."""
        print(f"[VIRUS] Creating backdoor in {backdoor_dir}")
        
        os.makedirs(backdoor_dir, exist_ok=True)
        
        backdoor_code = '''#!/usr/bin/env python3
# Simulated backdoor for testing
import socket
import json

def connect_to_c2():
    """Simulate connection to command and control server."""
    print("[BACKDOOR] Attempting to connect to C2 server...")
    # This is just a simulation - no real connection made
    return False

def execute_command(cmd):
    """Simulate executing remote commands."""
    print(f"[BACKDOOR] Would execute: {cmd}")
    return "Command executed"

if __name__ == "__main__":
    print("Backdoor simulation started")
    connect_to_c2()
'''
        
        backdoor_path = os.path.join(backdoor_dir, "backdoor.py")
        with open(backdoor_path, 'w') as f:
            f.write(backdoor_code)
        
        print(f"[VIRUS] Backdoor created: backdoor.py")
    
    def encrypt_files(self, test_dir="test_encrypt"):
        """Simulate file encryption - creates "encrypted" test files."""
        print(f"[VIRUS] Simulating file encryption in {test_dir}")
        
        os.makedirs(test_dir, exist_ok=True)
        
        # Create some "encrypted" files
        for i in range(3):
            original = f"document_{i}.txt"
            encrypted = f"document_{i}.txt.encrypted"
            
            # Create "original"
            with open(os.path.join(test_dir, original), 'w') as f:
                f.write(f"This is document {i}\n")
                f.write("Important content here\n")
            
            # Create "encrypted" version (just base64-like encoding)
            with open(os.path.join(test_dir, encrypted), 'w') as f:
                f.write(f"ENCRYPTED:{self.signature}:")
                f.write("VGhpcyBpcyBhbiBlbmNyeXB0ZWQgZmlsZQ==\n")  # Base64 for demo
                f.write(f"Key: DEMO_KEY_{i}\n")
            
            print(f"[VIRUS] Encrypted: {original} -> {encrypted}")
    
    def create_registry_mods(self, test_dir="test_registry"):
        """Simulate registry modifications - creates a test JSON file."""
        print(f"[VIRUS] Simulating registry modifications")
        
        os.makedirs(test_dir, exist_ok=True)
        
        registry_mods = {
            "HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run": {
                "VirusDemo": "C:\\Windows\\System32\\virus_demo.exe"
            },
            "HKCU\\Software\\SecuritySettings": {
                "AntivirusDisabled": "true",
                "FirewallBypass": "enabled"
            }
        }
        
        reg_file = os.path.join(test_dir, "registry_mods.json")
        with open(reg_file, 'w') as f:
            json.dump(registry_mods, f, indent=2)
        
        print(f"[VIRUS] Registry modifications saved to: registry_mods.json")
    
    def spread_to_network(self, network_dir="test_network"):
        """Simulate network spreading - creates test files."""
        print(f"[VIRUS] Simulating network spread")
        
        os.makedirs(network_dir, exist_ok=True)
        
        # Simulate spreading to network shares
        network_shares = ["\\\\SERVER\\Share", "\\\\PC01\\Documents", "\\\\PC02\\Downloads"]
        
        for share in network_shares:
            safe_share_name = share.replace("\\", "_").replace(":", "")
            filepath = os.path.join(network_dir, f"spread_{safe_share_name}.txt")
            
            with open(filepath, 'w') as f:
                f.write(f"Virus spread to: {share}\n")
                f.write(f"Signature: {self.signature}\n")
                f.write(f"Time: {datetime.now()}\n")
            
            print(f"[VIRUS] Spread to network share: {share}")
    
    def run_payload(self):
        """Execute the main virus payload - all simulated actions."""
        print("=" * 50)
        print("SIMULATED VIRUS EXECUTION STARTED")
        print("=" * 50)
        print(f"Signature: {self.signature}")
        print(f"Started at: {self.start_time}")
        print()
        
        # Execute all virus behaviors
        self.replicate()
        self.modify_system_files()
        self.create_backdoor()
        self.encrypt_files()
        self.create_registry_mods()
        self.spread_to_network()
        
        print()
        print("=" * 50)
        print("SIMULATED VIRUS EXECUTION COMPLETED")
        print("=" * 50)
        print(f"Total files created: {len(self.infected_files)}")
        print(f"Execution time: {datetime.now() - self.start_time}")
        print()
        print("NOTE: This was a harmless simulation for testing purposes.")
        print("No actual system damage was caused.")
    
    def cleanup(self):
        """Clean up all created test files."""
        print("\n[VIRUS] Cleaning up test files...")
        
        test_dirs = [
            "test_infected",
            "test_system", 
            "test_backdoor",
            "test_encrypt",
            "test_registry",
            "test_network"
        ]
        
        import shutil
        for dir_name in test_dirs:
            if os.path.exists(dir_name):
                shutil.rmtree(dir_name)
                print(f"[VIRUS] Removed: {dir_name}/")
        
        print("[VIRUS] Cleanup completed.")

def main():
    """Main function to run the simulated virus."""
    virus = SimulatedVirus()
    
    try:
        # Run the simulated virus
        virus.run_payload()
        
        # Wait a bit before cleanup
        print("\nPress Ctrl+C to cleanup now, or wait 5 seconds for auto-cleanup...")
        time.sleep(5)
        
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
    finally:
        # Always cleanup
        virus.cleanup()

if __name__ == "__main__":
    main()
