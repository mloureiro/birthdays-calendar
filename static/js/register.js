(function ($) {
  'use strict';
  /*==================================================================
    [ Daterangepicker ]*/
  try {
    $('.js-datepicker').daterangepicker({
      "singleDatePicker": true,
      "showDropdowns": true,
      "autoUpdateInput": false,
      locale: {
        format: 'DD/MM/YYYY'
      },
    });

    const myCalendar = $('.js-datepicker');
    let isClick = 0;

    $(window).on('click',function(){
      isClick = 0;
    });

    $(myCalendar).on('apply.daterangepicker',function(ev, picker){
      isClick = 0;
      $(this).val(picker.startDate.format('DD/MM/YYYY'));

    });

    $('.js-btn-calendar').on('click',function(e){
      e.stopPropagation();

      if(isClick === 1) isClick = 0;
      else if(isClick === 0) isClick = 1;

      if (isClick === 1) {
        myCalendar.focus();
      }
    });

    $(myCalendar).on('click',function(e){
      e.stopPropagation();
      isClick = 1;
    });

    $('.daterangepicker').on('click',function(e){
      e.stopPropagation();
    });


  } catch(er) {console.log(er);}
  /*[ Select 2 Config ]
    ===========================================================*/

  try {
    const selectSimple = $('.js-select-simple');

    selectSimple.each(function () {
      const that = $(this);
      const selectBox = that.find('select');
      const selectDropdown = that.find('.select-dropdown');
      selectBox.select2({
        dropdownParent: selectDropdown
      });
    });

  } catch (err) {
    console.log(err);
  }

})(jQuery);
