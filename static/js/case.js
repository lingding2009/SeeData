page_no = 1;
all_page_param = ' 1=1 ';
layui.use(['form', 'layer', 'laydate'], function () {

    $ = layui.jquery;
    var form = layui.form,
        layer = layui.layer,
        laydate = layui.laydate;
    //执行一个laydate实例
    laydate.render({
        elem: '#rep_time' //指定元素
        , type: 'datetime'
    });


//监听提交
    form.on('submit(edit)', function (data) {
        let id = data.field.id;
        if (id != undefined && id > 0) {
            $.ajax({
                url: "/case/edit",
                data: data.field,
                method: "PUT",
                success: function (obj) {
                    if (obj == "200") {
                        layer.closeAll();
                        layer.msg("modify successfully!", {icon: 6})
                        get_case_data(page_no)
                    } else {
                        layer.msg("fail to modify!", {icon: 5})
                    }
                },
                error: function (xhr, type, errorThrown) {
                }
            });

            return false;
        } else {
            $.ajax({
                url: "/case/add",
                data: data.field,
                method: "POST",
                success: function (obj) {
                    if (obj == "200") {
                        layer.closeAll();
                        layer.msg("successfully added!", {icon: 6})
                        get_user_data(page_no)
                    } else {
                        layer.msg("fail to add!", {icon: 5})
                    }
                },
                error: function (xhr, type, errorThrown) {
                }
            });
        }
    });
    form.on('submit(imp)', function (data) {
        let sendData = new FormData();
        sendData.append('file', $('#file')[0].files[0])
        $.ajax({
            url: "/case/import",
            data: sendData,
            method: "POST",
            contentType: false,
            processData: false,
            success: function (obj) {
                layer.closeAll();
                if (obj == 200) {
                    layer.msg("successe！", {icon: 6})
                } else {
                    layer.msg("fail！", {icon: 5})
                }
                get_case_data(page_no)
            },
            error: function (xhr, type, errorThrown) {
            }
        });
        return false;
    });
// 添加
    window.case_add = function () {
        w = '520px'
        he = '520px'
        $('#id').val("");
        $('#price').val("");
        $('#sex').val("");
        $('#tags').val("");
        $('#age').val("");
        $('#job').val("");
        $('#case_type').val("");
        $('#case_area').val("");
        $('#content').val("");
        $('#rep_time').val("");
        $('#is_end').val("1");
        form.render();
        layer.open({
            type: 1,
            area: [w, he],
            fix: false, //fluid
            maxmin: true,
            shadeClose: true,
            shade: 0.4,
            title: "New",
            content: $('#case-form')
        });

    }
    // 编辑
    window.case_edit = function (title, a, b, c, d, e, f, g, h, j, k) {
        w = '520px'
        he = '520px'
        $('#id').val(a);
        $('#price').val(b);
        $('#sex').val(c);
        $('#age').val(d);
        $('#job').val(e);
        $('#case_type').val(f);
        $('#case_area').val(g);
        $('#content').val(h);
        $('#rep_time').val(j);
        $('#is_end').val(k);
        form.render();
        layer.open({
            type: 1,
            area: [w, he],
            fix: false, //fluid
            maxmin: true,
            shadeClose: true,
            shade: 0.4,
            title: title,
            content: $('#case-form')
        });
    }
});
get_case_data(page_no);
max_page = 0;

function get_case_data(no) {
    page_no = no;
    $.ajax({
        url: "/case/list",
        data: {"page_size": 10, "page_no": page_no, "param": all_page_param},
        method: "POST",
        success: function (obj) {
            page_data = obj.data;
            page_list = obj.page_list;
            max_page = obj.max_page;
            count = obj.count;
            show_data(page_data, page_no, page_list, count, max_page)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}

function show_data(page_data, page_no, page_list, count, page) {
    list_data = '';
    for (var i = 0; i < page_data.length; i++) {
        item = page_data[i];
        list_data = list_data + '<tr>' +
            '<td>' + (i + 1) + '</td>' +
            '<td>' + item[1] + ' £</td>' +
            '<td>' + (item[2] == 'M' ? "male" : "female") + '</td>' +
            '<td>' + item[3] + '</td>' +
            '<td>' + item[4] + '</td>' +
            '<td>' + item[5] + '</td>' +
            '<td>' + item[6] + '</td>' +
            '<td>' + item[8] + '</td>' +
            '<td>' + (item[9] == 1 ? "finished" : "unfinished") + '</td>' +
            '<td class="td-manage">' +
            ' <a title="Edit"  onclick="case_edit(\'Edit\',\'' + item[0] + '\',\'' + item[1] + '\',\'' + item[2] + '\',\'' + item[3] + '\',\'' + item[4] + '\',\'' + item[5] + '\',\'' + item[6] + '\',\'' + item[7] + '\',\'' + item[8] + '\',\'' + item[9] + '\')" href = "javascript:;" > ' +
            '  <i class="layui-icon">&#xe63c;</i>' +
            '  </a>' +
            '        <a title="delete" onclick="member_del(this,\'' + item[0] + '\')" href="javascript:;">' +
            '  <i class="layui-icon">&#xe640;</i>' +
            '              </a>' +
            '            </td>' +
            '          </tr>'
    }
    if (page_no == 1) {
        page_str = ''
    } else {
        page_str = '<span class="prev" onclick="get_case_data(' + (page_no - 1) + ')">&lt;&lt;</span>';
    }
    page_str = '<span>Total ' + page + ' Page，' + count + ' pieces of data</span>' + page_str
    for (var i = 0; i < page_list.length; i++) {
        item = page_list[i];
        if (item == page_no) {
            page_str = page_str + '<span class="current">' + item + '</span>'
        } else {
            page_str = page_str + '<span class="num" onclick="get_case_data(' + item + ')">' + item + '</span>'
        }
    }
    if (page_no != max_page) {
        page_str = page_str + ' <span class="next" onclick="get_case_data(' + (page_no + 1) + ')">&gt;&gt;</span>'
    }
    $("#case_data").html(list_data);
    $("#page_list").html(page_str);

}


/*删除*/
function member_del(obj, id) {
    layer.confirm('Confirm to delete?', function (index) {
        //发异步删除数据
        $(obj).parents("tr").remove();
        $.ajax({
            url: "/case/delete",
            data: {"id": id},
            method: "DELETE",
            success: function (obj) {
                layer.msg('successfully delete!', {icon: 1, time: 1000});
            }
        })

    });
}

/*查询*/
function get_search() {
    param = ' 1=1 ';
    case_type_s = $("#case_type_s").val();
    case_area_s = $("#case_area_s").val();
    content_s = $("#content_s").val();

    if (content_s != null && content_s != '') {
        param = param + " and content LIKE '%%" + content_s + "%%'";
    }
    if (case_type_s != null && case_type_s != '') {
        param = param + " and case_type LIKE '%%" + case_type_s + "%%'";
    }
    if (case_area_s != null && case_area_s != '') {
        param = param + " and case_area LIKE '%%" + case_area_s + "%%'";
    }
    all_page_param = param;
    get_case_data(page_no)
}

function case_import() {
    $('#file').val('')
    layer.open({
        type: 1,
        area: ['600px', '200px'],
        fix: false, //fluid
        maxmin: true,
        shadeClose: true,
        shade: 0.4,
        title: 'One-click import',
        content: $('#case-import')
    });
}

