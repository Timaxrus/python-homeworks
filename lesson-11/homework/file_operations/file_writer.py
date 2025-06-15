def write_file(file_path, content):
    """
    Writes content to a file.
    
    :param file_path: Path to the file where content will be written.
    :param content: Content to be written to the file.
    :return: Success message or error message.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        return "File written successfully."
    except Exception as e:
        return f"An error occurred: {e}"