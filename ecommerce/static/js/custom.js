


$(function() {
    $('.increment-btn').on('click', e => {
        e.preventDefault();
        const inc_value = $(e.currentTarget).closest('.product_data').find('.qty-input').val();
        let value = parseInt(inc_value, 10);
        value = isNaN(value) ? 0 : value;
        if (value < 10) {
            value++;
            $(e.currentTarget).closest('.product_data').find('.qty-input').val(value);
        }
    });

    $('.decrement-btn').on('click', e => {
        e.preventDefault();
        const dec_value = $(e.currentTarget).closest('.product_data').find('.qty-input').val();
        let value = parseInt(dec_value, 10);
        value = isNaN(value) ? 0 : value;
        if (value > 1) {
            value--;
            $(e.currentTarget).closest('.product_data').find('.qty-input').val(value);
        }
    });
   
    $('.addToCartBtn').on('click', e => {
        e.preventDefault();
        var productData = $(e.currentTarget).closest('.product_data');
        var product_id = productData.find('.prod_id').val();
        var product_qty = productData.find('.qty-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/add-to-cart",
            data: {
                'product_id': product_id,
                'product_qty': product_qty,
                'csrfmiddlewaretoken' : token
            },
            success: function(response){
                console.log(response)
                alertify.success(response.status)
            }
        });
    });
    $('.addToWishlist').on('click', e => {
        e.preventDefault();
        var productData = $(e.currentTarget).closest('.product_data');
        var product_id = productData.find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/add-to-wishlist",
            data: {
                'product_id': product_id,
                'csrfmiddlewaretoken' : token
            },
            success: function(response){
                console.log(response)
                alertify.success(response.status)
            }
        });
    });

    $('.changeQuantity').on('click', e => {
        e.preventDefault();
        var productData = $(e.currentTarget).closest('.product_data');
        var product_id = productData.find('.prod_id').val();
        var product_qty = productData.find('.qty-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/update-cart",
            data: {
                'product_id': product_id,
                'product_qty': product_qty,
                'csrfmiddlewaretoken' : token
            },
            success: function(response){
                console.log(response)
                alertify.success(response.status)
            }
        });
    });

    $(document).on('click','.delete-cart-item',function(e) {

    
        e.preventDefault();
        var productData = $(e.currentTarget).closest('.product_data');
        var product_id = productData.find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/delete-cart-item",
            data: {
                'product_id': product_id,
                'csrfmiddlewaretoken' : token
            },
            success: function(response){
                console.log(response)
                alertify.success(response.status)
                // $('.cartdata').load(location.href + " .cartdata");
                location.reload();
            }
        });
    });

    $(document).on('click','.delete-wishlist-item',function(e) {

    e.preventDefault();
        var productData = $(e.currentTarget).closest('.product_data');
        var product_id = productData.find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/delete-wishlist-item",
            data: {
                'product_id': product_id,
                'csrfmiddlewaretoken' : token
            },
            success: function(response){
                console.log(response)
                alertify.success(response.status)
                // $('.cartdata').load(location.href + " .cartdata");
                location.reload();
            }
        });
    });
    

  



});
