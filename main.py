from persistence.db_setup import initialize_database
from ui import main_menu

if __name__ == "__main__":
    initialize_database()
    main_menu()
