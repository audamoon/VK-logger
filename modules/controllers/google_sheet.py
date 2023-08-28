from modules.external.google_sheet import GoogleSheetManager
from datetime import datetime

class GoogleSheetController:
    def __init__(self):
        self.manager = GoogleSheetManager()

    def start_service(self,path_to_creds,sheet_id):
        self.manager.start_service(path_to_creds, sheet_id)

    def get_names_to_bypass(self):
        row_ids = self.manager.reader.find_row_id_by_word("E:E", "TRUE")
        all_names = self.manager.reader.read_range("A:A")
        bypass_names = []
        for row_id in row_ids:
            bypass_names.append(all_names[row_id-1][0])
        return bypass_names

    def get_names_to_login(self):
        row_ids = self.manager.reader.find_row_id_by_word("F:F", "TRUE")
        all_names = self.manager.reader.read_range("A:A")
        login_names = []
        for row_id in row_ids:
            login_names.append(all_names[row_id-1][0])
        return login_names
    
    def get_all_login_data(self, choosed_names:list):
        all_names = self.manager.reader.read_range("A2:A")
        all_login = self.manager.reader.read_range("C2:C")
        all_password = self.manager.reader.read_range("D2:D")
        all_together = []
        
        for i in range(len(all_names)):
            all_together.append([all_names[i][0],all_login[i][0],all_password[i][0]])

        choosed_together = []
        for i in range(len(all_together)):
            for name in choosed_names:
                if name == all_together[i-1][0]:
                    choosed_together.append(all_together[i-1])
                    choosed_names.remove(name)
        
        return choosed_together
    
    def write_word_by_name(self, account_name:str, word:str, range_letter: str):
        cell_id = self.manager.reader.find_row_id_by_word('A:A', account_name)
        self.manager.writer.write_cell(f"{range_letter}{cell_id[0]}", word)
        
    def mark_success_bypass(self,account_name:str):
        self.write_word_by_name(account_name, str(datetime.now().date()), "B")