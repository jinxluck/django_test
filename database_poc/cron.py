from .models import testdatabase


def Database_clean_up():
    testdatabase.objects.filter(NODELETE=False).delete()
# forklaring:
# testdatabase.objects = henter de forskellige objekter ud af databasen "testdatabase"
# .filter(NODELETE=False) = tjekker NODELETE feltets værdi
# .delete() = hvid NODELETE er "False" bliver objektet slettet