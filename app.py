# -*- coding: utf-8 -*-
"""
نيو دنت - نظام المحاسبة
برنامج سطح المكتب
"""
import os
import sys

def main():
    try:
        import webview
    except ImportError:
        print("جاري تثبيت المكتبة المطلوبة...")
        os.system(f"{sys.executable} -m pip install pywebview -q")
        import webview

    base = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.join(base, "index.html")

    if not os.path.exists(html_path):
        print("خطأ: ملف index.html غير موجود")
        input("اضغط Enter للخروج...")
        return

    window = webview.create_window(
        title="نيو دنت - نظام المحاسبة",
        url=html_path,
        width=1100,
        height=750,
        min_size=(400, 600),
        background_color="#0d7377",
    )
    webview.start()

if __name__ == "__main__":
    main()
