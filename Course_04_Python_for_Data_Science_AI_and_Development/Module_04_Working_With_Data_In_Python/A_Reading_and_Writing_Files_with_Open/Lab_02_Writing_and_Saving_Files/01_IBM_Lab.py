"""
=========================================================
IBM Data Analyst Professional Certificate (IBM DAPC)

Course 04 : Python for Data Science, AI & Development
Module 04 : Working with Data in Python

Lab 02 : Writing and Saving Files in Python
Exercise : Active and Inactive Members

Author : Varghese
=========================================================
"""

# --------------------------------------------------------
# Import Library
# --------------------------------------------------------

from random import randint as rnd

# --------------------------------------------------------
# File Paths
# --------------------------------------------------------

memReg = "datasets/members.txt"
exReg = "datasets/inactive.txt"

fee = ("yes", "no")

# --------------------------------------------------------
# Generate Sample Files
# --------------------------------------------------------


def genFiles(current, old):
    """
    Creates sample member files.
    """

    with open(current, "w+") as writefile:

        writefile.write("Membership No  Date Joined  Active\n")

        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):

            date = str(rnd(2015, 2020)) + "-" + str(rnd(1, 12)) + "-" + str(rnd(1, 25))

            writefile.write(
                data.format(
                    rnd(10000, 99999),
                    date,
                    fee[rnd(0, 1)],
                )
            )

    with open(old, "w+") as writefile:

        writefile.write("Membership No  Date Joined  Active\n")

        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(3):

            date = str(rnd(2015, 2020)) + "-" + str(rnd(1, 12)) + "-" + str(rnd(1, 25))

            writefile.write(
                data.format(
                    rnd(10000, 99999),
                    date,
                    fee[1],
                )
            )


# Create sample files
genFiles(memReg, exReg)

# --------------------------------------------------------
# Exercise
# --------------------------------------------------------


def cleanFiles(currentMem, exMem):
    """
    Removes inactive members from currentMem
    and appends them to exMem.
    """

    with open(currentMem, "r+") as current:

        with open(exMem, "a+") as old:

            # Read all lines
            members = current.readlines()

            # Move pointer to beginning
            current.seek(0)

            # Rewrite header
            current.write(members[0])

            # Process remaining members
            for member in members[1:]:

                if "no" in member:
                    old.write(member)
                else:
                    current.write(member)

            # Remove remaining old content
            current.truncate()


# --------------------------------------------------------
# Run Exercise
# --------------------------------------------------------

cleanFiles(memReg, exReg)

# --------------------------------------------------------
# Display Active Members
# --------------------------------------------------------

print("=" * 60)
print("ACTIVE MEMBERS")
print("=" * 60)

with open(memReg, "r") as readFile:
    print(readFile.read())

# --------------------------------------------------------
# Display Inactive Members
# --------------------------------------------------------

print("=" * 60)
print("INACTIVE MEMBERS")
print("=" * 60)

with open(exReg, "r") as readFile:
    print(readFile.read())

# --------------------------------------------------------
# IBM Verification Test
# --------------------------------------------------------


def testMsg(passed):

    if passed:
        return "Test Passed"
    else:
        return "Test Failed"


testWrite = "datasets/testWrite.txt"
testAppend = "datasets/testAppend.txt"

passed = True

genFiles(testWrite, testAppend)

with open(testWrite, "r") as file:
    ogWrite = file.readlines()

with open(testAppend, "r") as file:
    ogAppend = file.readlines()

try:
    cleanFiles(testWrite, testAppend)
except Exception as e:
    print(e)

with open(testWrite, "r") as file:
    clWrite = file.readlines()

with open(testAppend, "r") as file:
    clAppend = file.readlines()

# --------------------------------------------------------
# Verify Total Rows
# --------------------------------------------------------

if len(ogWrite) + len(ogAppend) != len(clWrite) + len(clAppend):

    print("The number of rows do not add up.")

    passed = False

# --------------------------------------------------------
# Verify Active File
# --------------------------------------------------------

for line in clWrite:

    if "no" in line:

        print("Inactive members still exist.")

        passed = False

        break

    else:

        if line not in ogWrite:

            print("Data mismatch.")

            passed = False

print("\n" + "=" * 60)
print(testMsg(passed))
print("=" * 60)
