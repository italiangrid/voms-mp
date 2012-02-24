spec=emi-voms-mysql.spec emi-voms-oracle.spec
rpmbuild_dir=$(shell pwd)/rpmbuild

.PHONY: etics clean rpm

all: 	clean rpm

clean:	
		rm -rf $(rpmbuild_dir) tgz RPMS 

rpm:		
		mkdir -p 	$(rpmbuild_dir)/BUILD $(rpmbuild_dir)/RPMS \
					$(rpmbuild_dir)/SOURCES $(rpmbuild_dir)/SPECS \
					$(rpmbuild_dir)/SRPMS

		tar -cvzf $(rpmbuild_dir)/SOURCES/voms-mp.tar.gz *.spec
		rpmbuild -v -ba $(spec) --define "_topdir $(rpmbuild_dir)" 

etics: 	clean rpm
		mkdir -p tgz RPMS
		cp target/*.tar.gz tgz
		cp -r $(rpmbuild_dir)/RPMS/* $(rpmbuild_dir)/SRPMS/* RPMS
