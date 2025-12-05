# MCP Server for HNPX Document Processing

## Purpose
Enables AI agents to write fiction using the HNPX format through a Breadth-First Search (BFS) expansion workflow.

## Design Philosophy
- **AI-First**: Tools designed for AI agent workflows
- **BFS Guidance**: Built-in navigation guides systematic expansion
- **Native XML**: Direct work with HNPX format
- **Validation**: All operations enforce HNPX specification compliance
- **Atomic Operations**: Each tool performs a single, well-defined operation

## Tool Specifications

### Document Management

#### `create_document(file_path)`
Creates a new empty HNPX document with a root `<book>` element.

**Parameters:**
- `file_path` (string, required): Absolute or relative path where the document will be created

**Returns:** Success confirmation or error if file exists

---

### Navigation & Discovery

#### `get_next_empty_container(file_path)`
Finds the next container node in BFS order that needs children.

**Parameters:**
- `file_path` (string, required): Path to existing HNPX file

**Returns:** Object with `id` and `type` of the empty container, or `null` if document is fully expanded

#### `get_node(file_path, node_id)`
Retrieves XML representation of a specific node (without descendants).

**Parameters:**
- `file_path` (string, required): Path to HNPX file
- `node_id` (string, required): Unique identifier of the node

**Returns:** XML of the node including attributes and `<summary>` child

---

### Node Inspection

#### `get_subtree(file_path, node_id)`
Retrieves XML representation of a node including all its descendants.

**Parameters:**
- `file_path` (string, required): Path to HNPX file
- `node_id` (string, required): Unique identifier of the root node

**Returns:** Complete XML subtree of the node

#### `get_direct_children(file_path, node_id)`
Retrieves immediate child nodes of a specified parent.

**Parameters:**
- `file_path` (string, required): Path to HNPX file
- `node_id` (string, required): Unique identifier of the parent node

**Returns:** XML of all direct child elements

#### `get_node_path(file_path, node_id)`
Returns the complete hierarchical path from document root to specified node.

**Parameters:**
- `file_path` (string, required): Path to HNPX file
- `node_id` (string, required): Unique identifier of the target node

**Returns:** XML containing each ancestor in order from root to target

---

### Node Creation

#### `create_chapter(file_path, parent_id, title, summary, pov=null)`
Creates a new chapter element.

**Parameters:**
- `file_path` (string, required): Path to HNPX file
- `parent_id` (string, required): ID of parent book element
- `title` (string, required): Chapter title
- `summary` (string, required): Chapter summary
- `pov` (string, optional): Point-of-view character identifier

**Returns:** Success confirmation

#### `create_sequence(file_path, parent_id, location, summary, time=null, pov=null)`
Creates a new sequence element.

**Parameters:**
- `file_path` (string, required): Path to HNPX file
- `parent_id` (string, required): ID of parent chapter element
- `location` (string, required): Where the sequence takes place
- `summary` (string, required): Sequence summary
- `time` (string, optional): Time indicator
- `pov` (string, optional): Overrides chapter POV if present

**Returns:** Success confirmation

#### `create_beat(file_path, parent_id, summary)`
Creates a new beat element.

**Parameters:**
- `file_path` (string, required): Path to HNPX file
- `parent_id` (string, required): ID of parent sequence element
- `summary` (string, required): Beat summary

**Returns:** Success confirmation

#### `create_paragraph(file_path, parent_id, summary, text, mode="narration", char=null)`
Creates a new paragraph element.

**Parameters:**
- `file_path` (string, required): Path to HNPX file
- `parent_id` (string, required): ID of parent beat element
- `summary` (string, required): Paragraph summary
- `text` (string, required): Paragraph text content
- `mode` (string, optional): "narration", "dialogue", or "internal"
- `char` (string, optional): Character identifier

**Returns:** Success confirmation

---

### Node Modification

#### `edit_node_attributes(file_path, node_id, attributes)`
Modifies attributes of an existing node.

**Parameters:**
- `file_path` (string, required): Path to HNPX file
- `node_id` (string, required): ID of node to modify
- `attributes` (object, required): Key-value pairs of attributes to update

**Returns:** Success confirmation

#### `remove_node(file_path, node_id)`
Permanently removes a node and all its descendants.

**Parameters:**
- `file_path` (string, required): Path to HNPX file
- `node_id` (string, required): ID of node to remove

**Returns:** Success confirmation

#### `reorder_children(file_path, parent_id, child_ids)`
Reorganizes the order of child elements.

**Parameters:**
- `file_path` (string, required): Path to HNPX file
- `parent_id` (string, required): ID of parent container
- `child_ids` (array, required): List of child IDs in desired order

**Returns:** Success confirmation

---

### Rendering & Export

#### `render_node(file_path, node_id)`
Renders a node and descendants as formatted markdown.

**Parameters:**
- `file_path` (string, required): Path to HNPX file
- `node_id` (string, required): ID of node to render

**Returns:** Formatted markdown text showing hierarchy and content

#### `render_document(file_path)`
Exports entire document to plain text.

**Parameters:**
- `file_path` (string, required): Path to HNPX file

**Returns:** Continuous text of all paragraphs formatted appropriately
