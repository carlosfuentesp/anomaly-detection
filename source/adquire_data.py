import pandas as pd
from tensorflow.keras.utils import get_file


def read_data():
    try:
        print('Downloading Data...')
        path = get_file('kddcup.data_10_percent.gz',
                        origin='http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data_10_percent.gz')
    except:
        print('Error downloading')
        raise
    temp_df = pd.read_csv(path, header=None)

    temp_df.dropna(inplace=True, axis=1)

    temp_df.columns = [
        'duration',
        'protocol_type',
        'service',
        'flag',
        'src_bytes',
        'dst_bytes',
        'land',
        'wrong_fragment',
        'urgent',
        'hot',
        'num_failed_logins',
        'logged_in',
        'num_compromised',
        'root_shell',
        'su_attempted',
        'num_root',
        'num_file_creations',
        'num_shells',
        'num_access_files',
        'num_outbound_cmds',
        'is_host_login',
        'is_guest_login',
        'count',
        'srv_count',
        'serror_rate',
        'srv_serror_rate',
        'rerror_rate',
        'srv_rerror_rate',
        'same_srv_rate',
        'diff_srv_rate',
        'srv_diff_host_rate',
        'dst_host_count',
        'dst_host_srv_count',
        'dst_host_same_srv_rate',
        'dst_host_diff_srv_rate',
        'dst_host_same_src_port_rate',
        'dst_host_srv_diff_host_rate',
        'dst_host_serror_rate',
        'dst_host_srv_serror_rate',
        'dst_host_rerror_rate',
        'dst_host_srv_rerror_rate',
        'outcome'
    ]

    return temp_df
