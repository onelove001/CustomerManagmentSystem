(function( $ ) {
	'use strict';

	/**
	 * All of the code for your public-facing JavaScript source
	 * should reside in this file.
	 *
	 * Note: It has been assumed you will write jQuery code here, so the
	 * $ function reference has been prepared for usage within the scope
	 * of this function.
	 *
	 * This enables you to define handlers, for when the DOM is ready:
	 *
	 * $(function() {
	 *
	 * });
	 *
	 * When the window is loaded:
	 *
	 * $( window ).load(function() {
	 *
	 * });
	 *
	 * ...and/or other possibilities.
	 *
	 * Ideally, it is not considered best practise to attach more than a
	 * single DOM-ready or window-load handler for a particular page.
	 * Although scripts in the WordPress core, Plugins and Themes may be
	 * practising this, we should strive to set a better example in our own work.
	 */

	var active_day = 0,
		total_days;

    $( document ).ready(function() {
        init();
	});

    function init(){

        $('.timetable__entry').on('click', function(){
            $(this).toggleClass('is-active');
        });

        $('.timetable__previous').on('click', function(){
        	go_to_day( active_day-1, true );
		});

        $('.timetable__next').on('click', function(){
        	go_to_day( active_day+1, true );
		});

        $('.timetable__date').on('click', function(){
        	go_to_day( $(this).index(), false );
		});

        $('.timetable__details').on('click', function(e){
        	e.stopPropagation();
		});

        total_days = $('.timetable__date').length;
	}

    function go_to_day(day, move){
    	if( day < 0 || day > total_days-1 )
    		return;

        $('.timetable__date, .timetable__day').removeClass('is-active');

        $('.timetable__date').eq(day).addClass('is-active');
        $('.timetable__day').eq(day).addClass('is-active');

        var percentage = 0,
			visible = 7;

        if(move){
            if( day > active_day ) {
                if( day == total_days-1 ) {
                    percentage = (day - (visible-1)) * 100;
                } else if( day > (visible-2) && day < total_days-1 ){
                    percentage = (day - (visible-2)) * 100;
                }
            } else {
                if(day > (visible-1)){
                    percentage = (day - (visible-1)) * 100;
                }
            }

            $('.timetable__date').css("transform", "translateX(-" + percentage + "%)");
		}

		active_day = day;
	}

})( jQuery );
