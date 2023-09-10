from powerline.theme import requires_segment_info


@requires_segment_info
def environment(pl, segment_info, filepath=None):
    user_name = segment_info['environ'].get('USER', None)
    try:
        with open('/tmp/{}_{}'.(user_name, filepath), 'r') as f:
            file = f.read().splitlines()
    except Exception as e:
        return None
    return file[0]
