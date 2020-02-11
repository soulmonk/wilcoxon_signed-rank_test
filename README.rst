`Wilcoxon signed rank test <https://en.wikipedia.org/wiki/Wilcoxon_signed-rank_test>`_
--------------------------------------------------------------------------------------

Requirements:
-------------

- python3
- make

Install
-------

`make init`

Run
---

Note: xlsx file should contain spreadsheet called "Data"

``OPTIONS="--data_path=\"PATH_TO_XLSX_FILE\" --out_path=\"PATH_TO_OUTPUT_CSV_FILE\" --key_product_idx=INDEX_OF_KEY_PRODUCT" make run``