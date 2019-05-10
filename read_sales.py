# This program reads all of the values in
# the sales.txt file.

def main():


    sales_file = open('sales.txt', 'r')


    try:


        # Open the sales.txt file for reading.


        # Read the first line from the file, but
        # don't convert to a number yet. We still
        # need to test for an empty string.
        line = sales_file.readline()

        total_sales = 0

        # As long as an empty string is not returned
        # from readline, continue processing.
        while line != '':
            # Convert line to a float.
            amount = float(line)

            total_sales += amount

            # Format and display the amount.
            print(format(amount, '.2f'))

            # Read the next line.
            line = sales_file.readline()



        print("total sales was", total_sales)
    except ValueError:
        print('invalid data in file')
    finally:
        # Close the file.
        print('closing file connection')
        sales_file.close()



# Call the main function.
main()
