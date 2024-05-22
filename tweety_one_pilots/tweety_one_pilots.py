import json
import sys

def processInputTweetsJson(list):    
    tags_dict = dict()
    full_length = 0
    if 'tweets' not in list:
        raise KeyError('There is no any tweet in the given json')
    # Store each valid tag into tags_list
    for i in list['tweets']:
        if 'hashtags' not in i:
            continue
        else:
            for j in i['hashtags']:
                full_length = full_length + 1
                if j in tags_dict:
                    tags_dict[j] = tags_dict[j] + 1
                else:
                    tags_dict[j] = 1
            tags_dict['full_length'] = full_length
    return tags_dict


def checkPercentage(percentageJson):
    if 'percentage_threshold' not in percentageJson:
        raise KeyError('There is no percentage in given json')
    try:
        percentageJson['percentage_threshold'] = int(percentageJson['percentage_threshold'])
    except ValueError as error:
        raise ValueError('The value may contain some illegal string characters')
    percentage = percentageJson['percentage_threshold']
    return percentage


def orderData(processedDict, percentage, full_length):

    for x, y in list(processedDict.items()):
        if((y/full_length)*100) < percentage:
            processedDict.pop(x)      
    processedDict.pop("full_length")
    if len(processedDict) == 0:
       return
    # reverse order
    sort_orders = sorted(processedDict.items(), key=lambda x: x[1], reverse=True)
    final_list = []
    for i in sort_orders:
        final_list.append(i[0])
    return final_list

def jsonHandler(jsonFile):
    percentage = 0
    #error_dict = {}
    percentage = checkPercentage(jsonFile)
    if percentage < 0:
        # error_dict['percentage_error'] = "There is no valid percentage into input json file, it cannot be negative"
        return json.dumps([])
    processed_tags = processInputTweetsJson(jsonFile)
    if len(processed_tags) < 2:
        # error_dict['tag_error'] = "There is no valid tag into input json file"
        return json.dumps([])
    ordered_list = orderData(processed_tags, percentage, processed_tags['full_length'])    
    if ordered_list == None or len(ordered_list) < 1 :
        # error_dict['ordered_list_error'] = "There is no tag percentage higher than given percentage"
        return json.dumps([])
    return json.dumps(ordered_list)


def main():
    if len(sys.argv) < 2:
        raise ValueError('Bad request passed to script')
    else:
        if len(sys.argv) > 2:
            raise ValueError('You should only pass one argument')
        dataJson = sys.argv[1]
        with open(dataJson, 'r') as file:
            try:                                                                           
                json_object = json.load(file)                                                          
            except ValueError as error:                
                raise  ValueError('Incorrect Format', 'json')
            response = jsonHandler(json_object)
        print(response)
    

if __name__ == '__main__':
    main()