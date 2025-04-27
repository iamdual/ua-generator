from typing import reveal_type
import src.ua_generator as ua_generator

def test_ua_generator():
    """
    This function is used to test mypy type hints.
    
    To test this function, run the following command:
    ```bash
      mypy tests/test_typing.py
    ```
    """
    agent = ua_generator.generate()
    reveal_type(agent)