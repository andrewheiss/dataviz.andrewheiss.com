OUTPUTDIR=public
SSH_TARGET=cloud:/home/andrew/sites/dataviz/public_html

.PHONY : all

all: build

clean:
	rm -rf public/

build: clean
	Rscript -e "blogdown::build_site()"

serve: build
	Rscript -e "blogdown::serve_site(port=4321)"

deploy: build
	rsync -Prvzc --delete $(OUTPUTDIR)/ $(SSH_TARGET)
