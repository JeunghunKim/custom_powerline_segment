from powerline.theme import requires_segment_info


@requires_segment_info
def environment(pl, segment_info, filepath=None):
    try:
        with open('/tmp/{}_{}'.format(segment_info['environ'].get('USER', None), filepath), 'r') as f:
            file = f.read().splitlines()
    except Exception as e:
        return None
    return file[0]
