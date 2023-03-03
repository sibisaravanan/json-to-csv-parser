import json
import csv 
csv_filename = "file.csv"
def find_values(id, json_repr):
    results = []
    def _decode_dict(a_dict):
        try:
            results.append(a_dict[id])
        except KeyError:
            pass
        return a_dict
    json.loads(json_repr, object_hook=_decode_dict)
    return results

def find_values_if_exists(req, json_string):
    if len(find_values(req, json_string)) > 0:
        return find_values(req, json_string)[0]
    else:
        return '-'
    
def tags_to_dict(tags):
    result_dict = {}
    for tag in tags:
        result_dict[tag['Key']] = tag['Value']
    return result_dict

CSV_HEADERS = ['VolumeId','CreateTime','State','Size','Encrypted','AttachTime','InstanceId','Device','Tags']
with open(csv_filename, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(CSV_HEADERS)
    
    with open('file.json', 'r') as f:
        json_data = json.load(f)
        for volume in json_data["Volumes"]:
            json_string = json.dumps(volume).replace('\n', '').replace(' ', '')
        
            VolumeId = find_values_if_exists('VolumeId', json_string)
            State = find_values_if_exists('State', json_string)
            AttachTime = find_values_if_exists('AttachTime', json_string)
            Device = find_values_if_exists('Device', json_string)
            InstanceId = find_values_if_exists('InstanceId', json_string)
            AttachTime = find_values_if_exists('AttachTime', json_string)
            CreateTime = find_values_if_exists('CreateTime', json_string)
            Encrypted = find_values_if_exists('Encrypted', json_string)
            Size = find_values_if_exists('Size', json_string)
        
            Tags = find_values_if_exists('Tags', json_string)
            final_tags = tags_to_dict(Tags) if Tags != '-' else 'No Tags'
            final_tags = json.dumps(final_tags, indent=7, sort_keys=True)

            writer.writerow([VolumeId,CreateTime,State,Size,Encrypted,AttachTime,InstanceId,Device,Tags])
csvfile.close()
