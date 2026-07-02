"""
Phần 1: Phân tích & Đề xuất đa giải pháp
1. Phân tích Input/Output

Input
    order_id (Path Parameter): ID đơn hàng cần tra cứu.

Output
    Thành công (200 OK): Trả về thông tin thanh toán của đơn hàng.
    Thất bại:
    404 Not Found: Không tìm thấy đơn hàng.
    500 Internal Server Error: Có lỗi hệ thống, trả về thông báo thân thiện.

        
2. Đề xuất giải pháp

Giải pháp 1: Dùng List
    Lưu dữ liệu trong orders_list.
    Duyệt từng phần tử để tìm order_id.

Giải pháp 2: Dùng Dict
| Tiêu chí         | Duyệt List  | Dùng Dict    |
| ---------------- | ----------- | ------------ |
| Tốc độ tìm kiếm  | Chậm (O(n)) | Nhanh (O(1)) |
| Bộ nhớ           | Ít hơn      | Nhiều hơn    |
| Độ dễ hiểu       | Dễ          | Dễ           |
| Khả năng bảo trì | Trung bình  | Tốt          |
| Bối cảnh phù hợp | Dữ liệu nhỏ | Dữ liệu lớn  |


Kết luận: Chọn Dict vì tra cứu nhanh, phù hợp hệ thống có nhiều đơn hàng.
"""

from fastapi import FastAPI, HTTPException, status, Request
from fastapi.responses import JSONResponse

app = FastAPI()

orders_dict = {
    1: {"code": "SP001", "payment_status": "PAID", "method": "BANK_TRANSFER"},
    2: {"code": "SP002", "payment_status": "UNPAID", "method": "NONE"}
}

@app.exception_handler(Exception)
async def handle_exception(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Đã xảy ra lỗi hệ thống, vui lòng thử lại sau."
        }
    )

@app.get("/orders/{order_id}/payment", status_code=status.HTTP_200_OK)
def get_payment(order_id: int):

    order = orders_dict.get(order_id)

    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Không tìm thấy đơn hàng"
        )

    return order
