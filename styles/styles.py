styles_table_files = '''
    QTableWidget {
        border-radius: 10px;
        selection-background-color: #FFFFFF;
        alternate-background-color: #FFFFFF;
        background:#cfc6cb;
    }
    QHeaderView::section {
        background-color: #324960;
        color: white;
        padding-left: 4px; /* Align text to the left */
        border: none;
        border-bottom: 1px solid white;
    }
    QHeaderView::section:first {
        border-top-left-radius: 10px;
    }
    QHeaderView::section:last:horizontal {
        border-top-right-radius: 10px;
    }

    QHeaderView::section:last:vertical {
        border-bottom-left-radius: 10px;
    }
'''

styles_btn_disabled = '''
    QPushButton:disabled {
        background-color: #C0C0C0;
        color: white;
    }
'''

styles_btn_enabled = '''
    QPushButton:enabled {
        background-color: #ff6e40;
        color: white;
    }
'''