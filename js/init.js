---
# Empty YAML header gets Jekyll to process this, important for {{ site.baseurl }} processing
---
/*
	Standout by Pixelarity
	pixelarity.com @pixelarity
	License: pixelarity.com/license
*/

(function($) {

	skel.init({
		reset: 'full',
		breakpoints: {
			'global':	{ range: '*', href: '{{ site.baseurl }}/css/style.css' },
			'desktop':	{ range: '737-', href: '{{ site.baseurl }}/css/style-desktop.css', containers: 1200, grid: { gutters: 25 } },
			'1000px':	{ range: '737-1200', href: '{{ site.baseurl }}/css/style-1000px.css', containers: 1000, grid: { gutters: 20 }, viewport: { width: 1080 } },
			'mobile':	{ range: '-736', href: '{{ site.baseurl }}/css/style-mobile.css', containers: '100%!', grid: { collapse: true, gutters: 15 }, viewport: { scalable: false } }
		},
		plugins: {
			layers: {
				config: {
					mode: 'transform'
				},
				navPanel: {
					hidden: true,
					breakpoints: 'mobile',
					position: 'top-left',
					side: 'left',
					animation: 'pushX',
					width: '80%',
					height: '100%',
					clickToHide: true,
					html: '<div data-action="navList" data-args="nav"></div>',
					orientation: 'vertical'
				},
				titleBar: {
					breakpoints: 'mobile',
					position: 'top-left',
					side: 'top',
					height: 44,
					width: '100%',
					html: '<span class="toggle" data-action="toggleLayer" data-args="navPanel"></span><span class="title" data-action="copyHTML" data-args="logo"></span>'
				}
			}
		}
	});

	$(function() {

		var	$window = $(window);

		// Forms (IE<10).
			var $form = $('form');
			if ($form.length > 0) {

				$form.find('.form-button-submit')
					.on('click', function() {
						$(this).parents('form').submit();
						return false;
					});

				if (skel.vars.IEVersion < 10) {
					$.fn.n33_formerize=function(){var _fakes=new Array(),_form = $(this);_form.find('input[type=text],textarea').each(function() { var e = $(this); if (e.val() == '' || e.val() == e.attr('placeholder')) { e.addClass('formerize-placeholder'); e.val(e.attr('placeholder')); } }).blur(function() { var e = $(this); if (e.attr('name').match(/_fakeformerizefield$/)) return; if (e.val() == '') { e.addClass('formerize-placeholder'); e.val(e.attr('placeholder')); } }).focus(function() { var e = $(this); if (e.attr('name').match(/_fakeformerizefield$/)) return; if (e.val() == e.attr('placeholder')) { e.removeClass('formerize-placeholder'); e.val(''); } }); _form.find('input[type=password]').each(function() { var e = $(this); var x = $($('<div>').append(e.clone()).remove().html().replace(/type="password"/i, 'type="text"').replace(/type=password/i, 'type=text')); if (e.attr('id') != '') x.attr('id', e.attr('id') + '_fakeformerizefield'); if (e.attr('name') != '') x.attr('name', e.attr('name') + '_fakeformerizefield'); x.addClass('formerize-placeholder').val(x.attr('placeholder')).insertAfter(e); if (e.val() == '') e.hide(); else x.hide(); e.blur(function(event) { event.preventDefault(); var e = $(this); var x = e.parent().find('input[name=' + e.attr('name') + '_fakeformerizefield]'); if (e.val() == '') { e.hide(); x.show(); } }); x.focus(function(event) { event.preventDefault(); var x = $(this); var e = x.parent().find('input[name=' + x.attr('name').replace('_fakeformerizefield', '') + ']'); x.hide(); e.show().focus(); }); x.keypress(function(event) { event.preventDefault(); x.val(''); }); });  _form.submit(function() { $(this).find('input[type=text],input[type=password],textarea').each(function(event) { var e = $(this); if (e.attr('name').match(/_fakeformerizefield$/)) e.attr('name', ''); if (e.val() == e.attr('placeholder')) { e.removeClass('formerize-placeholder'); e.val(''); } }); }).bind("reset", function(event) { event.preventDefault(); $(this).find('select').val($('option:first').val()); $(this).find('input,textarea').each(function() { var e = $(this); var x; e.removeClass('formerize-placeholder'); switch (this.type) { case 'submit': case 'reset': break; case 'password': e.val(e.attr('defaultValue')); x = e.parent().find('input[name=' + e.attr('name') + '_fakeformerizefield]'); if (e.val() == '') { e.hide(); x.show(); } else { e.show(); x.hide(); } break; case 'checkbox': case 'radio': e.attr('checked', e.attr('defaultValue')); break; case 'text': case 'textarea': e.val(e.attr('defaultValue')); if (e.val() == '') { e.addClass('formerize-placeholder'); e.val(e.attr('placeholder')); } break; default: e.val(e.attr('defaultValue')); break; } }); window.setTimeout(function() { for (x in _fakes) _fakes[x].trigger('formerize_sync'); }, 10); }); return _form; };
					$form.n33_formerize();
				}

			}

		// Dropdowns.
			$('#nav > ul').dropotron({
				offsetY: -20,
				offsetX: -1,
				mode: 'fade',
				alignment: 'center',
				noOpenerFade: true
			});

		// Slider.
			var $slider = $('#slider');
			if ($slider.length > 0) {

				$slider.slidertron({
					mode: 'fade',
					seamlessWrap: false,
					viewerSelector: '.viewer',
					speed: 'slow',
					autoFit: true,
					autoFitAspectRatio: (1200 / 635),
					reelSelector: '.viewer .reel',
					slidesSelector: '.viewer .reel .slide',
					advanceDelay: 5000,
					speed: 'slow',
					navPreviousSelector: '.previous-button',
					navNextSelector: '.next-button',
					indicatorSelector: '.indicator ul li',
					slideLinkSelector: '.link',
					captionLines: 1,
					captionLineSelector: '.captionLine',
					slideCaptionSelector: '.caption'
				});

				$window
					.on('resize load', function() {
						$slider.trigger('slidertron_reFit');
					})
					.trigger('resize');

			}

	// Portfolio.
		var $portfolio = $('#portfolio');
		if ($portfolio.length > 0) {

			var _settings;

			$portfolio.rotatorrr({
				titlesSelector: '.titles li',
				slidesSelector: '.category'
			});

			if (skel.isActive('mobile')) {

				$portfolio.find('.button-top').click(function(e) {
					_bh.animate({ scrollTop: $portfolio.offset().top - 60 }, 800, 'swing');
					return false;
				});

				_settings = {
					baseZIndex: 100000,
					usePopupCaption: true,
					overlayOpacity: 0.8,
					useBodyOverflow: false,
					usePopupCloser: false,
					popupPadding: 0,
					windowMargin: 5,
					popupCaptionHeight: 40,
					popupSpeed: 0,
					fadeSpeed: 0,
					overlayClass: 'poptrox-overlay skel-layers-fixed'
				};

			}
			else
				_settings = {
					baseZIndex: 100000,
					usePopupCaption: true,
					overlayOpacity: 0.8,
					useBodyOverflow: false,
					usePopupCloser: false,
					overlayClass: 'poptrox-overlay skel-layers-fixed'
				};

			$portfolio.find('.category').each(function() {
				$(this).poptrox(_settings);
			});

		}
	});

})(jQuery);