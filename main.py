import pandas as pd
import numpy as np
import logging
import sys


logger = None
def set_log():
    try:
        global logger
        if logger is not None:
            return logger

        logger = logging.getLogger("ロガーさん")
        logger.setLevel(logging.DEBUG)

        if not logger.handlers:
            file_handler = logging.FileHandler("sales_analysis.log", encoding="utf-8")
            file_handler.setLevel(logging.WARNING)
            file_formatter = logging.Formatter("%(levelname)-9s  %(asctime)s [%(filename)s:%(lineno)d] %(message)s")
            file_handler.setFormatter(file_formatter)

            consore_handler = logging.StreamHandler(sys.stdout)
            consore_handler.setLevel(logging.DEBUG)
            consore_handler.setFormatter( logging.Formatter("%(levelname)-9s  %(asctime)s [%(filename)s:%(lineno)d] %(message)s"))

            logger.addHandler(file_handler)
            logger.addHandler(consore_handler)

            return logger

    except TypeError:
        logger.error("ログ作成に失敗しました")
        raise
    except FileNotFoundError:
        logger.error("ログ記録用のファイルが見つかりません")
        raise


def load():
    try:
        logger = set_log()
        df = pd.read_csv("input.csv")
        return df
    except FileNotFoundError:
        logger.error("fairuが見つかりません")
        raise


def crean_data(df):
    try:
        new_df = df.copy()
        logger.debug(f"読み込み直後のデータ形状: {new_df.shape}")
        logger.debug(f"欠損値の数: {new_df.isna().sum()}")

        none_count = (new_df["価格"] <= 0).sum()
        new_df["価格"] = new_df["価格"].mask(df["価格"] <= 0)
        logger.info(f"価格が0円以下の商品を{none_count}件を欠損値として扱います")

        zero_stock_count = new_df["在庫数"].isnull().sum()
        new_df["在庫数"] = new_df["在庫数"].mask(df["在庫数"].isna(), 0 )
        logger.info(f"在庫が空欄の商品{zero_stock_count}件を、在庫０に変更しました")

        stock_count = (new_df["在庫数"] < 0).sum()
        new_df["在庫数"] = new_df["在庫数"].mask(df["在庫数"] < 0)
        logger.info(f"在庫がマイナス表記の商品{stock_count}件を欠損値として扱います")

        logger.info("欠損値除去前のデータ:")
        logger.info(new_df[new_df.isna().any(axis=1)])
        new_df = new_df.dropna()
        count_df = len(df) - len(new_df)
        logger.info(f"欠損値がある行を{count_df}件除去しました")

        new_df["商品名"] = new_df["商品名"].str.strip()
        logger.info("商品名の前後の空白を除去しました")

        new_df["カテゴリー"] = new_df["カテゴリー"].str.lower()
        logger.info("カテゴリー列を小文字に変換しました")

        return new_df

    except FileNotFoundError:
        logger.error("ファイル読み込みに失敗しました")
        raise
    except Exception:
        logger.error("データをクリーニング中に何らかのエラーが発生しました")
        raise

import unittest
class Testcode(unittest.TestCase):
    def test_remove(self):
        test_data = pd.DataFrame({
            '商品ID': [1, 2, 3, 4],
            '商品名': ['商品A', '商品B', '商品C', '商品D'],
            '価格': [100, 200, 50, 200],
            'カテゴリ': ['a', 'b', 'c', 'd'],
            '在庫数': [-10, 20, 30, 40]
        })

        # テスト実行
        result = crean_data(test_data)
        self.assertEqual(len(result), 1)



if __name__ == '__main__':
    unittest.main()









