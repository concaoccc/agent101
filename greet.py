def greet(name: str) -> str:
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"


def main() -> None:
    """Run a simple greeting example when executed directly."""
    user_name = input("Enter your name: ")
    print(greet(user_name))


if __name__ == "__main__":
    main()