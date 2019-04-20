
def check_config_result(qian_data,hou_data):
    for key in qian_data.keys():
        assert qian_data[key] == hou_data[key]

