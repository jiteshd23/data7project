import pandas as pd


# table1 and table2 are matched on col1_key/col2_key
# col1 is then replaced with column col2_replace with optional new col_alias
# tables are in pandas form


def replace_col_with_id(table1, table2, col1_key, col2_key, col2_replace, new_col_alias=''):
    # replace col2 with col1 name for merging if they're not the same
    if col1_key != col2_key:
        table2[col1_key] = table2[col2_key]
        table2 = table2.drop(col2_key, axis=1)

    if new_col_alias == '':
        new_col_alias = col2_replace

    df = pd.merge(table1, table2, how='left', on=col1_key)

    # finds the index of the column to be replaced, and replace it with the new column:
    col1_key_loc_int = list(df.columns).index(col1_key)
    output_df_cols_list = list(table1.columns)
    output_df_cols_list[col1_key_loc_int] = col2_replace
    df = df[output_df_cols_list]

    # renames made column with new col_alias
    df.rename(columns={col2_replace: new_col_alias}, inplace=True)

    return df


def un_id(table1, table2, col1_key, col2_key, col1_replace, col2_replace, new_col_alias=''):
    # replace col2 with col1 name for merging if they're not the same
    if col1_key != col2_key:
        table2[col1_key] = table2[col2_key]
        table2 = table2.drop(col2_key, axis=1)

    if new_col_alias == '':
        new_col_alias = col2_replace

    df = pd.merge(table1, table2, how='left', on=col1_key)

    # finds the index of the column to be replaced, and replace it with the new column:
    col1_replace_loc_int = list(df.columns).index(col1_replace)
    output_df_cols_list = list(table1.columns)
    output_df_cols_list[col1_replace_loc_int] = col2_replace
    df = df[output_df_cols_list]

    df = df.drop(col1_replace)

    # renames made column with new col_alias
    df.rename(columns={col2_replace: new_col_alias}, inplace=True)

    return df
