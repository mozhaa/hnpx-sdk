import fastmcp.exceptions


class HNPXError(fastmcp.exceptions.ToolError):
    """Base exception for HNPX errors"""

    pass


class DuplicateIDError(HNPXError):
    def __init__(self, node_id: str):
        super().__init__(f"Node ID '{node_id}' already exists in the document")


class InvalidParentError(HNPXError):
    def __init__(self, parent_type: str, expected_type: str):
        super().__init__(f"Parent must be a {expected_type}, not {parent_type}")


class NodeNotFoundError(HNPXError):
    def __init__(self, node_id: str):
        super().__init__(f"Node with id '{node_id}' not found")


class InvalidAttributeError(HNPXError):
    def __init__(self, attr: str, value: str, reason: str):
        super().__init__(f"Invalid value '{value}' for attribute '{attr}': {reason}")


class MissingAttributeError(HNPXError):
    def __init__(self, attr: str):
        super().__init__(f"Missing required attribute: '{attr}'")


class InvalidHierarchyError(HNPXError):
    def __init__(self, parent_tag: str, child_tag: str):
        super().__init__(f"Cannot add {child_tag} to {parent_tag} - invalid hierarchy")


class ValidationError(HNPXError):
    def __init__(self, errors: list):
        error_messages = "\n".join([str(e) for e in errors])
        super().__init__(f"Schema validation failed:\n{error_messages}")


class InvalidOperationError(HNPXError):
    def __init__(self, operation: str, reason: str):
        super().__init__(f"Cannot {operation}: {reason}")
