###############################################################################
MK_INFO := https://pypi.org/project/vmklib
ifeq (,$(shell which mk))
$(warning "No 'mk' in $(PATH), install 'vmklib' with 'pip' ($(MK_INFO))")
endif
ifndef MK_AUTO
$(error target this Makefile with 'mk', not '$(MAKE)' ($(MK_INFO)))
endif
###############################################################################

.PHONY: build edit env host host-coverage format lint test yaml

# Link the project directory to the 'src' directory.
$($(PROJ)_DIR)/$(PROJ):
	cd $($(PROJ)_DIR) && ln -s src $(PROJ)

.DEFAULT_GOAL := host

env: $(VENV_CONC) $($(PROJ)_DIR)/$(PROJ)

build: env
	npx parcel build

edit: env $(PY_PREFIX)edit

host: env
	npx parcel --no-cache

host-coverage:
	cd $($(PROJ)_DIR)/coverage/lcov-report && python -m http.server 0

format: env
	npx eslint --fix $($(PROJ)_DIR)/src
	npx prettier -w $($(PROJ)_DIR)/src

lint: env
	npx eslint $($(PROJ)_DIR)/src
	npx prettier --check $($(PROJ)_DIR)/src

test: env
	npx jest --coverage

yaml: $(YAML_PREFIX)lint-local $(YAML_PREFIX)lint-manifest.yaml

test-%: env
	npx jest -t $*
