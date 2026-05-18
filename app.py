# SANDHU JI
from flask import Flask, render_template, request
import random
import time
import re

app = Flask(__name__)

# =========================
# LOGIN DATA
# =========================

login_otp = ""
login_time = 0

saved_login_user = ""
saved_login_password = ""

# =========================
# REGISTER DATA
# =========================

register_otp = ""
register_time = 0

saved_register_user = ""
saved_register_email = ""
saved_register_password = ""

# SANDHU JI
@app.route("/", methods=["GET", "POST"])
def home():

    global login_otp
    global login_time

    global register_otp
    global register_time

    global saved_login_user
    global saved_login_password

    global saved_register_user
    global saved_register_email
    global saved_register_password

    message = ""

    active_form = ""

    # =========================
    # FORM SUBMIT
    # =========================

    if request.method == "POST":
# SANDHU JI
        # ====================================
        # LOGIN SEND OTP
        # ====================================

        if "send_login_otp" in request.form:

            active_form = "login"

            saved_login_user = request.form["login_user"]
            saved_login_password = request.form["login_password"]

            login_otp = str(random.randint(100000, 999999))

            login_time = time.time()

            print("\n========== LOGIN OTP ==========")
            print("USERNAME :", saved_login_user)
            print("PASSWORD :", saved_login_password)
            print("OTP :", login_otp)
            print("================================")

            message = "Login OTP Sent ✅"

        # ====================================
        # LOGIN VERIFY OTP
        # ====================================

        elif "verify_login_otp" in request.form:

            active_form = "login"

            user_otp = request.form["login_otp"]

            current_time = time.time()

            # OTP EXPIRED
# SANDHU JI
            if current_time - login_time > 59:

                message = "Login OTP Expired ❌"

            # INVALID OTP

            elif user_otp != login_otp:

                message = "Invalid Login OTP ❌"

            # SUCCESS

            else:

                message = "Login Successful ✅"

                saved_login_user = ""
                saved_login_password = ""

                login_otp = ""

        # ====================================
        # REGISTER SEND OTP
        # ====================================

        elif "send_register_otp" in request.form:

            active_form = "register"

            saved_register_user = request.form["register_user"]

            saved_register_email = request.form["register_email"]

            saved_register_password = request.form["register_password"]

            # PASSWORD VALIDATION

            password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$"

            if not re.match(
                password_pattern,
                saved_register_password
            ):

                message = "Weak Password ❌"

                return render_template(
                    "index.html",
                    message=message,
                    active_form=active_form,

# SANDHU JI
                    saved_login_user=saved_login_user,
                    saved_login_password=saved_login_password,

                    saved_register_user=saved_register_user,
                    saved_register_email=saved_register_email,
                    saved_register_password=saved_register_password
                )

            register_otp = str(random.randint(100000, 999999))

            register_time = time.time()

            print("\n======= REGISTER OTP ========")
            print("USERNAME :", saved_register_user)
            print("EMAIL :", saved_register_email)
            print("PASSWORD :", saved_register_password)
            print("OTP :", register_otp)
            print("================================")

            message = "Register OTP Sent ✅"

        # ====================================
        # REGISTER VERIFY OTP
        # ====================================

        elif "verify_register_otp" in request.form:

            active_form = "register"

            user_otp = request.form["register_otp"]

            current_time = time.time()

            # OTP EXPIRED

            if current_time - register_time > 59:

                message = "Register OTP Expired ❌"

            # INVALID OTP

            elif user_otp != register_otp:

                message = "Invalid Register OTP ❌"

            # SUCCESS

            else:

                message = "Registration Successful ✅"

                saved_register_user = ""
                saved_register_email = ""
                saved_register_password = ""

                register_otp = ""

    return render_template(

        "index.html",

        message=message,

        active_form=active_form,

        saved_login_user=saved_login_user,
        saved_login_password=saved_login_password,

        saved_register_user=saved_register_user,
        saved_register_email=saved_register_email,
        saved_register_password=saved_register_password
    )

# SANDHU JI

if __name__ == "__main__":
    app.run(debug=True)

    register_message = ""
login_message = ""