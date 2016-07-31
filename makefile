project=index


${project}: ${project}.org
	emacs ${project}.org -u "$(id -un)" --batch  -f org-publish-project 

${project}.org: FORCE
	python3 make_${project}org.py

FORCE:




