URJTAG=urjtag/

wheel: $(URJTAG)src/.libs/liburjtag.a
	python3 -m build --wheel

$(URJTAG)src/.libs/liburjtag.a: $(URJTAG)config.status .FORCE
	$(MAKE) -C $(URJTAG)

# --disable-python as we build a wheel from here
$(URJTAG)config.status: $(URJTAG)
	cd $(URJTAG) && ./configure --disable-bus --enable-cable=ft2232 --disable-shared --disable-apps --disable-jedec-exp --without-readline --disable-python --enable-relocatable CFLAGS=-fPIC

# setuptools seem to require to be on top; so create a symlink to 
# the sibling
$(URJTAG):
	ln -s ../urjtag .

clean distclean:
	$(MAKE) -C $(URJTAG) $@
	$(RM) -r build/ dist/ *.egg-info/
	if [ $@ = distclean ] ; then $(RM) urjtag ; fi
	
.PHONY: .FORCE wheel clean distclean
