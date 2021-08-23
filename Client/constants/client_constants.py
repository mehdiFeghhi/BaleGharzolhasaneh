class BotMessages:
    cat_count = " ({})"
    help = "راهنما"
    line = "\n"
    choose_from_buttons = "لطفا از بین گزینه ها انتخاب کنید:"
    start = "سلام به بات قرض الحسنه خوش آمدید.\nلطفا از بین گزینه ها انتخاب کنید:"
    number_of_day_in_month = "در ماه می‌خواهید چندبار یکبار کمک کنید"
    amount_of_money = "چه میزان می‌خواهید کمک کنید؟ "
    which_day = "روز {day} روز چندم از ماه باشد؟"
    End_pay = "مشخصات آخرین پرداختی شما"

class Keyboards:

    register = "ثبت نام در قرض الحسنه"
    read_me = "درباره قرض الحسنه ما"

    date_last_pay = "مشاهده آخرین پرداختی"
    dates_of_all_time = "مشاهده تمامی پرداختی‌ها از ابتدا تااکنون"
    date_day_must_pay = "مشاهده زمان‌‌های پرداخت قرض الحسنه"
    amount_of_each_time = "مشاهده مقداری که هرماه باید پرداخت شود "
    change_date_of_pay = "تغییر زمان‌های پراختی"
    change_amount_of_pay = "تغییر میزان پرداخت"
    back = "بازگشت"


class ConversationStates:
    CATEGORY, LOCATION, PRODUCT_INFO, PRODUCT, CONFIRM_ORDER, PRODUCT_ADDED_TO_ORDER, PAYMENT, PRODUCT_COUNT = range(8)