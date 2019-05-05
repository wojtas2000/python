import os

# c:\katalog\katlog
# /katalog/katalog


print(os.path.join("katalog1", "katalog"))
print(
    os.path.abspath(
        os.path.dirname('example.py')
    )
)
