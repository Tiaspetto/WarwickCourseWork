"""This module should filter and sort uk phone numbers from the text file provided. """
import re
import sys


class PhoneNumberProcessor:

    def __init__(self):
        self.phone_number_list = []

    def __phoneNumberMatching(self, szLog):
        """ Matching all fit numbers form single log"""
        szLog = szLog.replace(' ', '')  # filter out all spaces
        phone_pattern = re.compile(r'\+44([0-9]*)')  # test +44 pattern 
        if szLog != None and phone_pattern.search(szLog):
            # return a list with mathed numbers
            return phone_pattern.findall(szLog)
        else:
            return None

    def __phoneNumberFormating(self, szPhoneNumber):
        """Format phone number [XXXXX XXXXX]"""
        szPhoneNumber = "0{} {}".format(szPhoneNumber[0:4],szPhoneNumber[4:])
        return szPhoneNumber

    def __phoneNumberSorting(self):
        """Lexicographically sorting"""
        self.phone_number_list.sort()

    def __phoneNumberUnduplicating(self, lsPhoneNumbers):
        """Unduplicating"""
        return reduce(lambda x, y: x if y in x else x + [y], [[], ] + lsPhoneNumbers)  # use 'reduce' function & lambda filter out duplicated number

    def __phoneNumberReader(self, szFilePath):
        """Reader logs form file"""
        try:
            logs = open(szFilePath, 'r')
        except IOError:
            print 'cannot open file: ', szFilePath  # catch exception if file can't open
        else:
            while True:
                log = logs.readline()
                if log:
                    results = self.__phoneNumberMatching(log)
                    if results:
                        for result in results:
                        	if len(result) == 10:  # Only len == 10 phone number valid
                           	    self.phone_number_list.append(
                                    self.__phoneNumberFormating(result))
                else:
                    break  # break in end

    def Start(self, szFilePath):
        self.__phoneNumberReader(szFilePath)
        self.phone_number_list = self.__phoneNumberUnduplicating(
            self.phone_number_list)
        self.__phoneNumberSorting()
        for number in self.phone_number_list:
            print number

if __name__ == "__main__":
    processor = PhoneNumberProcessor()
    if len(sys.argv) > 1:
        processor.Start(sys.argv[1])
    else:
        file_path = raw_input("Please enter a file path:")
        processor.Start(file_path)
