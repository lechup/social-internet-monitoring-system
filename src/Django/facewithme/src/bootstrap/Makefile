BOOTSTRAP_SRC_DIR = ./src/
BOOTSTRAP = ../../apps/core/static/core/lib/bootstrap/css/bootstrap.css
BOOTSTRAP_LESS = ${BOOTSTRAP_SRC_DIR}less/bootstrap.less
BOOTSTRAP_RESPONSIVE = ../../apps/core/static/core/lib/bootstrap/css/bootstrap-responsive.css
BOOTSTRAP_RESPONSIVE_LESS = ${BOOTSTRAP_SRC_DIR}less/responsive.less
BOOTSTRAP_JS_MIN = ../../apps/core/static/core/lib/bootstrap/js/bootstrap.min.js
DATE=$(shell date +%I:%M%p)
CHECK=\033[32m✔\033[39m
HR=\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#


#
# BUILD DOCS
#

build:
	@echo "\n${HR}"
	@echo "Building Bootstrap..."
	@echo "${HR}\n"
	@jshint ${BOOTSTRAP_SRC_DIR}js/*.js --config ${BOOTSTRAP_SRC_DIR}js/.jshintrc
	@jshint ${BOOTSTRAP_SRC_DIR}js/tests/unit/*.js --config ${BOOTSTRAP_SRC_DIR}js/.jshintrc
	@echo "Running JSHint on javascript...             ${CHECK} Done"
	@recess --compile ${BOOTSTRAP_LESS} > ${BOOTSTRAP}
	@recess --compile ${BOOTSTRAP_RESPONSIVE_LESS} > ${BOOTSTRAP_RESPONSIVE}
	@echo "Compiling LESS with Recess...               ${CHECK} Done"
#	@node docs/build
#	@cp img/* docs/assets/img/
#	@cp ${BOOTSTRAP_SRC_DIR}js/*.js docs/assets/${BOOTSTRAP_SRC_DIR}js/
#	@cp ${BOOTSTRAP_SRC_DIR}js/tests/vendor/jquery.js docs/assets/${BOOTSTRAP_SRC_DIR}js/
#	@echo "Compiling documentation...                  ${CHECK} Done"
	@cat ${BOOTSTRAP_SRC_DIR}js/bootstrap-transition.js ${BOOTSTRAP_SRC_DIR}js/bootstrap-alert.js ${BOOTSTRAP_SRC_DIR}js/bootstrap-button.js ${BOOTSTRAP_SRC_DIR}js/bootstrap-carousel.js ${BOOTSTRAP_SRC_DIR}js/bootstrap-collapse.js ${BOOTSTRAP_SRC_DIR}js/bootstrap-dropdown.js ${BOOTSTRAP_SRC_DIR}js/bootstrap-modal.js ${BOOTSTRAP_SRC_DIR}js/bootstrap-tooltip.js ${BOOTSTRAP_SRC_DIR}js/bootstrap-popover.js ${BOOTSTRAP_SRC_DIR}js/bootstrap-scrollspy.js ${BOOTSTRAP_SRC_DIR}js/bootstrap-tab.js ${BOOTSTRAP_SRC_DIR}js/bootstrap-typeahead.js > ${BOOTSTRAP_SRC_DIR}docs/assets/js/bootstrap.js
	@uglifyjs -nc ${BOOTSTRAP_SRC_DIR}docs/assets/js/bootstrap.js > ${BOOTSTRAP_SRC_DIR}docs/assets/js/bootstrap.min.tmp.js
	@echo "/**\n* Bootstrap.js by @fat & @mdo\n* Copyright 2012 Twitter, Inc.\n* http://www.apache.org/licenses/LICENSE-2.0.txt\n*/" > ${BOOTSTRAP_SRC_DIR}docs/assets/js/copyright.js
	@cat ${BOOTSTRAP_SRC_DIR}docs/assets/js/copyright.js ${BOOTSTRAP_SRC_DIR}docs/assets/js/bootstrap.min.tmp.js > ${BOOTSTRAP_SRC_DIR}docs/assets/js/bootstrap.min.js
	@rm ${BOOTSTRAP_SRC_DIR}docs/assets/js/copyright.js ${BOOTSTRAP_SRC_DIR}docs/assets/js/bootstrap.min.tmp.js
	@cat ${BOOTSTRAP_SRC_DIR}docs/assets/js/bootstrap.min.js > ${BOOTSTRAP_JS_MIN}
	@echo "Compiling and minifying javascript...       ${CHECK} Done"
	@echo "\n${HR}"
	@echo "Bootstrap successfully built at ${DATE}."
	@echo "${HR}\n"
	@echo "Thanks for using Bootstrap,"
	@echo "<3 @mdo and @fat\n"

