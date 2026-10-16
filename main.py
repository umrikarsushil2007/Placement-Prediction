import os
import sys

# Ensure project root is in sys.path
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

def main():
    print("=" * 60)
    print("   Placement Prediction System - Windows Ready")
    print("=" * 60)

    # 1. Ensure required directories exist
    required_dirs = [
        os.path.join(PROJECT_ROOT, "Data"),
        os.path.join(PROJECT_ROOT, "Models"),
        os.path.join(PROJECT_ROOT, "Results"),
        os.path.join(PROJECT_ROOT, "App", "static", "charts"),
    ]
    for d in required_dirs:
        os.makedirs(d, exist_ok=True)

    # 2. Check data files
    data_file = os.path.join(PROJECT_ROOT, "Data", "placement_data.csv")
    if not os.path.exists(data_file):
        print(f"[-] Warning: Dataset not found at {data_file}")
    else:
        print("[+] Placement dataset verified.")

    # 3. Import and launch Flask App
    try:
        from App.app import app
        print("\n[+] Starting Web Application on http://127.0.0.1:5002 ...")
        print("[+] Open your browser and navigate to: http://127.0.0.1:5002")
        print("=" * 60 + "\n")
        app.run(host="127.0.0.1", port=5002, debug=False)
    except Exception as e:
        print(f"[-] Error starting application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
