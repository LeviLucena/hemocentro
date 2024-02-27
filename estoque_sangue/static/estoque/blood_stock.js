// JavaScript

$(document).ready(function() {
    $('#hemocentro').change(function() {
        var selectedHemocentro = $(this).val();
        $.ajax({
            url: '/get_blood_types/',
            method: 'GET',
            data: { hemocentro_id: selectedHemocentro },
            success: function(response) {
                var bloodTypesHTML = '';
                response.forEach(function(bloodType) {
                    bloodTypesHTML += '<div class="mb-3">';
                    bloodTypesHTML += '<label for="' + bloodType + '" class="form-label">' + bloodType + '</label>';
                    bloodTypesHTML += '<div class="row">';
                    bloodTypesHTML += '<div class="col">';
                    bloodTypesHTML += '<input type="number" class="form-control blood-stock" id="' + bloodType + '" name="' + bloodType + '_stock" placeholder="Estoque Atual">';
                    bloodTypesHTML += '</div>';
                    bloodTypesHTML += '<div class="col">';
                    bloodTypesHTML += '<input type="number" class="form-control blood-stock" id="' + bloodType + '_min" name="' + bloodType + '_min" placeholder="Estoque Mínimo">';
                    bloodTypesHTML += '</div>';
                    bloodTypesHTML += '</div>';
                    bloodTypesHTML += '</div>';
                });
                $('#blood-types').html(bloodTypesHTML);
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        });
    });
});
