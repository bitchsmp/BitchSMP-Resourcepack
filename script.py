import os
import json

# Ask for namespace
namespace = input("Enter the namespace (e.g., dueris): ").strip()

# Define base paths
base_path = os.path.join("assets", namespace)
item_model_path = os.path.join(base_path, "models", "item")
item_data_path = os.path.join(base_path, "items")

# Create necessary directories
os.makedirs(item_model_path, exist_ok=True)
os.makedirs(item_data_path, exist_ok=True)

print("\nEnter item names to create. Type 'exit' to exit.\n")

while True:
    # Ask for item name
    item_name = input("Enter the item name (or 'exit' to exit): ").strip()
    if item_name.lower() == "exit":
        print("Exiting...")
        break

    # Define JSON content for item model
    model_content = {
        "parent": "minecraft:item/generated",
        "textures": {
            "layer0": f"{namespace}:item/{item_name}"
        }
    }

    # Define JSON content for item model definition
    item_content = {
        "model": {
            "type": "model",
            "model": f"{namespace}:item/{item_name}"
        }
    }

    # File paths
    model_file_path = os.path.join(item_model_path, f"{item_name}.json")
    item_file_path = os.path.join(item_data_path, f"{item_name}.json")

    # Write JSON files
    with open(model_file_path, "w", encoding="utf-8") as f:
        json.dump(model_content, f, indent=2)

    with open(item_file_path, "w", encoding="utf-8") as f:
        json.dump(item_content, f, indent=2)

    print(f"Created:\n  {model_file_path}\n  {item_file_path}\n")
