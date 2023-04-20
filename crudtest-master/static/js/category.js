$(document).ready(function () {
    if ($('#result') != null) {
        Read();
    }

    $('#create').on('click', function () {
        var name = $('#name').val();
        var nameRegex = /^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$/;

        if (name.trim() == "") {
            alert("Please complete the required field");
        } else if (!nameRegex.test(name)) {
            alert("Name can only contain letters and spaces");
        } else {
            $.ajax({
                url: 'create/',
                type: 'POST',
                data: {
                    name: name,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function () {
                    Read();
                    $('#name').val('');
                    alert("New Category Successfully Added");
                }
            });
        }
    });
    $(document).on('click', '.edit', function () {
        $id = $(this).attr('name');
        window.location = "edit/" + $id;
    });

    // $(document).on('click', '.user-edit', function (event) {
    //     console.log("updateddddddd");
    //     event.preventDefault();
    //     var name = $('input[name="name"]').val();
    //     var nameRegex = /^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$/;
    
    //     if (name.trim() == "") {
    //         alert("Please complete the required field");
    //     } else if (!nameRegex.test(name)) {
    //         alert("Name can only contain letters and spaces");
    //     } else {
    //         var id = $('#member_id').val();
    //         $('#name').val(name); // update input field value
    //         $.ajax({
    //             url: 'update/' + id,
    //             type: 'POST',
    //             data: {
    //                 name: name,
    //                 csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
    //             },
    //             success: function () {
    //                 alert('Updated!');
    //                 window.location = '';
    //             }
    //         });
    //     }
    // });

    $(document).on('click', '.user-edit', function (event) {
        console.log("updateddddddd");
        event.preventDefault();
        var name = $('input[name="name"]').val();
        var nameRegex = /^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$/;
      
        if (name.trim() == "") {
          alert("Please complete the required field");
        } else if (!nameRegex.test(name)) {
          alert("Name can only contain letters and spaces");
        } else {
          var id = $('#category_id').val();
          $('#name').val(name); // update input field value
          console.log(id);
          $.ajax({
            url: 'update/' + id ,
            type: 'POST',
            data: {
              id: id,
              name: name,
              csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function () {
              alert('Updated!');
              window.location = '';
            }
          });
        }
      });
      
    
    $(document).on('click', '.toggle-active-btn', function () {
        var projectcategory_id = $(this).data('projectcategory-id');
        var csrf_token = $(this).data('csrf-token');

        $.ajax({
            url: '/projectcategory/' + projectcategory_id + '/toggle-active/',
            method: 'POST',
            data: {
                'csrfmiddlewaretoken': csrf_token
            },
            success: function (response) {
                if (response.status === 'success') {
                    $('.toggle-active-btn[data-projectcategory-id=' + projectcategory_id + ']').text(response.is_active ? 'Disable' : 'Enable');
                } else {
                    alert(response.message);
                }
            },
            error: function (xhr, status, error) {
                console.log('Error:', error);
            }
        });
    });

    $(document).on('click', '.delete', function () {
        $id = $(this).attr('name');
        $.ajax({
            url: 'delete/' + $id,
            type: 'POST',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function () {
                Read();
                alert("Deleted!");
            }
        });
    });

});





function Read() {
    $.ajax({
        async: true,
        url: 'read/',
        type: 'POST',

        data: {
            res: 1,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function (response) {
            $('#result').html(response);
        }
    });
}






