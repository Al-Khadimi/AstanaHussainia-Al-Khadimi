import json

# Load updates from the JSON file
with open("updates.json", "r") as file:
    updates = json.load(file)

# Read the existing documentation
with open("project_documentation.md", "r") as file:
    documentation = file.readlines()

# Append new updates to the Development Progress section
for i, line in enumerate(documentation):
    if "## Development Progress" in line:
        documentation.insert(i + 2, "### Recent Updates\n")
        for feature in updates["features"]:
            documentation.insert(i + 3, f"- {feature}\n")
        for task in updates["tasks"]:
            documentation.insert(i + 3 + len(updates["features"]), f"- {task}\n")
        break

# Save the updated documentation
with open("project_documentation.md", "w") as file:
    file.writelines(documentation)

print("Documentation updated successfully!")
