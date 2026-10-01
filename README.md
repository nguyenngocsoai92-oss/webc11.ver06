# VBNA Chapter 11 — Website V7

Cập nhật 01/10/2026. Giao diện desktop/mobile và các luồng thử nghiệm đã được kiểm tra lại. **Chưa go-live:** ứng dụng HTML vẫn lưu dữ liệu nghiệp vụ trong trình duyệt; chưa kết nối toàn bộ với máy chủ dùng chung.

- [Kết quả kiểm thử trước go-live](docs/KIEM_THU_TRUOC_GOLIVE_2026-10-01.md): 17 nhóm kiểm thử giao diện/nghiệp vụ và 28 bài kiểm thử máy chủ đạt; ghi rõ giới hạn nghiệm thu.
- [Thiết kế database V7](docs/DATABASE_V7.md): cấu trúc dự kiến, ánh xạ dữ liệu, quyền và thứ tự triển khai. Đã bổ sung model và migration, kiểm thử database riêng; chưa kết nối toàn bộ giao diện. Xem [bàn giao database](docs/DATABASE_IMPLEMENTATION_V7.md).
- [Máy chủ hiện có](server/README.md): Django cho tài khoản, thông báo, quyền, tệp riêng và email; chưa thay toàn bộ HTML.

Nguồn yêu cầu: Excel VBNA_C11_V6_Ra_soat_va_Chot_Final.xlsx và các điều chỉnh của anh trong cuộc trò chuyện. Giữ nguyên câu từ tổng quan VBNA. Nguồn đồng bộ trong `sources/` là tài liệu chỉ đọc.

Không đưa nguyên thư mục này lên hosting như website đã hoàn chỉnh. Không dùng seed demo, mật khẩu thử hay hàng đợi email thử làm dữ liệu production. Tệp `database_schema.sql` thuộc V5, chỉ để đối chiếu lịch sử; không chạy trên database V7.

Gói bàn giao là mã nguồn đang hoàn thiện, loại cơ sở dữ liệu cục bộ và thông tin bí mật. Tài liệu lịch sử [230 điều chỉnh](V7_230_dieu_chinh.md) và [bàn giao ban đầu](V7_Ra_soat_va_dieu_kien_golive.md) không thay thế kết quả rà soát mới.
