# update_readme.py
from datetime import datetime

def update_readme():
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    
    with open("README.md", "r") as f:
        content = f.read()
    
    # Update or append a timestamp line
    if "<!-- LAST_UPDATED -->" in content:
        lines = content.split("\n")
        new_lines = []
        for line in lines:
            if line.startswith("<!-- LAST_UPDATED -->"):
                new_lines.append(f"<!-- LAST_UPDATED --> Last auto-updated: `{now}`")
            else:
                new_lines.append(line)
        new_content = "\n".join(new_lines)
    else:
        new_content = content + f"\n\n<!-- LAST_UPDATED --> Last auto-updated: `{now}`"
    
    with open("README.md", "w") as f:
        f.write(new_content)

if __name__ == "__main__":
    update_readme()
    print("README updated successfully!")  
