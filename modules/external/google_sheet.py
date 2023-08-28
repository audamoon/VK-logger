from google.oauth2 import service_account
from apiclient import discovery


class GoogleSheetLogger:
    SCOPE = ['https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive']

    def get_service(self):
        return self.service

    def start_service(self, path_to_creds, sheet_id):
        self.__set_creds(path_to_creds)
        self.__set_sheet_id(sheet_id)
        self.__service_init()

    def __set_sheet_id(self, sheet_id):
        self.sheet_id = sheet_id

    def __set_creds(self, path_to_creds: str):
        self.creds = service_account.Credentials.from_service_account_file(
            path_to_creds, scopes=self.SCOPE)

    def __service_init(self):
        self.service = discovery.build('sheets', 'v4', credentials=self.creds)


class InLoop:
    pass


class GoogleSheetReader:

    def set_options(self, service, sheet_id):
        self.service = service
        self.sheet_id = sheet_id

    def read_сell(self, range):
        """
        usage example: 

        read_cell("B1", value)

        ===================================

        if you want specify list name just add: "listname!" before range:

        read_cell("Sheet1!B1", value)
        """
        return self.service.spreadsheets().values().get(spreadsheetId=self.sheet_id, range=range).execute()['values'][0][0]

    def read_range(self, range):
        """
        usage example: 

        read_range("B:B")

        ===================================

        if you want specify list name just add: "listname!" before range:

        read_range("Sheet1!B1:B5")
        """
        return self.service.spreadsheets().values().get(spreadsheetId=self.sheet_id, range=range).execute()['values']

    def find_cell_id_by_word(self, sheet_range, word):
        """
        usage example:

        find_cell_id_by_word("E:E", "TRUE")

        ===================================

        if you want specify list name just add: "listname!" before range:

        find_cell_id_by_word("Sheet1!E:E", "TRUE")
        """
        status_from_sheet = self.read_range(sheet_range)
        row_numbers = []
        for i in range(len(status_from_sheet)):
            try:
                if status_from_sheet[i][0] == word:
                    el_n = i + 1
                    row_numbers.append(el_n)
            except:
                pass
        return row_numbers


class GoogleSheetWriter:
    def set_options(self, service, sheet_id):
        self.service = service
        self.sheet_id = sheet_id

    def write_cell(self, range, value: str):
        """
        usage example: 

        write_cell("B1", value)

        ===================================

        if you want specify list name just add: "listname!" before range:

        write_cell("Sheet1!B1", value)
        """
        valueInputOption = 'USER_ENTERED'
        body = {
            'values': [[value]]
        }
        self.service.spreadsheets().values().update(spreadsheetId=self.sheet_id,
                                                    range=range, valueInputOption=valueInputOption, body=body).execute()

    def write_range(self, column_range, value: list):
        """
        usage example: 

        write_range("B:B", list_with_values)

        ===================================

        if you want specify list name just add: "listname!" before range:

        write_range("Sheet1B:B", list_with_values)

        ===================================

        for fill all range with one word use:

        write_range(range, [your_word] * last_row_id)
        """
        if isinstance(value, list) == False:
            raise TypeError("value must be list")

        valueInputOption = 'RAW'
        body = {
            'values': [[value1] for value1 in value]
        }
        return self.service.spreadsheets().values().update(spreadsheetId=self.sheet_id, range=column_range, valueInputOption=valueInputOption, body=body).execute()


class GoogleSheetManager:
    def __init__(self):
        self.logger = GoogleSheetLogger()
        self.reader = GoogleSheetReader()
        self.writer = GoogleSheetWriter()

    def start_service(self, path_to_creds, sheet_id):
        self.logger.start_service(path_to_creds, sheet_id)
        service = self.logger.get_service()
        self.reader.set_options(service, sheet_id)
        self.writer.set_options(service, sheet_id)