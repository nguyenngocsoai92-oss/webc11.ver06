# V7 — Kết quả rà soát và điều kiện đưa vào sử dụng

**Trạng thái: đang phát triển, chưa nghiệm thu go-live.** Ngày 24/09/2026.

## Quyết định đã ghi nhận

- Tên miền: vbnachapter11.com; email gửi: bnachapter11@gmail.com.
- Chưa có hosting. Chưa có địa chỉ nhận thư kiểm thử và xác thực Gmail.
- “3 nhà hàng lập” được anh xác nhận là **3 nhà sáng lập**.
- Giữ nguyên nội dung tổng quan VBNA; không viết lại hoặc tóm tắt.
- Kỳ doanh thu gắn buổi họp chính, không bị buổi đào tạo/Power Team/sự kiện làm thay đổi. Mốc 17:00 được giữ theo nội dung workbook và cho phép cấu hình; anh chưa xác nhận riêng mốc này trong câu trả lời vừa rồi.

## Đối chiếu triển khai

| Nội dung | Trạng thái V7 | Việc còn lại |
|---|---|---|
| Trang chủ đỏ đồng bộ, đăng nhập/khách cạnh nhau | Đã chỉnh bản thử | Kiểm tra với logo, banner, ảnh và nội dung thật |
| Tổng quan VBNA nguyên văn | Đã dùng lại nguồn 7 phần | Nghiệm thu đối chiếu bản gốc từng câu trước xuất bản |
| Ba nhà sáng lập, chân trang liên hệ Ban Khách mời | Đã dựng bố cục | Bổ sung 3 ảnh/tên/chức danh; phân công Trưởng ban; địa chỉ văn phòng |
| Nhiệm kỳ 8, 9+ chỉ công bố khi bổ nhiệm | Chưa hoàn tất | Lưu nhiệm kỳ và quy trình công bố trên máy chủ |
| Hai logo, tự xóa nền trắng, kích thước; nhiều banner có liên kết | Mới có hiển thị hai logo và vị trí ảnh | Chưa hoàn thiện tự tách nền, trình quản lý banner và kiểm thử ảnh thật |
| Hồ sơ năng lực công khai / cập nhật riêng tư | Kế thừa giao diện thử V6 | Lưu máy chủ, duyệt công khai, lịch sử, tối đa 20 ảnh doanh nghiệp |
| Album tối đa 500 ảnh | Chưa hoàn tất | Lưu trữ ảnh, nén và phân trang; không lưu 500 ảnh trong bộ nhớ trình duyệt |
| Trưởng ban Hội viên/PCT/MC phê duyệt và khóa tài khoản | Mới có quyền nền tảng | Hoàn thiện quy trình, khóa phiên đăng nhập và kiểm thử từng vai trò |
| Quyền tích từng chức năng | Đã có màn hình và kiểm tra tại máy chủ mới | Nối toàn bộ chức năng cũ vào cơ chế này |
| Thông báo Ban, lịch, sinh nhật phát sinh, tệp | Đã có nghiệp vụ máy chủ và cổng nhận | Hoàn thiện giao diện theo bộ nhận diện, popup, tệp email và lịch nâng cao |
| Email Gmail thực | Đã có hàng đợi và kết nối SMTP | Cấu hình bí mật, người nhận kiểm thử, gửi thật và xác nhận nhận thư |
| Sinh nhật tự động, AI theo tuổi | Đã có logic và lệnh xử lý | Cấu hình AI; duyệt chất lượng lời chúc; cài lịch chạy trên hosting |
| Báo cáo đúng kỳ và đúng cột | Đã sửa một số lỗi trọng yếu; kiểm thử quy tắc | Chưa nghiệm thu toàn bộ workbook V7, kiểu ngày Excel, phân quyền và các tình huống tài chính |
| Lucky Draw Ban sự kiện, thêm khách ngoài, N giải liên tiếp | Kế thừa prototype | Chưa chuyển máy chủ/kiểm thử yêu cầu mới |
| Bản đồ Hải Phòng, địa chỉ cũ/mới | Mới có menu và trường dữ liệu | Dịch vụ bản đồ, xác định vị trí, cơ chế cho phép công khai vị trí nhà ở |
| Đồng bộ desktop/mobile | Có kiểm tra kích thước trang thử | Chưa có kiểm thử nhiều tài khoản, nhiều thiết bị với dữ liệu máy chủ |

## Kiểm thử và giới hạn

Đã chạy kiểm tra bản V6 trước khi sửa, lưu bằng chứng riêng. Vòng cuối V7 đạt **25 kiểm thử máy chủ** và **28 lượt trang/kích thước** (7 trang × 4 chiều rộng: 1440/768/390/360). Kiểm thử quy tắc doanh thu tại biên thời gian, phân loại buổi họp, điểm danh trùng và công nợ đều đạt.

Đã tải file Excel thật từ giao diện V7 và mở lại bằng bộ đọc độc lập: **14 sheet, 384 ô** được đối chiếu với dữ liệu báo cáo, tất cả khớp. Bộ dữ liệu thử cho doanh thu trong kỳ 333, cộng dồn 1.333, hiện diện 2/3; ô R3 của tổng hợp tuần là số 0,666666… có định dạng `0.00%`. Khoản chờ duyệt bị loại khỏi công nợ chính thức. Buổi họp ngoài kỳ bị chặn. Đây là dữ liệu kiểm thử, không phải số liệu kinh doanh thật.

Đây là các kiểm thử có phạm vi. Chưa phải kiểm thử tất cả 158 yêu cầu hoặc bằng chứng hệ thống không còn lỗi. SMTP và AI trong kiểm thử được mô phỏng; chưa có thư gửi thật. Kiểm thử cơ sở dữ liệu hiện dùng SQLite; cần chạy lại trên PostgreSQL trước triển khai.

## Rà soát thẩm mỹ

Trang chủ đã rõ thứ tự: nhận diện → thông điệp → buổi họp/thao tác → tổng quan nguyên văn → nhà sáng lập → hội viên → hoạt động → quy trình → lời mời → chân trang. Tuy nhiên ảnh sáng lập và một số thông tin còn trống, phần tổng quan dài khiến trang chưa cân đối hoàn toàn. Không coi ảnh xem trước hiện tại là giao diện VIP đã nghiệm thu. Cần dữ liệu thật và thêm một vòng bố cục desktop/mobile, menu có hai logo, kiểm tra từng đường dẫn và trạng thái không có lịch họp.

## Điều kiện nghiệm thu bắt buộc

1. Hoàn thành phần nghiệp vụ còn thiếu ở bảng trên; toàn bộ dữ liệu vận hành nằm trên máy chủ và quyền được kiểm tra ở máy chủ.
2. Nhập nội dung/ảnh chính thức, loại dữ liệu mẫu, đối chiếu tổng quan nguyên văn; kiểm tra trang public không lộ dữ liệu nội bộ.
3. Chạy báo cáo với bộ giao dịch có kết quả biết trước, đối chiếu từng cột, tổng và kỳ; xuất Excel rồi mở lại để xác minh kiểu dữ liệu.
4. Kiểm thử trên PostgreSQL, hai tài khoản/thiết bị, khôi phục sao lưu, tải tệp, thiết bị nhỏ, link/menu và lỗi mạng.
5. Có hosting, HTTPS, DNS, cơ sở dữ liệu, kho tệp riêng, sao lưu và tiến trình gửi thư định kỳ.
6. Kết nối Gmail/AI bằng cấu hình bí mật; gửi email thử đến địa chỉ được anh chỉ định, xác nhận nhận được và nội dung đúng; sau đó mới bật sinh nhật tự động.

Quy tắc sinh nhật tạm áp dụng: không có năm sinh thì dùng lời chúc trung tính; 29/02 vào năm không nhuận chúc ngày 28/02; chỉ gửi người đang hoạt động và đã bật nhận lời chúc. Các quy tắc này phải được ghi nhận khi nghiệm thu. Trạng thái “Gmail đã tiếp nhận” không đồng nghĩa thư đã nằm trong hộp thư đến.
