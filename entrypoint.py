#!/usr/bin/env python3
import os
import subprocess

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        raise

def main():
    # Upgrade pip and install requirements if requirements.txt exists
    if os.path.exists("/opt/airflow/requirements.txt"):
        run_command("python -m pip install --upgrade pip")
        run_command("pip install --user -r /opt/airflow/requirements.txt")

    # Initialize the Airflow database if it doesn't exist
    if not os.path.exists("/opt/airflow/airflow.db"):
        run_command("airflow db init")
        run_command(
            "airflow users create "
            "--username admin --firstname admin --lastname admin "
            "--role Admin --email admin@example.com --password admin"
        )

    # Upgrade the database to the latest version
    run_command("airflow db upgrade")

    # Start the Airflow webserver
    run_command("airflow webserver")

if __name__ == "__main__":
    main()