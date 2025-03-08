import sqlite3


# Task 1: Roster Database
def manage_roster():
    conn = sqlite3.connect("roster.db")
    cursor = conn.cursor()

    # Create table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Roster (
            Name TEXT,
            Species TEXT,
            Age INTEGER
        )
    """)

    # Insert data
    cursor.executemany("""
        INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)
    """, [
        ("Benjamin Sisko", "Human", 40),
        ("Jadzia Dax", "Trill", 300),
        ("Kira Nerys", "Bajoran", 29)
    ])

    # Update Data
    cursor.execute("UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'")

    # Query Data
    cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
    print(cursor.fetchall())

    # Delete Data
    cursor.execute("DELETE FROM Roster WHERE Age > 100")

    # Bonus Task: Add new column
    cursor.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT")

    # Update Rank Data
    cursor.executemany("""
        UPDATE Roster SET Rank = ? WHERE Name = ?
    """, [
        ("Captain", "Benjamin Sisko"),
        ("Lieutenant", "Ezri Dax"),
        ("Major", "Kira Nerys")
    ])

    # Advanced Query
    cursor.execute("SELECT * FROM Roster ORDER BY Age DESC")
    print(cursor.fetchall())

    conn.commit()
    conn.close()


# Task 2: Library Database
def manage_library():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    # Create table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Books (
            Title TEXT,
            Author TEXT,
            Year_Published INTEGER,
            Genre TEXT
        )
    """)

    # Insert data
    cursor.executemany("""
        INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)
    """, [
        ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
        ("1984", "George Orwell", 1949, "Dystopian"),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
    ])

    # Update Data
    cursor.execute("UPDATE Books SET Year_Published = 1950 WHERE Title = '1984'")

    # Query Data
    cursor.execute("SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'")
    print(cursor.fetchall())

    # Delete Data
    cursor.execute("DELETE FROM Books WHERE Year_Published < 1950")

    # Bonus Task: Add new column
    cursor.execute("ALTER TABLE Books ADD COLUMN Rating REAL")

    # Update Rating Data
    cursor.executemany("""
        UPDATE Books SET Rating = ? WHERE Title = ?
    """, [
        (4.8, "To Kill a Mockingbird"),
        (4.7, "1984"),
        (4.5, "The Great Gatsby")
    ])

    # Advanced Query
    cursor.execute("SELECT * FROM Books ORDER BY Year_Published ASC")
    print(cursor.fetchall())

    conn.commit()
    conn.close()


# Run both tasks
manage_roster()
manage_library()
