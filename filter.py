


import json
import os
import shutil


class Filter:
    def __init__(self, verbose:bool=False)->None:
        self.verbose = verbose
        self.tracker = 0
        if not os.path.isfile('resources' + os.sep + 'filtered.json'):
            shutil.copy('resources' + os.sep + 'initial.json','resources' + os.sep + 'filtered.json')
            #with open('resources' + os.sep + 'initial.json', encoding='utf-8') as file:
             #   self.initialJSON = json.load(file)
              #  print('New JSON file created')
               # if self.verbose:
                #    print(self.initialJSON)
        #with open('resources'+ os.sep + 'removed.json', 'w', encoding='utf-8') as file:
         #   json.dump({"key": 0}, file, ensure_ascii=False, indent=2)
          #  file.close()
        
        #with open('resources'+ os.sep + 'tracker.json', 'w', encoding='utf-8') as file:
         #   json.dump({"trials": self.tracker}, file, ensure_ascii=False, indent=2)
          #  file.close()

    def apply(self, filter_category:str, filter_value:str)->list:
        with open('resources' + os.sep + 'filtered.json', encoding='utf-8') as file:
            self.initialJSON = json.load(file)
            print('Using existing JSON file')
            if self.verbose:
                print(self.initialJSON)
                
        # Neue gefilterte Daten erzeugen
        filtered = {
            name: info
            for name, info in self.initialJSON.items()
            if info.get(filter_category) == filter_value
        }

        removed = {
            name: info
            for name, info in self.initialJSON.items()
            if info.get(filter_category) != filter_value
        }
        #self.removed_list = [lastname for lastname, info in self.initialJSON.items() if info.get(filter_category) != filter_value ]
        #print(f"List of removed persons: {self.removed_list}")
        try:
            os.remove('resources' + os.sep + 'filtered.json') # Loescht temporaere Filter-Datei
            os.remove('resources' + os.sep + 'removed.json') # Loescht temporaere Filter-Datei
        except:
            pass
        # Gefilterte Daten in eine neue Datei speichern
        with open('resources'+ os.sep + 'filtered.json', 'w', encoding='utf-8') as file:
            json.dump(filtered, file, ensure_ascii=False, indent=2)
        with open('resources'+ os.sep + 'removed.json', 'w', encoding='utf-8') as file:
            json.dump(removed, file, ensure_ascii=False, indent=2)

        if self.verbose:
            print(f"{len(self.initialJSON) - len(filtered)} Entries were removed.")

        self.tracker += 1
        #return self.removed_list
        #with open('resources'+ os.sep + 'tracker.json', 'w', encoding='utf-8') as file:
         #   json.dump({"trials": self.tracker}, file, ensure_ascii=False, indent=2)

    #def trackInput(self)->int:
     #   return self.tracker


def main()->None:
    filter = Filter(verbose=True)
    filter.apply(filter_category='Geschlecht', filter_value='m')

if __name__ == "__main__":
    main()