#!/usr/bin/env python3

import os
import base64
from pathlib import Path
from github import Github
from typing import List, Dict


def get_json_files_from_repo(
    repo_name: str = "OpenCloning/OpenCloning-submission",
    target_dir: str = "processed",
    output_dir: str = "src/data/templates",
) -> List[Dict]:
    """
    Download JSON files from a GitHub repository's processed directory.

    Args:
        repo_name: The repository name in format 'owner/repo'
        target_dir: The directory in the repo to search for JSON files
        output_dir: Local directory to save the files

    Returns:
        List of dictionaries containing file information
    """
    # Initialize GitHub client (uses GITHUB_TOKEN if available)
    g = Github(os.getenv("GITHUB_TOKEN"))

    # Get the repository
    repo = g.get_repo(repo_name)

    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Get contents of the processed directory
    contents = repo.get_contents(target_dir)

    downloaded_files = []

    # Process all subdirectories
    while contents:
        file_content = contents.pop(0)

        if file_content.type == "dir":
            # Add subdirectory contents to the stack
            contents.extend(repo.get_contents(file_content.path))

        elif file_content.type == "file" and file_content.name.endswith(".json"):
            try:
                # Get the file content
                file_data = base64.b64decode(file_content.content).decode("utf-8")

                # Create subdirectories if needed
                relative_path = file_content.path.replace(target_dir + "/", "")
                output_path = os.path.join(output_dir, relative_path)
                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                # Save the file
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(file_data)

                downloaded_files.append({"path": relative_path, "full_path": output_path, "size": file_content.size})

                print(f"Downloaded: {relative_path}")

            except Exception as e:
                print(f"Error downloading {file_content.path}: {str(e)}")

    return downloaded_files


def main():
    """Main function to execute the download process."""
    print("Starting test data download...")
    downloaded = get_json_files_from_repo(
        repo_name="OpenCloning/OpenCloning-submission", target_dir="processed", output_dir="src/data/templates"
    )
    # downloaded += get_json_files_from_repo(
    #     repo_name="manulera/OpenCloning_frontend", target_dir="public/examples", output_dir="src/data/examples"
    # )
    print(f"\nDownload complete! Downloaded {len(downloaded)} files.")
    for file in downloaded:
        print(f"- {file['path']} ({file['size']} bytes)")


if __name__ == "__main__":
    main()
