import pandas as pd


# Encode a numeric column as zscores
def encode_numeric_zscore(df, name, mean=None, sd=None):
    if mean is None:
        mean = df[name].mean()

    if sd is None:
        sd = df[name].std()

    df[name] = (df[name] - mean) / sd


# Encode text values to dummy variables(i.e. [1,0,0],[0,1,0],[0,0,1] for red,green,blue)
def encode_text_dummy(df, name):
    dummies = pd.get_dummies(df[name])
    for x in dummies.columns:
        dummy_name = f"{name}-{x}"
        df[dummy_name] = dummies[x]
    df.drop(name, axis=1, inplace=True)


def process(df):
    # display 5 rows
    print('Preprocessing data...')
    pd.set_option('display.max_columns', 7)
    pd.set_option('display.max_rows', 5)

    df.groupby('outcome')['outcome'].count()

    encode_numeric_zscore(df, 'duration')
    encode_text_dummy(df, 'protocol_type')
    encode_text_dummy(df, 'service')
    encode_text_dummy(df, 'flag')
    encode_numeric_zscore(df, 'src_bytes')
    encode_numeric_zscore(df, 'dst_bytes')
    encode_text_dummy(df, 'land')
    encode_numeric_zscore(df, 'wrong_fragment')
    encode_numeric_zscore(df, 'urgent')
    encode_numeric_zscore(df, 'hot')
    encode_numeric_zscore(df, 'num_failed_logins')
    encode_text_dummy(df, 'logged_in')
    encode_numeric_zscore(df, 'num_compromised')
    encode_numeric_zscore(df, 'root_shell')
    encode_numeric_zscore(df, 'su_attempted')
    encode_numeric_zscore(df, 'num_root')
    encode_numeric_zscore(df, 'num_file_creations')
    encode_numeric_zscore(df, 'num_shells')
    encode_numeric_zscore(df, 'num_access_files')
    encode_numeric_zscore(df, 'num_outbound_cmds')
    encode_text_dummy(df, 'is_host_login')
    encode_text_dummy(df, 'is_guest_login')
    encode_numeric_zscore(df, 'count')
    encode_numeric_zscore(df, 'srv_count')
    encode_numeric_zscore(df, 'serror_rate')
    encode_numeric_zscore(df, 'srv_serror_rate')
    encode_numeric_zscore(df, 'rerror_rate')
    encode_numeric_zscore(df, 'srv_rerror_rate')
    encode_numeric_zscore(df, 'same_srv_rate')
    encode_numeric_zscore(df, 'diff_srv_rate')
    encode_numeric_zscore(df, 'srv_diff_host_rate')
    encode_numeric_zscore(df, 'dst_host_count')
    encode_numeric_zscore(df, 'dst_host_srv_count')
    encode_numeric_zscore(df, 'dst_host_same_srv_rate')
    encode_numeric_zscore(df, 'dst_host_diff_srv_rate')
    encode_numeric_zscore(df, 'dst_host_same_src_port_rate')
    encode_numeric_zscore(df, 'dst_host_srv_diff_host_rate')
    encode_numeric_zscore(df, 'dst_host_serror_rate')
    encode_numeric_zscore(df, 'dst_host_srv_serror_rate')
    encode_numeric_zscore(df, 'dst_host_rerror_rate')
    encode_numeric_zscore(df, 'dst_host_srv_rerror_rate')

    # display 5 rows

    df.dropna(inplace=True, axis=1)
    normal_mask = df['outcome'] == 'normal.'
    attack_mask = df['outcome'] != 'normal.'

    df.drop('outcome', axis=1, inplace=True)

    df_normal = df[normal_mask]
    df_attack = df[attack_mask]

    print(f"Normal count: {len(df_normal)}")
    print(f"Attack count: {len(df_attack)}")

    # This is the numeric feature vector, as it goes to the neural net
    x_normal = df_normal.values
    x_attack = df_attack.values

    return x_normal, x_attack
