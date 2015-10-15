USE_PKGBUILD=1
include /usr/local/share/luggage/luggage.make
TITLE=OnCorpCondition
REVERSE_DOMAIN=com.grahamgilbert
PACKAGE_VERSION=0.1
PAYLOAD= \
	pack-condition

pack-condition: l_usr_local
	@sudo mkdir -p ${WORK_D}/usr/local/munki/conditions
	@sudo ${CP} on_corp.py ${WORK_D}/usr/local/munki/conditions/on_corp.py
	@sudo chmod 755 ${WORK_D}/usr/local/munki/conditions/on_corp.py
	@sudo chown root:wheel ${WORK_D}/usr/local/munki/conditions/on_corp.py
