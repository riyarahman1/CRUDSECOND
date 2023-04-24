$(document).ready(function () {
    if ($('#table') != null) {
        Read();
    }



    $('#create2').on('click', function () {
        var subcategory = $('#subcategory').val();
        console.log(subcategory);

        var title = $('#title').val();
        var description = $('#description').val();
        var nameRegex = /^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$/;

        // if (category.trim() == "" || product_name.trim() == "") {
        //     alert("Please complete the required field");
        // } else 
        if (!nameRegex.test(title) || (!nameRegex.test(description))) {
            alert("please complete the required fields");
        } else {
            $.ajax({
                url: 'project',
                type: 'POST',
                data: {
                    subcategory: subcategory,
                    title: title,
                    description: description,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function () {
                    Read();
                    $('#subcategory').val('');
                    $('#title').val('');
                    $('#description').val('');
                    alert("New Project Successfully Added");
                }
            });
        }
    });

    $(document).on('click', '.toggle-active-btn', function () {
        var project_id = $(this).data('projectcategory-id');
        var csrf_token = $(this).data('csrf-token');

        $.ajax({
            url: '/project/' + project_id + '/toggle-active/',
            method: 'POST',
            data: {
                'csrfmiddlewaretoken': csrf_token
            },
            success: function (response) {
                if (response.status === 'success') {
                    $('.toggle-active-btn[data-projectcategory-id=' + project_id + ']').text(response.is_active ? 'Disable' : 'Enable');
                } else {
                    alert(response.message);
                }
            },
            error: function (xhr, status, error) {
                console.log('Error:', error);
            }
        });
    });
    function Read() {
        $.ajax({
            async: true,
            url: 'project/viewproject/',
            type: 'POST',

            data: {
                res: 1,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function (response) {
                $('#table').html(response);
            }
        });
    }
});