import json
import re

classification_text = """1
1. maj (#H.II.3.h.)
2
23. juli første hundedag (#H.II.3.p.) [no]
A
Abort (#E.III.2.)
Adam og Eva (#J.IV.6.) [no]
Adopsjon (#E.VII.5.) [no]
Advent (#H.II.2.e.)
..osv
""".strip()

# ------------------------------------------------------------------------
# STEP 1: Read and parse each line, capture term + termid if it has (#....)
#         Skip any line that contains [no].
# ------------------------------------------------------------------------

pattern = re.compile(r"^(.*?)\s*\(#([^)]*)\)\s*$")

all_entries = []
for raw_line in classification_text.split("\n"):
    line = raw_line.strip()
    if not line:
        continue  # skip blank lines
    # skip lines containing '[no]'
    if "[no]" in line:
        continue
    
    match = pattern.search(line)
    if match:
        # Group 1 = term, Group 2 = everything after '#' but before the final ')'
        term = match.group(1).strip()
        termid = "#" + match.group(2).strip()
        # Example: term = "Abort", termid = "#E.III.2."
        # Store it
        all_entries.append((term, termid))

# ------------------------------------------------------------------------
# STEP 2: Build a dict of nodes by termid, each node has:
#         {
#           "term": ...,
#           "termid": ...,
#           "children": []
#         }
# ------------------------------------------------------------------------

nodes = {}
for (term, termid) in all_entries:
    nodes[termid] = {
        "term": term,
        "termid": termid,
        "children": []
    }

# ------------------------------------------------------------------------
# STEP 3: A helper to find the parent termid:
#         - remove trailing "." if present
#         - remove last segment
#         - re-add trailing "." if it’s still non-empty
#         Example: "#K.V.1.a." => parent "#K.V.1."
#                  "#K.V.1."   => parent "#K.V."
#                  "#K.V."     => parent "#K."
#                  "#K."       => no parent -> None
# ------------------------------------------------------------------------
def get_parent_tid(tid):
    # remove trailing '.' if present
    if tid.endswith('.'):
        tid = tid[:-1]  # remove the last dot
    
    if '.' not in tid:
        return None  # e.g. "#K" -> top-level if we never had a dot
    
    # split by '.'
    parts = tid.split('.')
    # the last piece is the final segment after the last dot
    # remove it
    parts.pop()  # this was the final segment
    
    if not parts:
        return None
    
    # join back with '.', then re-append a trailing dot
    parent = ".".join(parts) + "."
    return parent

# ------------------------------------------------------------------------
# STEP 4: Link each node to its parent. If parent doesn't exist in dict,
#         it means it’s a top-level node (we’ll store it separately).
# ------------------------------------------------------------------------

children_found = set()
for tid, node in nodes.items():
    parent_tid = get_parent_tid(tid)
    if parent_tid in nodes:
        # attach me to my parent's children
        nodes[parent_tid]["children"].append(node)
        children_found.add(tid)

# The top-level nodes are those that never appeared as a child
top_level_nodes = []
for tid, node in nodes.items():
    if tid not in children_found:
        top_level_nodes.append(node)

# Optional: sort children by their termid or term if you like
def sort_tree(node):
    node["children"].sort(key=lambda x: x["termid"])
    for c in node["children"]:
        sort_tree(c)

for top in top_level_nodes:
    sort_tree(top)

# ------------------------------------------------------------------------
# Print the resulting structure as a JSON array
# ------------------------------------------------------------------------
hierarchy_json = (json.dumps(top_level_nodes, ensure_ascii=False, indent=2))

with open("../../../../Users/.../Desktop/hierarchy_output.txt", "w", encoding="utf-8") as outfile:
    outfile.write(hierarchy_json)
