from dotenv import load_dotenv
import os

load_dotenv()

map_source = os.getenv("MAP_SOURCE_FOLDER")
map_export = os.getenv("MAP_LIST_EXPORT_FILE")
map_blacklist = os.getenv("MAP_BLACKLIST")
include_workshop = os.getenv("INCLUDE_WORKSHOP")


def auto_generate_map_list():
    map_folder = os.listdir(map_source)
    maps_bsp = list(filter(lambda x: x.endswith(".bsp"), map_folder))
    maps = list(filter(lambda x: x not in map_blacklist, maps_bsp))

    if include_workshop:
        map_workshop_folder = os.listdir((map_source + '/workshop'))
        for workshop in map_workshop_folder:
            workshop_folder = os.listdir((map_source + '/workshop/' + workshop))
            workshop_maps_bsp = list(filter(lambda x: x.endswith(".bsp"), workshop_folder))
            maps.extend(list(filter(lambda x: x not in map_blacklist, workshop_maps_bsp)))

    export_maps = list(map(lambda orig_string: orig_string.split('.', 1)[0], maps))
    export_maps.sort()

    export_map_list(export_maps)


def export_map_list(maps):
    with open(fr'{map_export}', 'w') as fp:
        for map_name in maps:
            fp.write("%s\n" % map_name)


if __name__ == '__main__':
    auto_generate_map_list()
