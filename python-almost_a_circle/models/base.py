#!/usr/bin/python3
"""imports"""
import json
import csv
import os.path


class Base:
    """base mange the id"""
    __nb_objects = 0

    def __init__(self, id=None):
        """inits the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """json string"""
        return json.dumps(list_dictionaries or [])

    @staticmethod
    def from_json_string(json_string):
        """list of jsons"""
        return json.loads(json_string or "[]")

    @classmethod
    def create(cls, **dictionary):
        """build the instance"""
        if cls.__name__ is 'Square':
            newcreate = cls(1)
        if cls.__name__ is 'Rectangle':
            newcreate = cls(1, 1)
        if newcreate:
            newcreate.update(**dictionary)
            return newcreate

    @classmethod
    def save_to_file(cls, list_objs):
        """savefile"""
        try:
            jsons = cls.to_json_string([x.to_dictionary() for x in list_objs])
        except:
            jsons = '[]'
        with open(cls.__name__+'.json', 'w', encoding='utf-8') as f:
            f.write(jsons)

    @classmethod
    def load_from_file(cls):
        if not os.path.isfile(cls.__name__ + '.json'):
            return []
        else:
            with open(cls.__name__ + '.json', 'r', encoding='utf-8') as f:
                list_dicts = cls.from_json_string(f.read())
            return [cls.create(**dic) for dic in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        try:
            csvs = [x.to_dictionary() for x in list_objs]
        except AttributeError:
            csvs = '[]'
        if len(csv) == 0:
            return
        keys = csvs[0].keys()
        file_name = cls.__name__ + '.csv'
        with open(file_name, 'w', newline='') as f:
            writer = csv.DictWriter(f, keys)
            writer.writeheader()
            writer.writerows(csvs)

    @classmethod
    def load_from_file_csv(cls):
        file_name = cls.__name__ + '.csv'
        if not os.path.isfile(file_name):
            return []
        objects = []
        with open(file_name, 'r') as f:
            reader = csv.DictReader(f)
            """num to ent"""
            for row in reader:
                for key, val in row.items():
                    try:
                        row[key] = int(val)
                    except:
                        pass
            obj = cls.create(**row)
            objects.append(obj)
        return objects
