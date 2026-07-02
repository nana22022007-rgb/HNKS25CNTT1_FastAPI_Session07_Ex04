from fastapi import FastAPI, HTTPException

app = FastAPI()

orders_dict = {
    1: {"code": "SP001", "payment_status": "PAID", "method": "BANK_TRANSFER"},
    2: {"code": "SP002", "payment_status": "UNPAID", "method": "NONE"}
}

@app.get("/orders/{order_id}/payment")
def get_payment(order_id: int):
    try:
        order = orders_dict.get(order_id)

        if order is None:
            raise HTTPException(
                status_code=404,
                detail="Không tìm thấy đơn hàng"
            )

        return order

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Đã xảy ra lỗi hệ thống, vui lòng thử lại sau."
        )