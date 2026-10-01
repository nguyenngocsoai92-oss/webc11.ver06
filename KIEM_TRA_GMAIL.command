#!/bin/zsh
umask 077
cd -- "${0:A:h}" || exit 1
if [[ -x .venv/bin/python ]]; then
  .venv/bin/python server/connect_gmail.py
else
  print 'Chưa tìm thấy môi trường chạy V7 trên máy này. Báo lại để được thiết lập; không nhập mật khẩu vào chat.'
fi
read '?Nhấn Enter để đóng cửa sổ…'
