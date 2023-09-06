from flask import Flask as _Flask, flash
from flask import request, session
from flask import render_template
from flask.json import JSONEncoder as _JSONEncoder, jsonify
import decimal
import service.users_data as user_service
import service.notice_data as notice_data
import service.category_data as category_data
import service.type_data as type_data
import service.case_data as case_data
import service.view_data as view_data
import service.version_data as version_data
from service.data_utils import data_time_change
import time


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        super(_JSONEncoder, self).default(o)


class Flask(_Flask):
    json_encoder = JSONEncoder


import os

base = os.path.dirname(__file__)
file_path = base + '/file/'
app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = os.urandom(24)


# -------------Front-end visualization of big data analytics-related services interfacestart-----------------
# System default path foreground jump
@app.route('/')
def main_page():
    return render_template("main.html")


# -------------Front-end visualization of big data analytics-related service interfaces end-----------------

# -------------Backend Service Interface start-----------------
# log in
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        account = request.form.get('account')
        password = request.form.get('password')
        if not all([account, password]):
            flash('Incomplete parameter')
            return "300"
        res = user_service.get_user(account, password)
        if res and res[0][0] > 0:
            session['is_login'] = True
            session['role'] = res[0][1]
            return "200"
        else:
            return "300"


# Login Page Jump
@app.route('/admin')
def admin():
    if session.get("is_login"):
        if session.get('role') == 0:
            return render_template('index.html')
        else:
            return render_template('index1.html')
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    try:
        session.pop("is_login")
        return render_template('login.html')
    except Exception:
        return render_template('login.html')


# Backend Home Page Jump
@app.route('/html/welcome')
def welcome():
    return render_template('html/welcome.html')


# Backend Registration Jump
@app.route('/html/reg')
def html_reg():
    return render_template('reg.html')


# -----------------User manage module START-----------------

# User manage page
@app.route('/html/user')
def user_manager():
    return render_template('html/user.html')


# Get user data paging
@app.route('/user/list', methods=["POST"])
def user_list():
    get_data = request.form.to_dict()
    page_size = get_data.get('page_size')
    page_no = get_data.get('page_no')
    param = get_data.get('param')
    data, count, page_list, max_page = user_service.get_user_list(int(page_size), int(page_no), param)
    return jsonify({"data": data, "count": count, "page_no": page_no, "page_list": page_list, "max_page": max_page})


# Registered User Data
@app.route('/user/reg', methods=["POST"])
def user_reg():
    get_data = request.form.to_dict()
    name = str(get_data.get('username'))
    account = str(get_data.get('account'))
    password = str(get_data.get('password'))
    company = "Registration"
    phone = " "
    mail = " "
    type = 1
    return user_service.add_user(name, account, password, company, phone, mail, type)


# Adding User Data
@app.route('/user/add', methods=["POST"])
def user_add():
    get_data = request.form.to_dict()
    name = get_data.get('name')
    account = get_data.get('account')
    password = get_data.get('password')
    company = get_data.get('company')
    phone = get_data.get('phone')
    mail = get_data.get('mail')
    type = get_data.get('type')
    return user_service.add_user(name, account, password, company, phone, mail, type)


# Modify user data
@app.route('/user/edit', methods=["PUT"])
def user_edit():
    get_data = request.form.to_dict()
    id = get_data.get('id')
    name = get_data.get('name')
    password = get_data.get('password')
    company = get_data.get('company')
    phone = get_data.get('phone')
    mail = get_data.get('mail')
    type = get_data.get('type')
    user_service.edit_user(id, name, password, company, phone, mail, type)
    return '200'


# Deleting user data
@app.route('/user/delete', methods=["DELETE"])
def user_delete():
    get_data = request.form.to_dict()
    id = get_data.get('id')
    user_service.del_user(id)
    return '200'


# -----------------User manage module END-----------------


# -----------------Notice manage module START-----------------

# Notice manage page
@app.route('/html/notice')
def notice_manager():
    return render_template('html/notice.html')


# Get the latest announcements
@app.route('/notice/new', methods=["POST"])
def notice_new():
    res = notice_data.get_notice()
    return jsonify({"title": res[1], "content": res[2], "user_name": res[3], "create_time": str(res[4])})


# Get the latest announcements
@app.route('/notice/list', methods=["POST"])
def notice_list():
    get_data = request.form.to_dict()
    page_size = get_data.get('page_size')
    page_no = get_data.get('page_no')
    param = get_data.get('param')
    data, count, page_list, max_page = notice_data.get_notice_list(int(page_size), int(page_no), param)
    return jsonify({"data": data, "count": count, "page_no": page_no, "page_list": page_list, "max_page": max_page})


# Add Announcement Data
@app.route('/notice/add', methods=["POST"])
def notice_add():
    get_data = request.form.to_dict()
    title = get_data.get('title')
    content = get_data.get('content')
    user_name = get_data.get('user_name')
    return notice_data.add_notice(title, content, user_name)


# Modification of announcement data
@app.route('/notice/edit', methods=["PUT"])
def notice_edit():
    get_data = request.form.to_dict()
    id = get_data.get('id')
    title = get_data.get('title')
    content = get_data.get('content')
    user_name = get_data.get('user_name')
    notice_data.edit_notice(id, title, content, user_name)
    return '200'


# Deletion of announcement data
@app.route('/notice/delete', methods=["DELETE"])
def notice_delete():
    get_data = request.form.to_dict()
    id = get_data.get('id')
    notice_data.del_notice(id)
    return '200'


# -----------------Notice manage module END-----------------


# -----------------System Version manage module START-----------------

# System Version manage page
@app.route('/html/version')
def version_manager():
    return render_template('html/version.html')


# Get system version
@app.route('/version/show', methods=["POST"])
def version_show():
    res = version_data.get_sys_version()
    return jsonify({"data": res})


# Get system version data paging
@app.route('/version/list', methods=["POST"])
def version_list():
    get_data = request.form.to_dict()
    page_size = get_data.get('page_size')
    page_no = get_data.get('page_no')
    param = get_data.get('param')
    data, count, page_list, max_page = version_data.get_sys_version_list(int(page_size), int(page_no), param)
    return jsonify({"data": data, "count": count, "page_no": page_no, "page_list": page_list, "max_page": max_page})


# Add system version data
@app.route('/version/add', methods=["POST"])
def sys_version_add():
    get_data = request.form.to_dict()
    name = get_data.get('name')
    version = get_data.get('version')
    return version_data.add_sys_version(name, version)


# Modify system version data
@app.route('/version/edit', methods=["PUT"])
def version_edit():
    get_data = request.form.to_dict()
    id = get_data.get('id')
    name = get_data.get('name')
    version = get_data.get('version')
    version_data.edit_sys_version(id, name, version)
    return '200'


# Deleting system version data
@app.route('/version/delete', methods=["DELETE"])
def version_delete():
    get_data = request.form.to_dict()
    id = get_data.get('id')
    version_data.del_sys_version(id)
    return '200'


# -----------------System Version manage module END-----------------

# -----------------Case type management module START-----------------

# Case Type Management Page
@app.route('/html/category')
def category_manager():
    return render_template('html/category.html')


# Obtaining data on the type of case paging
@app.route('/category/list', methods=["POST"])
def category_list():
    get_data = request.form.to_dict()
    page_size = get_data.get('page_size')
    page_no = get_data.get('page_no')
    param = get_data.get('param')
    data, count, page_list, max_page = category_data.get_category_list(int(page_size), int(page_no), param)
    return jsonify({"data": data, "count": count, "page_no": page_no, "page_list": page_list, "max_page": max_page})


# Add data on the type of cases
@app.route('/category/add', methods=["POST"])
def category_add():
    get_data = request.form.to_dict()
    content = get_data.get('content')
    return category_data.add_category(content)


# Modification of data on the type of case
@app.route('/category/edit', methods=["PUT"])
def category_edit():
    get_data = request.form.to_dict()
    id = get_data.get('id')
    content = get_data.get('content')
    category_data.edit_category(id, content)
    return '200'


# Deletion of data on the type of cases
@app.route('/category/delete', methods=["DELETE"])
def category_delete():
    get_data = request.form.to_dict()
    id = get_data.get('id')
    category_data.del_category(id)
    return '200'


# -----------------Type of case management module END-----------------

# -----------------Case category management module START-----------------

# Case category management page
@app.route('/html/type')
def type_manager():
    return render_template('html/type.html')


# Get case category data paging
@app.route('/type/list', methods=["POST"])
def type_list():
    get_data = request.form.to_dict()
    page_size = get_data.get('page_size')
    page_no = get_data.get('page_no')
    param = get_data.get('param')
    data, count, page_list, max_page = type_data.get_type_list(int(page_size), int(page_no), param)
    return jsonify({"data": data, "count": count, "page_no": page_no, "page_list": page_list, "max_page": max_page})


# Data on new case categories
@app.route('/type/add', methods=["POST"])
def type_add():
    get_data = request.form.to_dict()
    content = get_data.get('content')
    return type_data.add_type(content)


# Modification of case category data
@app.route('/type/edit', methods=["PUT"])
def type_edit():
    get_data = request.form.to_dict()
    id = get_data.get('id')
    content = get_data.get('content')
    type_data.edit_type(id, content)
    return '200'


# Deletion of case category data
@app.route('/type/delete', methods=["DELETE"])
def type_delete():
    get_data = request.form.to_dict()
    id = get_data.get('id')
    type_data.del_type(id)
    return '200'


# -----------------Case category management module END-----------------


# -----------------Data management module START-----------------

# Data Management Page
@app.route('/html/case')
def case_manager():
    return render_template('html/case.html')


# Get Cases manage paging
@app.route('/case/list', methods=["POST"])
def case_list():
    get_data = request.form.to_dict()
    page_size = get_data.get('page_size')
    page_no = get_data.get('page_no')
    param = get_data.get('param')
    data, count, page_list, max_page = case_data.get_case_list(int(page_size), int(page_no), param)
    return jsonify({"data": data, "count": count, "page_no": page_no, "page_list": page_list, "max_page": max_page})


# Add Cases manage
@app.route('/case/add', methods=["POST"])
def case_add():
    get_data = request.form.to_dict()
    price = get_data.get('price')
    sex = get_data.get('sex')
    age = get_data.get('age')
    job = get_data.get('job')
    case_type = get_data.get('case_type')
    case_area = get_data.get('case_area')
    content = get_data.get('content')
    rep_time = get_data.get('rep_time')
    is_end = get_data.get('is_end')
    return case_data.add_case(price, sex, age, job, case_type, case_area, content, rep_time, is_end)


# modify Cases manage
@app.route('/case/edit', methods=["PUT"])
def case_edit():
    get_data = request.form.to_dict()
    id = get_data.get('id')
    price = get_data.get('price')
    sex = get_data.get('sex')
    age = get_data.get('age')
    job = get_data.get('job')
    case_type = get_data.get('case_type')
    case_area = get_data.get('case_area')
    content = get_data.get('content')
    rep_time = get_data.get('rep_time')
    is_end = get_data.get('is_end')
    case_data.edit_case(id, price, sex, age, job, case_type, case_area, content, rep_time, is_end)
    return '200'


# delete Cases manage
@app.route('/case/delete', methods=["DELETE"])
def case_delete():
    get_data = request.form.to_dict()
    id = get_data.get('id')
    case_data.del_case(id)
    return '200'


# -----------------Data management module END-----------------
# -----------------Visualization page module START-----------------
# Total Data Acquisition
@app.route('/view/data/total')
def view_data_total():
    return view_data.total_data()


# Type of crime top6
@app.route('/view/data/area/top')
def case_area_top_data():
    return view_data.case_area_top()


# Gender distribution
@app.route('/view/data/sex')
def sex_dist_data():
    return view_data.sex_distribution_data()


# Distribution of completion rates
@app.route('/view/data/end')
def end_dist_data():
    return view_data.end_distribution_data()


# page rotation
@app.route('/view/data/table')
def case_table_data():
    return view_data.get_case_table_data()


# Page category statistics
@app.route('/view/data/type')
def view_type_case_data():
    return view_data.type_case_data()


# Reporting time statistics
@app.route('/view/data/time')
def view_time_case_data():
    return view_data.case_time_data()


# Job Classification
@app.route('/view/data/job')
def view_job_data():
    return view_data.job_data()


# Reported in the last 30 days
@app.route('/view/data/month')
def view_month_case_data():
    return view_data.case_month_data()


# Import of regional data
@app.route('/case/import', methods=['GET', 'POST'])
def details_import():
    file_obj = request.files.get("file")
    try:
        if file_obj is None:
            return "500"
        # Save directly using the file upload object
        after = file_obj.filename.split('.')[1]
        path = os.path.join(file_path, str(int(time.time())) + "." + after)
        file_obj.save(path)
        return case_data.import_xls_data(path)
    except:
        return "500"


# -----------------Visualization page module END-----------------
if __name__ == '__main__':
    # Re-generation of case data time per start-up, in order to ensure that the visualization can display the data properly
    data_time_change()
    # Port Number Setting
    app.run(host="127.0.0.1", port=5000)
