$(document).ready(function(){
    if($('#res') != null){
        Read();
    }



    $('#create1').on('click', function () {
        var category = $('#category').val();
        console.log(category);
       
        var project_name = $('#project_name').val();
        var nameRegex = /^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$/;

        // if (category.trim() == "" || product_name.trim() == "") {
        //     alert("Please complete the required field");
        // } else 
        if (!nameRegex.test(project_name)) {
            alert("please compleate the required fields");
        } else {
            $.ajax({
                url: 'create_project',
                type: 'POST',
                data: {
                    category: category,
                    project_name: project_name,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function () {
                    Read();
                    $('#category').val('');
                    $('#product_name').val('');
                    alert("New Subcategory Successfully Added");
                }
            });
        }
    });

    $(document).on('click', '.toggle-active-btn', function () {
        var projectcategory_id = $(this).data('projectcategory-id');
        var csrf_token = $(this).data('csrf-token');

        $.ajax({
            url: '/projectcategory/' + projectsubcategory_id + '/toggle-active/',
            method: 'POST',
            data: {
                'csrfmiddlewaretoken': csrf_token
            },
            success: function (response) {
                if (response.status === 'success') {
                    $('.toggle-active-btn[data-projectcategory-id=' + projectsubcategory_id + ']').text(response.is_active ? 'Disable' : 'Enable');
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
            url: 'create_project/read1/',
            type: 'POST',



            data: {
                res: 1,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function (response) {
                $('#res').html(response);
            }
        });
    }
});